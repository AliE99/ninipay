from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Food, Cloths, Accessory
from .serializers import FoodSerializer, ClothsSerializer, AccessorySerializer


# Create your views here.
class FoodViewSet(ModelViewSet):
    queryset = Food.custom_objects.get_brand_or_category(brand='Maz Maz')
    # queryset = Food.custom_objects.get_foods(brand='Zara')
    serializer_class = FoodSerializer


class ClothsViewSet(ModelViewSet):
    queryset = Cloths.custom_objects.get_brand_or_category(brand='Zara', category='hat')
    serializer_class = ClothsSerializer


class AccessoryViewSet(ModelViewSet):
    queryset = Accessory.objects.all()
    serializer_class = AccessorySerializer
