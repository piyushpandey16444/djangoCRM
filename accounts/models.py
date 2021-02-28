from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField("Customer Name", max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField("Email Id", max_length=254, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    write_date = models.DateTimeField(auto_now=False, null=True, blank=True)

    def __str__(self):
        return self.name
