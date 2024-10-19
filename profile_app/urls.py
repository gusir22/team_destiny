# pages/urls.py
from django.urls import path

from .views import (
    ProfilePageView,
)


urlpatterns = [
    path('<int:pk>/', ProfilePageView.as_view(), name='profile_page'),
]