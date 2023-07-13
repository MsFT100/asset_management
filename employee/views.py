import os
from django.shortcuts import render, redirect, get_object_or_404

from .models import Employee
from .forms import EmployeeForm

from django.core.paginator import Paginator
from django.core.files.storage import default_storage
from django.contrib.auth.decorators import login_required, permission_required
from django.http import Http404
from django.conf import settings
from django.contrib import messages


@login_required
@permission_required("employee.add_employee", raise_exception=True)
def employee_create(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.company = request.user.company
            obj.save()
            messages.success(request, 'Employee saved successfully.')
            # TODO :CORRECT THIS
            return redirect('employee_list')
        else:            
            messages.error(request, 'Error occurred while saving the employee.')

    else:
        form = EmployeeForm()
    return render(request, 'employee_create.html', {"form": form})


@login_required
@permission_required("employee.view_employee", raise_exception=True)
def employee_list(request):
    # employee_list = employee.objects.get_queryset().order_by('id')
    employee_list = Employee.objects.filter(company=request.user.company).order_by('id')

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
    employee = get_object_or_404(Employee, id=employee_id)
    if request.user.company.id == employee.company.id:
        if request.method == 'POST':  
                form = EmployeeForm(request.POST, instance=employee)
                if form.is_valid():                   
                    form.save()
                    messages.success(request, 'Employee updated successfully.')
                    return redirect('employee_list')
                else:
                    messages.error(request, 'Error occurred while updating the employee.')
        else:        
            # employee = get_object_or_404(employee, id=employee_id)
            form = EmployeeForm(instance=employee)

        return render(request, 'employee_edit.html', {'form': form})

    else:
        raise Http404("Employee not found.")


@login_required
@permission_required("employee.view_employee", raise_exception=True)
def employee_details(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)
    if request.user.company.id == employee.company.id:
        return render(request, 'employee_details.html', {'employee': employee})
    else:
        raise Http404("Employee not found.")
    
    
@login_required
@permission_required("employee.delete_employee", raise_exception=True)
def employee_delete(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)
    if request.user.company.id == employee.company.id:

        
        if request.method == "POST":
            employee.delete()
            return redirect('employee_list')
        context = {
            'employee': employee
        }
        return render(request, "employee_delete.html", context)
    
    else:
        raise Http404("Employee not found.")

    


