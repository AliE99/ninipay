from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Food, Cloths, Accessory
from .serializers import FoodSerializer, ClothsSerializer, AccessorySerializer


# Create your views here.
class FoodViewSet(ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer


class ClothsViewSet(ModelViewSet):
    queryset = Cloths.objects.all()
    serializer_class = ClothsSerializer


class AccessoryViewSet(ModelViewSet):
    queryset = Accessory.objects.all()
    serializer_class = AccessorySerializer
