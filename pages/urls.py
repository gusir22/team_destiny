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
]