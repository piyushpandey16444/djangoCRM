from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(string="Customer Name", max_length=255, null=True)
    phone = models.CharField(max_length=255, null=True)
    email = models.EmailField(string="Email Id", max_length=254, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    write_date = models.DateTimeField(auto_now=False, null=True)

    def __str__(self):
        return self.name

    
