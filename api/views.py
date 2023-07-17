# device/device_api/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from device.models import Device
from .serializers import DeviceSerializer


class DeviceListApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the device items for given requested user
        '''
        devices = Device.objects.get_queryset().order_by('id')

        serializer = DeviceSerializer(devices, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the Device with given device data
        '''
        data = {                        
            'asset_tag': request.data.get('asset_tag'),
            'model_id': request.data.get('model_id'),
            'serial_no': request.data.get('serial_no'),
            'purchase_date': request.data.get('purchase_date'),
            'asset_eol_date': request.data.get('asset_eol_date'),
            'purchase_cost': request.data.get('purchase_cost'),
            'order_number': request.data.get('order_number'),
            'assigned_to': request.data.get('assigned_to'),
            'comments': request.data.get('comments'),
            'image': request.data.get('image'),
            # 'user_id': request.data.get('user_id'),
            'physical': request.data.get('physical'),
            'status': request.data.get('status'),
            'archived': request.data.get('archived'),
            'rtd_location_id': request.data.get('rtd_location_id'),
            'warranty_months': request.data.get('warranty_months'),
            'depreciate': request.data.get('depreciate'),
            'supplier_id': request.data.get('supplier_id'),
            'last_checkout': request.data.get('last_checkout'),
            'expected_checkin': request.data.get('expected_checkin'),
            'assigned_type': request.data.get('assigned_type'),
            'last_audit_date': request.data.get('last_audit_date'),
            'next_audit_date': request.data.get('next_audit_date'),
            'byod': request.data.get('byod'),            
            "company" : request.user.company.id
        }
        print(data)
        serializer = DeviceSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeviceDetailApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, device_id, company_id):
        '''
        Helper method to get the object with given device_id, and company_id
        '''
        try:
            return Device.objects.get(id=device_id, company = company_id)
        except Device.DoesNotExist:
            return None

    # 3. Retrieve
    def get(self, request, device_id, *args, **kwargs):
        '''
        Retrieves the Device with given device_id
        '''
        device_instance = self.get_object(device_id, request.user.company.id)
        if not device_instance:
            return Response(
                {"res": "Object with device id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = DeviceSerializer(device_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 4. Update
    def put(self, request, device_id, *args, **kwargs):
        '''
        Updates the device item with given device_id if exists
        '''
        device_instance = self.get_object(device_id, request.user.id)
        if not device_instance:
            return Response(
                {"res": "Object with device id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'task': request.data.get('task'), 
            'completed': request.data.get('completed'), 
            'user': request.user.id
        }
        serializer = DeviceSerializer(instance = device_instance, data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 5. Delete
    def delete(self, request, device_id, *args, **kwargs):
        '''
        Deletes the device item with given device_id if exists
        '''
        device_instance = self.get_object(device_id, request.user.id)
        if not device_instance:
            return Response(
                {"res": "Object with device id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        device_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )
