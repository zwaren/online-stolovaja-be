import datetime

from django.contrib.auth.models import User
from rest_framework import status, viewsets
from rest_framework.response import Response

from auth_service.serializers import UserSerializer

from .models import Dish, DishType, Order, ScheduleItem
from .permissions import IsAdmin, IsCook, IsStaff, IsUser
from .serializers import (DishSerializer, DishTypeSerializer, OrderSerializer,
                          ScheduleItemSerializer)


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

    def list(self, request):
        date = self.request.query_params.get('date', None)
        if date is not None:
            date = datetime.date(*[int(i) for i in date.split('-')])
            queryset = self.get_queryset().filter(date=date)
            serializer = self.get_serializer_class()(queryset, many=True).data
            return Response(serializer)
        return Response(status=status.HTTP_400_BAD_REQUEST)

class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

    def get_permissions(self):
        permission_classes = []
        if self.action in ['list', 'retrieve']:
            permission_classes = [IsCook]
        elif self.action in ['create', 'update']:
            permission_classes = [IsStaff, IsCook]
        else:
            permission_classes = [IsAdmin]
        return [permission() for permission in permission_classes]
    
    def create(self, request):
        data = {
            'staff': User.objects.get(username=request.user.username).id, 
            'schedule_item': request.data['schedule_item']
        }
        serializer = self.get_serializer_class()(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
