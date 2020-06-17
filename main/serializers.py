from rest_framework import serializers

from .models import DishType, Dish, ScheduleItem, Order

class DishTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DishType
        fields = '__all__'


class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = '__all__'


class ScheduleItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScheduleItem
        fields = "__all__"

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"

