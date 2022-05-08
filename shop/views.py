from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
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

    @action(detail=False, methods=['GET'])
    def brand(self, request):
        brand = request.query_params['search']
        queryset = Accessory.objects.filter(brand=brand).all()
        print(queryset)
        serializer = AccessorySerializer(queryset, many=True)
        return HttpResponse(serializer.data)
