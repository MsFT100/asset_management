import os
from django.shortcuts import render, redirect, get_object_or_404

from branch.models import Branch
from .models import Branch
from .forms import BranchForm

from django.core.paginator import Paginator
from django.core.files.storage import default_storage
from django.contrib.auth.decorators import login_required, permission_required
from django.http import Http404
from django.conf import settings


@login_required
@permission_required("branch.add_branch", raise_exception=True)
def branch_create(request):
    if request.method == 'POST':
        form = BranchForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.company = request.user.company
            obj.save()
            # TODO :CORRECT THIS
            return redirect('branch_list')

    else:
        form = BranchForm()
    return render(request, 'branch_create.html', {"form": form})


@login_required
@permission_required("branch.view_branch", raise_exception=True)
def branch_list(request):
    # branch_list = Branch.objects.get_queryset().order_by('id')
    branch_list = Branch.objects.filter(company=request.user.company).order_by('id')

    # Configure the number of items per page
    items_per_page = 5
    paginator = Paginator(branch_list, items_per_page)

    # Get the current page number from the request's GET parameters
    page_number = request.GET.get('page')

    # Retrieve the page object for the requested page number
    branch_list = paginator.get_page(page_number)

    context = {
        'branch_list': branch_list,
    }
    return render(request, 'branch_list.html', context)


@login_required
@permission_required("branch.change_branch", raise_exception=True)
def branch_edit(request, branch_id):
    branch = get_object_or_404(Branch, id=branch_id)
    if request.user.company.id == branch.company.id:
        if request.method == 'POST':        
                form = BranchForm(request.POST, instance=branch)
                if form.is_valid():                    
                    form.save()
                    return redirect('branch_details', branch_id=branch_id)
        else:        
            # branch = get_object_or_404(Branch, id=branch_id)
            form = BranchForm(instance=branch)

        return render(request, 'branch_edit.html', {'form': form})

    else:
        raise Http404("Branch not found.")


@login_required
@permission_required("branch.view_branch", raise_exception=True)
def branch_details(request, branch_id):
    branch = get_object_or_404(Branch, id=branch_id)
    if request.user.company.id == branch.company.id:
        return render(request, 'branch_details.html', {'branch': branch})
    else:
        raise Http404("Branch not found.")
    
@login_required
@permission_required("branch.delete_branch", raise_exception=True)
def branch_delete(request, branch_id):
    branch = get_object_or_404(Branch, id=branch_id)
    if request.user.company.id == branch.company.id:

        if request.method == "POST":
            branch.delete()
            return redirect('branch_list')
        context = {
            'branch': branch
        }
        return render(request, "branch_delete.html", context)
    
    else:
        raise Http404("Branch not found.")

