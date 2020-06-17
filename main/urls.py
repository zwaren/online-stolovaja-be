from django.urls import path

from .views import DishTypeViewSet, DishViewSet, ScheduleItemViewSet, OrderViewSet

urlpatterns = [
    path('dish_types/', DishTypeViewSet.as_view({ 'get': 'list', 'post': 'create' })),
    path('dish_types/<int:pk>/', DishTypeViewSet.as_view({ 'get': 'retrieve' })),
    path('dishes/', DishViewSet.as_view({ 'get': 'list', 'post': 'create' })),
    path('dishes/<int:pk>/', DishViewSet.as_view({ 'get': 'retrieve' })),
    path('schedule_items/', ScheduleItemViewSet.as_view({ 'get': 'list', 'post': 'create' })),
    path('schedule_items/<int:pk>/', ScheduleItemViewSet.as_view({ 'get': 'retrieve' })),
    path('orders/', OrderViewSet.as_view({ 'get': 'list', 'post': 'create' })),
    path('orders/<int:pk>/', OrderViewSet.as_view({ 'get': 'retrieve' })),
]