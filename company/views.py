
from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import HttpResponse
from .models import Company
from .forms import CompanyForm

from django.contrib.auth.decorators import login_required, permission_required


@login_required
@permission_required("company.add_company", raise_exception=True)
def company_create(request):
    if request.method == "POST":
        form = CompanyForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('company_index')
            except:
                pass
    else:
        form = CompanyForm()

    return render(request, "company_create.html", {'form': form})


@login_required
@permission_required("company.view_company", raise_exception=True)
def company_list(request):
    company_list = Company.objects.get_queryset().order_by('id')

    # Configure the number of items per page
    items_per_page = 5
    paginator = Paginator(company_list, items_per_page)

    # Get the current page number from the request's GET parameters
    page_number = request.GET.get('page')

    # Retrieve the page object for the requested page number
    company_list = paginator.get_page(page_number)

    user = request.user
    permissions = user.get_all_permissions()

    user_permissions = []
    for permission in permissions:
        if user.has_perm(permission):
            user_permissions.append(permission)

    context = {
        'company_list': company_list,
        'permissions': user_permissions
    }
    return render(request, 'company_list.html', context)


@login_required
def company_edit(request):

    return render(request, "company_edit.html", {'test': 'sdf'})
