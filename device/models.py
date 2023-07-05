from django.db import models
from company.models import Company, CustomUser
from employee.models import Employee

# Create your models here
class Device(models.Model):
    id = models.AutoField(primary_key=True)
    asset_tag = models.CharField(max_length=255, blank=True, null=True)
    # TODO - make model type entity
    model_id = models.IntegerField(null=True)
    serial_no = models.CharField(max_length=191, null=True)
    purchase_date = models.DateField(blank=True, null=True)
    asset_eol_date = models.DateField(blank=True, null=True)
    purchase_cost = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    order_number = models.CharField(max_length=191, blank=True, null=True)
    
    assigned_to = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True)

    comments = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='uploads/devices/',blank=True, null=True)
    physical = models.BooleanField(default=True)
    status = models.IntegerField(blank=True, null=True)
    archived = models.BooleanField(default=False)
    rtd_location_id = models.IntegerField(blank=True, null=True)
    warranty_months = models.IntegerField(blank=True, null=True)
    depreciate = models.BooleanField(blank=True, null=True)
    # Todo - make supplier entity
    supplier_id = models.IntegerField(blank=True, null=True)
    last_checkout = models.DateTimeField(blank=True, null=True)
    expected_checkin = models.DateField(blank=True, null=True)
    assigned_type = models.CharField(max_length=191, blank=True, null=True)
    last_audit_date = models.DateTimeField(blank=True, null=True)
    next_audit_date = models.DateField(blank=True, null=True)
    byod = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        db_table = 'device'

    def __str__(self):
        return self.serial_no

    def get_logo_display(self):
        # Example method to generate an HTML <img> tag for the logo URL
        if self.logo:
            return f'<img src="{self.image}" alt="{self.serial_no} Logo">'
        else:
            return ''


    def save(self, *args, **kwargs):
        if self.id:
            existing_company = Device.objects.get(pk=self.pk)
            if existing_company.image != self.image:
                existing_company.image.delete(save=False)

        if self.serial_no:
            # Perform some validation or data manipulation
            self.serial_no = self.serial_no.capitalize()
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.image.delete(save=False)
        super().delete(*args, **kwargs)