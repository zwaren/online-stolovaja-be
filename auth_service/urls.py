from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_jwt.views import obtain_jwt_token

from .views import UserView, LoginView, LogoutView

urlpatterns = format_suffix_patterns([
    path('signup/', UserView.as_view({ 'post': 'create' })),
    path('profile/', UserView.as_view({ 'get': 'retrieve' })),
    path('login/', LoginView.as_view({ 'post': 'create' })),
    path('logout/', LogoutView.as_view()),
])