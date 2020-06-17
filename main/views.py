from rest_framework import viewsets
from rest_framework.response import Response

from .models import DishType, Dish, ScheduleItem, Order
from .serializers import DishTypeSerializer, DishSerializer, ScheduleItemSerializer, OrderSerializer
from .permissions import IsUser, IsStaff, IsCook, IsAdmin

class DishTypeViewSet(viewsets.ModelViewSet):
    serializer_class = DishTypeSerializer
    queryset = DishType.objects.all()

    def get_permissions(self):
        permission_classes = []
        if self.action in ['list', 'retrieve']:
            permission_classes = [IsUser]
        else:
            permission_classes = [IsAdmin]
        return [permission() for permission in permission_classes]


class DishViewSet(viewsets.ModelViewSet):
    serializer_class = DishSerializer
    queryset = Dish.objects.all()

    def get_permissions(self):
        permission_classes = []
        if self.action in ['list', 'retrieve']:
            permission_classes = [IsUser]
        elif self.action in ['create', 'update']:
            permission_classes = [IsCook]
        else:
            permission_classes = [IsAdmin]
        return [permission() for permission in permission_classes]


class ScheduleItemViewSet(viewsets.ModelViewSet):
    serializer_class = ScheduleItemSerializer
    queryset = ScheduleItem.objects.all()

    def get_permissions(self):
        permission_classes = []
        if self.action in ['list', 'retrieve']:
            permission_classes = [IsUser]
        elif self.action in ['create', 'update']:
            permission_classes = [IsCook]
        else:
            permission_classes = [IsAdmin]
        return [permission() for permission in permission_classes]


class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

    def get_permissions(self):
        permission_classes = []
        if self.action in ['list', 'retrieve']:
            permission_classes = [IsCook]
        elif self.action in ['create', 'update']:
            permission_classes = [IsStaff]
        else:
            permission_classes = [IsAdmin]
        return [permission() for permission in permission_classes]
