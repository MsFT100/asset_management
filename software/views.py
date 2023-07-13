import os
import sys
from django.shortcuts import render, redirect, get_object_or_404
from config import config
from .models import Software
from .forms import SoftwareForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required, permission_required
from django.http import Http404
from django.conf import settings
from urllib.parse import urlencode


sys.path.append('..')

@login_required
@permission_required("software.add_software", raise_exception=True)
def software_create(request):
    if request.method == 'POST':
        form = SoftwareForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.company = request.user.company
            obj.save()
            # TODO :CORRECT THIS
            return redirect('software_list')

    else:
        form = SoftwareForm()
    return render(request, 'software_create.html', {"form": form})

@login_required
@permission_required("software.view_software", raise_exception=True)
def software_list(request):
    softwares = Software.objects.filter(company=request.user.company).order_by('id')

    # Configure the number of items per page
    items_per_page = 5
    paginator = Paginator(softwares, items_per_page)

    # Get the current page number from the request's GET parameters
    page_number = request.GET.get('page')

    # Retrieve the page object for the requested page number
    software_list = paginator.get_page(page_number)

    context = {
        'software_list': software_list,
    }
    return render(request, 'software_list.html', context)

@login_required
@permission_required("software.view_software", raise_exception=True)
def software_details(request, software_id):
    software = get_object_or_404(Software, id=software_id)
    return render(request, 'software_details.html', {'software': software})


@login_required
@permission_required("software.change_software", raise_exception=True)
def software_edit(request, software_id):
    software = get_object_or_404(Software, id=software_id)
    if software.company is not None and request.user.company.id == software.company.id:
        if request.method == 'POST':
            form = SoftwareForm(request.POST, instance=software)
            if form.is_valid():
                form.save()
                return redirect('software_details', software_id=software_id)
        else:
            form = SoftwareForm(instance=software)

        return render(request, 'software_edit.html', {'form': form})
    else:
         raise Http404("Software not found.")


        

@login_required
@permission_required("software.delete_software", raise_exception=True)
def software_delete(request, software_id):
    software = get_object_or_404(Software, id=software_id)
    if request.user.company.id == software.company.id:

        
        if request.method == "POST":
            software.delete()
            return redirect('software_list')
        context = {
            'software': software
        }
        return render(request, "software_delete.html", context)
    
    else:
        raise Http404("Software not found.")


