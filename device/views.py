import os
from django.shortcuts import render, redirect, get_object_or_404

from device.models import Device
from .models import Device
from .forms import DeviceForm

from django.core.paginator import Paginator
from django.core.files.storage import default_storage
from django.contrib.auth.decorators import login_required, permission_required
from django.http import Http404
from django.conf import settings


@login_required
@permission_required("device.add_device", raise_exception=True)
def device_create(request):
    if request.method == 'POST':
        form = DeviceForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.company = request.user.company
            obj.save()
            # TODO :CORRECT THIS
            return redirect('device_list')

    else:
        form = DeviceForm()
    return render(request, 'device_create.html', {"form": form})


@login_required
@permission_required("device.view_device", raise_exception=True)
def device_list(request):
    # device_list = Device.objects.get_queryset().order_by('id')
    device_list = Device.objects.filter(company=request.user.company).order_by('id')

    # Configure the number of items per page
    items_per_page = 5
    paginator = Paginator(device_list, items_per_page)

    # Get the current page number from the request's GET parameters
    page_number = request.GET.get('page')

    # Retrieve the page object for the requested page number
    device_list = paginator.get_page(page_number)

    context = {
        'device_list': device_list,
    }
    return render(request, 'device_list.html', context)


@login_required
@permission_required("device.change_device", raise_exception=True)
def device_edit(request, device_id):
    device = get_object_or_404(Device, id=device_id)
    if request.user.company.id == device.company.id:
        if request.method == 'POST':        
                form = DeviceForm(request.POST, request.FILES, instance=device)
                if form.is_valid():                    
                    form.save()
                    return redirect('device_details', device_id=device_id)
        else:        
            # device = get_object_or_404(Device, id=device_id)
            form = DeviceForm(instance=device)

        return render(request, 'device_edit.html', {'form': form})

    else:
        raise Http404("Device not found.")


@login_required
@permission_required("device.view_device", raise_exception=True)
def device_details(request, device_id):
    device = get_object_or_404(Device, id=device_id)
    if request.user.company.id == device.company.id:
        return render(request, 'device_details.html', {'device': device})
    else:
        raise Http404("Device not found.")
    
@login_required
@permission_required("device.delete_device", raise_exception=True)
def device_delete(request, device_id):
    device = get_object_or_404(Device, id=device_id)
    if request.user.company.id == device.company.id:

        
        if request.method == "POST":
            device.delete()
            return redirect('device_list')
        context = {
            'device': device
        }
        return render(request, "device_delete.html", context)
    
    else:
        raise Http404("Device not found.")



