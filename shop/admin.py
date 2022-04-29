from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Brand)
admin.site.register(models.Category)

admin.site.register(models.Cloths)
admin.site.register(models.Food)
admin.site.register(models.Accessory)
