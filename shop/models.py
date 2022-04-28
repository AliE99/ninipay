from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.postgres.fields import ArrayField
from mptt.models import MPTTModel, TreeForeignKey


# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=255)


class Category(MPTTModel):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['name']


class BabyProduct(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField(null=True, blank=True)
    unit_price = models.DecimalField(max_digits=6,
                                     decimal_places=2,
                                     validators=[MinValueValidator(1)])
    last_update = models.DateTimeField(auto_now=True)
    quantity = models.IntegerField(validators=[MinValueValidator(0)])
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='products')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')


class Food(BabyProduct):
    expiration_date = models.DateField()


class Cloths(BabyProduct):
    min_size = models.IntegerField()
    max_size = models.IntegerField()


class Accessory(BabyProduct):
    colors = ArrayField(models.CharField(max_length=15))
