from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)  # in cents is preferred

    def __str__(self):
        return self.name

