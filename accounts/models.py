from django.db import models


class Customer(models.Model):
    name = models.CharField("Customer Name", max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField("Email Id", max_length=254, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    write_date = models.DateTimeField(auto_now=False, null=True, blank=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(
        "Customer Name", max_length=255, null=True, blank=True)
    
    def __str__(self):
        return self.name


class Product(models.Model):
    CATEGORY = (
        ('indoor', 'Indoor'),
        ('outdoor', 'Outdoor')
    )
    name = models.CharField(max_length=255, null=True, blank=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=250, null=True, choices=CATEGORY)
    description = models.CharField(max_length=250, null=True)
    date_created = models.DateTimeField(
        auto_now_add=True, null=True, blank=True)
    write_date = models.DateTimeField(auto_now=False, null=True, blank=True)
    tag_ids = models.ManyToManyField("accounts.Tag", verbose_name=("Tag Ids"))

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS = (
        ('pending', 'Pending'),
        ('out_for_delivery', 'Out for delivery'),
        ('delivered', 'Delivered')
    )
    customer = models.ForeignKey("accounts.Customer", verbose_name=("Customer"), on_delete=models.SET_NULL, null=True, blank=True)
    product = models.ForeignKey("accounts.Product", verbose_name=("Product"), on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(max_length=250, choices=STATUS, null=True, blank=True)
    date_created = models.DateTimeField(
        auto_now_add=True, null=True, blank=True)
    write_date = models.DateTimeField(auto_now=False, null=True, blank=True)
