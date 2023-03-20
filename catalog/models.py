from django.db import models


class City(models.Model):
    city_name = models.CharField(max_length=100)

    def __str__(self):
        return self.city_name


class Provider(models.Model):
    provider_name = models.CharField(max_length=100)
    city = models.OneToOneField(City, on_delete=models.CASCADE)

    def __str__(self):
        return self.provider_name


class Product(models.Model):
    product_name = models.CharField(max_length=100)

    def __str__(self):
        return self.product_name


class Client(models.Model):
    client_name = models.CharField(max_length=100)
    product = models.ManyToManyField(Product)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, blank=True, related_name='clients')

    def __str__(self):
        return self.client_name
