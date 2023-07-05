#from django.db import models

# Create your models here.
from django.db import models
from company.models import Company, CustomUser
from branch.models import Branch

class Department(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=200)
    comment = models.CharField(max_length=200, null=True, blank=True)
    department_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    created_by = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True, related_name='departments_created_by')
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True, blank=True)
    branch = models.ForeignKey(Branch, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        db_table = 'department'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.name:
            # Perform some validation or data manipulation
            self.name = self.name.capitalize()
        super().save(*args, **kwargs)
