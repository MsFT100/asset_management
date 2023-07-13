import os
import sys
from django.shortcuts import render, redirect, get_object_or_404
from .models import Company
from .forms import CompanyForm
from django.core.paginator import Paginator
from django.core.files.storage import default_storage
from django.contrib.auth.decorators import login_required, permission_required
from django.http import Http404
from django.conf import settings
from urllib.parse import urlencode
from config import config

sys.path.append('..')

@login_required
@permission_required("company.add_company", raise_exception=True)
def company_create(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('company_list')

    else:
        form = CompanyForm()
    return render(request, 'company_create.html', {"form": form})



@login_required
@permission_required("company.view_company", raise_exception=True)
def company_list(request):

    default_val = config.DEFAULT_PER_COMPANY
    max_val = config.MAX_PER_COMPANY

    company_list = Company.objects.get_queryset().order_by('id')

    # Configure the default number of items per page
    default_items_per_page = default_val

    # Get the requested page number from the request's GET parameters
    page_number = request.GET.get('page')

    # Get the requested items per page from the request's GET parameters
    items_per_page = request.GET.get('size', default_items_per_page)

    # Validate and convert items_per_page to an integer
    try:
        items_per_page = int(items_per_page)
        if items_per_page < 1 or items_per_page > int(max_val):  # Limit the maximum page size to max_val
            items_per_page = max_val
            # Update the URL to set the maximum page size
            params = request.GET.copy()
            params['size'] = max_val
            updated_url = f"{request.path}?{params.urlencode()}"
            return redirect(updated_url)
    except ValueError:
        items_per_page = default_items_per_page

    paginator = Paginator(company_list, items_per_page)

    # Retrieve the page object for the requested page number
    company_list = paginator.get_page(page_number)

    context = {
        'company_list': company_list,
        'size': items_per_page,
    }
    return render(request, 'company_list.html', context)


@login_required
@permission_required("company.change_company", raise_exception=True)
def company_edit(request, company_id):
    company = get_object_or_404(Company, id=company_id)
    if request.user.company.id == company_id:
        if request.method == 'POST':        
                form = CompanyForm(request.POST, request.FILES, instance=company)
                if form.is_valid():
                    if 'logo' in form.changed_data:
                        previous_logo_path = company.logo.path
                        if os.path.exists(previous_logo_path):
                            os.remove(previous_logo_path)
                    
                    form.save()
                    return redirect('company_details', company_id=company_id)
        else:        
            # company = get_object_or_404(Company, id=company_id)
            form = CompanyForm(instance=company)

        return render(request, 'company_edit.html', {'form': form})

    else:
        raise Http404("Company not found.")

@login_required
@permission_required("company.view_company", raise_exception=True)
def company_details(request, company_id):
    company = get_object_or_404(Company, id=company_id)
    if request.user.company.id == company.id:
        return render(request, 'company_details.html', {'company': company})
    else:
        raise Http404("Company not found.")
    
@login_required
@permission_required("company.delete_company", raise_exception=True)
def company_delete(request, company_id):
    company = get_object_or_404(Company, id=company_id)
    if request.user.company.id == company.id:
        
        if request.method == "POST":
            company.delete()
            return redirect('company_list')
        context = {
            'company': company
        }
        return render(request, "company_delete.html", context)
    
    else:
        raise Http404("Company not found.")


    
