import os
from django.shortcuts import render, redirect, get_object_or_404

from employee.models import employee
from .models import employee
from .forms import employeeForm

from django.core.paginator import Paginator
from django.core.files.storage import default_storage
from django.contrib.auth.decorators import login_required, permission_required
from django.http import Http404
from django.conf import settings


@login_required
@permission_required("employee.add_employee", raise_exception=True)
def employee_create(request):
    if request.method == 'POST':
        form = employeeForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.company = request.user.company
            obj.save()
            # TODO :CORRECT THIS
            return redirect('employee_list')

    else:
        form = employeeForm()
    return render(request, 'employee_create.html', {"form": form})


@login_required
@permission_required("employee.view_employee", raise_exception=True)
def employee_list(request):
    # employee_list = employee.objects.get_queryset().order_by('id')
    employee_list = employee.objects.filter(company=request.user.company).order_by('id')

    # Configure the number of items per page
    items_per_page = 5
    paginator = Paginator(employee_list, items_per_page)

    # Get the current page number from the request's GET parameters
    page_number = request.GET.get('page')

    # Retrieve the page object for the requested page number
    employee_list = paginator.get_page(page_number)

    context = {
        'employee_list': employee_list,
    }
    return render(request, 'employee_list.html', context)


@login_required
@permission_required("employee.change_employee", raise_exception=True)
def employee_edit(request, employee_id):
    employee = get_object_or_404(employee, id=employee_id)
    if request.user.company.id == employee.company.id:
        if request.method == 'POST':  
                form = employeeForm(request.POST, instance=employee)
                if form.is_valid():                   
                    form.save()
                    return redirect('employee_details', employee_id=employee_id)
        else:        
            # employee = get_object_or_404(employee, id=employee_id)
            form = employeeForm(instance=employee)

        return render(request, 'employee_edit.html', {'form': form})

    else:
        raise Http404("employee not found.")


@login_required
@permission_required("employee.view_employee", raise_exception=True)
def employee_details(request, employee_id):
    employee = get_object_or_404(employee, id=employee_id)
    if request.user.company.id == employee.company.id:
        return render(request, 'employee_details.html', {'employee': employee})
    else:
        raise Http404("employee not found.")

