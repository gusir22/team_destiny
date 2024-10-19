# pages/urls.py
from django.urls import path

from .views import (
    HomePageView,
    SignupView,
    LoginView,
    ProfileView,
)


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('/signup/', SignupView.as_view(), name='signup'),
    path('/login/', LoginView.as_view(), name='login'),
    path('/profile/', ProfileView.as_view(), name='profile'),
]