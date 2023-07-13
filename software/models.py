from django.db import models
from company.models import Company, CustomUser
from employee.models import Employee

# Create your models here
class Software(models.Model):
    id = models.AutoField(primary_key=True)
    license_key = models.CharField(max_length=191, null=True)
    license_name =  models.CharField(max_length=120,blank=True, null=True)
    license_email =  models.CharField(max_length=120, blank=True, null=True)
    license_allocated = models.IntegerField(blank=True, null=True)
    license_type = models.CharField(max_length=120)

    purchase_date = models.DateField(blank=True, null=True)
    purchase_order =  models.CharField(max_length=191, blank=True, null=True)
    seats =  models.IntegerField(null= False)
    expiration_date = models.DateTimeField(blank=True, null=True)

    order_number = models.CharField(max_length=191, blank=True, null=True)
    purchase_cost = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)

    # TODO
    supplier_id = models.IntegerField(blank=True, null=True)


    comments = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True, blank=True)


    class Meta:
        db_table = 'software'

    def __str__(self):
        return self.license_name


    # def save(self, *args, **kwargs):
    #     if self.serial_no:
    #         # Perform some validation or data manipulation
    #         self.serial_no = self.serial_no.capitalize()
    #     super().save(*args, **kwargs)