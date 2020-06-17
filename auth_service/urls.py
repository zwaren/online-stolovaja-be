from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_jwt.views import obtain_jwt_token

from . import views

urlpatterns = format_suffix_patterns([
    path('signup/', views.Registration.as_view()),
    path('login/', obtain_jwt_token),
])