from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_jwt.views import obtain_jwt_token

from .views import RegistrationView, LoginView, LogoutView

urlpatterns = format_suffix_patterns([
    path('signup/', RegistrationView.as_view()),
    path('login/', LoginView.as_view({ 'post': 'create' })),
    path('logout/', LogoutView.as_view()),
])