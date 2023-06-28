import os
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    company = models.ForeignKey(
        'Company', on_delete=models.SET_NULL, null=True, blank=True)

    # Add any additional fields or methods as needed

    class Meta:
        db_table = 'auth_user'  # Specify the database table name for the user model


class Company(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=200)
    domain = models.CharField(blank=True, null=True, max_length=255)
    email = models.EmailField(max_length=250)
    logo = models.ImageField(upload_to='uploads/')
    location = models.CharField(blank=True, null=True, max_length=255)
    company_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    created_by = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True, related_name='created_by')

    class Meta:
        db_table = 'company'

    def __str__(self):
        return self.name

    def get_full_address(self):
        # Example method to retrieve the full address of the company
        if self.location:
            return f"{self.location}, {self.name}"
        else:
            return self.name

    def get_logo_display(self):
        # Example method to generate an HTML <img> tag for the logo URL
        if self.logo:
            return f'<img src="{self.logo}" alt="{self.name} Logo">'
        else:
            return ''

    def has_domain(self):
        # Example method to check if the company has a domain
        return bool(self.domain)

    def save(self, *args, **kwargs):
        if self.id:
            existing_company = Company.objects.get(pk=self.pk)
            if existing_company.logo != self.logo:
                existing_company.logo.delete(save=False)

        if self.location:
            # Perform some validation or data manipulation
            self.location = self.location.capitalize()
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.logo.delete(save=False)
        super().delete(*args, **kwargs)

