import os
import sys
from django.shortcuts import render, redirect, get_object_or_404
from config import config
from .models import Department
from .forms import DepartmentForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required, permission_required
from django.http import Http404
from django.conf import settings
from urllib.parse import urlencode


sys.path.append('..')

@login_required
@permission_required("department.add_department", raise_exception=True)
def department_create(request):
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.company = request.user.company
            obj.save()
            # TODO :CORRECT THIS
            return redirect('department_list')

    else:
        form = DepartmentForm()
    return render(request, 'department_create.html', {"form": form})

@login_required
@permission_required("department.view_department", raise_exception=True)
def department_list(request):
    departments = Department.objects.filter(company=request.user.company).order_by('id')

    # Configure the number of items per page
    items_per_page = 5
    paginator = Paginator(departments, items_per_page)

    # Get the current page number from the request's GET parameters
    page_number = request.GET.get('page')

    # Retrieve the page object for the requested page number
    department_list = paginator.get_page(page_number)

    context = {
        'department_list': department_list,
    }
    return render(request, 'department_list.html', context)

@login_required
@permission_required("department.view_department", raise_exception=True)
def department_details(request, department_id):
    department = get_object_or_404(Department, id=department_id)
    return render(request, 'department_details.html', {'department': department})


@login_required
@permission_required("department.change_department", raise_exception=True)
def department_edit(request, department_id):
    department = get_object_or_404(Department, id=department_id)
    if department.company is not None and request.user.company.id == department.company.id:
        if request.method == 'POST':
            form = DepartmentForm(request.POST, instance=department)
            if form.is_valid():
                form.save()
                return redirect('department_details', department_id=department_id)
        else:
            form = DepartmentForm(instance=department)

        return render(request, 'department_edit.html', {'form': form})
    else:
         raise Http404("Department not found.")


        

@login_required
@permission_required("department.delete_department", raise_exception=True)
def department_delete(request, department_id):
    department = get_object_or_404(Department, id=department_id)
    if request.user.company.id == department.company.id:

        
        if request.method == "POST":
            department.delete()
            return redirect('department_list')
        context = {
            'department': department
        }
        return render(request, "department_delete.html", context)
    
    else:
        raise Http404("Department not found.")


    
