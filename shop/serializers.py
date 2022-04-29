from rest_framework import serializers
from . import models


class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Food
        fields = '__all__'


class ClothsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Cloths
        fields = '__all__'


class AccessorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Accessory
        fields = '__all__'
