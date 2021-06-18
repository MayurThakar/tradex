from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=25)
    weight = models.IntegerField()
    price = models.IntegerField()
    created_at = models.DateField()
    updated_at = models.DateField()

    class Meta:
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name
