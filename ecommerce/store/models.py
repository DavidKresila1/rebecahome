from django.db import models

class Category(models.Model):

    class Meta:
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=200, blank=False)

    def __str__(self):
        return self.name

    


class Product(models.Model):
    name = models.CharField(max_length=200, blank=False)
    price = models.FloatField(default=0, blank=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,)
    stock = models.IntegerField(default=0, blank=False)
    description = models.TextField(max_length=600, blank=False)
    image = models.ImageField(null=True)


    def __str__(self):
        return self.name


class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.IntegerField()
    email = models.EmailField()
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.first_name + " " + self.last_name