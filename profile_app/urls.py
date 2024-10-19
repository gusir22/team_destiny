# pages/urls.py
from django.urls import path

from .views import (
    ProfilePageDetailView,
    ProfilePageListView,
    CompanionCreateView,
)


urlpatterns = [
    path('', ProfilePageListView.as_view(), name='profile_list'),
    path('<int:pk>/add_companion/', CompanionCreateView.as_view(), name='companion_create'),
    path('<int:pk>/', ProfilePageDetailView.as_view(), name='profile_page'),
]
