from django.db import models
from django.utils.html import mark_safe


# Create your models here.
class User(models.Model):
    Genre = [
        ("Masculin", 'M'),
        ("Féminin", 'F'),
    ]
    gender = models.CharField(max_length=20, choices=Genre)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birthday_date = models.DateField()
    mail_address = models.EmailField(max_length=150)
    address = models.CharField(max_length=150)
    post_code = models.IntegerField()
    city = models.CharField(max_length=50)

    def __str__(self):
        return str(str(self.first_name) + " " + str(self.last_name))


class Products(models.Model):
    type_products = [
        ("Fruits", 'Fruits'),
        ("Légumes", 'Légumes'),
    ]

    measure_unit = [
        ("Kilo", 'Kg'),
        ("Gramme", 'Gr'),
        ("Pièces", 'Pièce'),

    ]
    type = models.CharField(max_length=20, choices=type_products)
    name = models.CharField(max_length=30)
    image_preview = models.ImageField(null=True, blank=True, upload_to="staticfiles/img/")
    unit_of_measure = models.CharField(max_length=20, choices=measure_unit)
    number_in_lot = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=4, decimal_places=2)

    @property
    def thumbnail_preview(self):
        if self.image_preview:
            return mark_safe('<img src="{}" width="300" height="300" />'.format(self.image_preview.url))
        return ""

    def __str__(self):
        return self.name

class Carts(models.Model):
    pass