import os
from django.shortcuts import render, redirect, get_object_or_404

from .models import Accessories
from .forms import AccessoriesForm

from django.core.paginator import Paginator
from django.core.files.storage import default_storage
from django.contrib.auth.decorators import login_required, permission_required
from django.http import Http404
from django.conf import settings
from django.contrib import messages


@login_required
@permission_required("accessories.add_accessories", raise_exception=True)
def accessories_create(request):
    if request.method == 'POST':
        form = AccessoriesForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.company = request.user.company
            obj.save()
            messages.success(request, 'Accessories saved successfully.')
            # TODO :CORRECT THIS
            return redirect('accessories_list')
        else:            
            messages.error(request, 'Error occurred while saving the accessories.')

    else:
        form = AccessoriesForm()
    return render(request, 'accessories_create.html', {"form": form})


@login_required
@permission_required("accessories.view_accessories", raise_exception=True)
def accessories_list(request):
    # accessories_list = accessories.objects.get_queryset().order_by('id')
    accessories_list = Accessories.objects.filter(company=request.user.company).order_by('id')

    # Configure the number of items per page
    items_per_page = 5
    paginator = Paginator(accessories_list, items_per_page)

    # Get the current page number from the request's GET parameters
    page_number = request.GET.get('page')

    # Retrieve the page object for the requested page number
    accessories_list = paginator.get_page(page_number)

    context = {
        'accessories_list': accessories_list,
    }
    return render(request, 'accessories_list.html', context)


@login_required
@permission_required("accessories.change_accessories", raise_exception=True)
def accessories_edit(request, accessories_id):
    accessories = get_object_or_404(Accessories, id=accessories_id)
    if request.user.company.id == accessories.company.id:
        if request.method == 'POST':  
                form = AccessoriesForm(request.POST, instance=accessories)
                if form.is_valid():                   
                    form.save()
                    messages.success(request, 'Accessories updated successfully.')
                    return redirect('accessories_list')
                else:
                    messages.error(request, 'Error occurred while updating the accessories.')
        else:        
            # accessories = get_object_or_404(accessories, id=accessories_id)
            form = AccessoriesForm(instance=accessories)

        return render(request, 'accessories_edit.html', {'form': form})

    else:
        raise Http404("Accessories not found.")


@login_required
@permission_required("accessories.view_accessories", raise_exception=True)
def accessories_details(request, accessories_id):
    accessories = get_object_or_404(Accessories, id=accessories_id)
    if request.user.company.id == accessories.company.id:
        return render(request, 'accessories_details.html', {'accessories': accessories})
    else:
        raise Http404("Accessories not found.")
    
    
@login_required
@permission_required("accessories.delete_accessories", raise_exception=True)
def accessories_delete(request, accessories_id):
    accessories = get_object_or_404(Accessories, id=accessories_id)
    if request.user.company.id == accessories.company.id:
        if request.method == "POST":
            accessories.delete()
            return redirect('accessories_list')
        context = {
            'accessories': accessories
        }
        return render(request, "accessories_delete.html", context)
    
    else:
        raise Http404("Accessories not found.")

