from django.db import models
from django.db.models import Q
from django.core.validators import MinValueValidator
from django.contrib.postgres.fields import ArrayField
from mptt.models import MPTTModel, TreeForeignKey
from django.shortcuts import get_object_or_404


# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Category(MPTTModel):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


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

    def __str__(self):
        return self.title


class CustomManager(models.Manager):
    def get_brand_or_category(self, brand=None, category=None):
        objects = self.all()
        if brand is not None:
            brand = Brand.objects.filter(name=brand).first()
            if brand is not None:
                objects = self.filter(brand=brand.id)
        if category is not None:
            category = Category.objects.filter(name=category).first()
            if category is not None:
                objects = self.filter(category=category.id)
        return objects.filter(quantity__gt=10)
        # return self.filter(Q(brand=brand.id) | Q(category=category.id)).filter(quantity__gt=10)


class Food(BabyProduct):
    expiration_date = models.DateField()

    objects = models.Manager()

    custom_objects = CustomManager()

    def __str__(self):
        return self.title


class Cloths(BabyProduct):
    min_size = models.IntegerField()
    max_size = models.IntegerField()

    objects = models.Manager()

    custom_objects = CustomManager()

    def __str__(self):
        return self.title


class Accessory(BabyProduct):
    colors = ArrayField(models.CharField(max_length=15))

    objects = models.Manager()

    custom_objects = CustomManager()

    class Meta:
        verbose_name_plural = 'Accessories'

    def __str__(self):
        return self.title
