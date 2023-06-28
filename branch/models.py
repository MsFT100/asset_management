from django.db import models
from company.models import Company, CustomUser

# Create your models here.
class Branch(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=200)
    location = models.CharField(blank=True, null=True, max_length=255)
    branch_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        db_table = 'branch'

    def __str__(self):
        return self.name

    def get_full_address(self):
        # Example method to retrieve the full address of the company
        if self.location:
            return f"{self.location}, {self.name}"
        else:
            return self.name

    def is_active(self):
        # Example method to check if the company has a domain
        return bool(self.is_active)

    def save(self, *args, **kwargs):
        if self.name:
            # Perform some validation or data manipulation
            self.name = self.name.capitalize()
        super().save(*args, **kwargs)

