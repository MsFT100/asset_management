from django.db import models
from company.models import Company, CustomUser

# Create your models here.
class Accessories(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price =models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='accessories/images')
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        db_table = 'accessories'

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

