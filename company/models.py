from django.db import models

# Create your models here.


class Company(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "company"

    def __str__(self):
        return self.name
