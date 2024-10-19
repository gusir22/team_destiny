# pages/urls.py
from django.urls import path

from .views import (
    ProfilePageDetailView,
    ProfilePageListView,
)


urlpatterns = [
    path('', ProfilePageListView.as_view(), name='profile_list'),
    path('<int:pk>/', ProfilePageDetailView.as_view(), name='profile_page'),
]