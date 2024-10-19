# alerts/urls.py
from django.urls import path

from .views import (
    AlertDetailView,
)


urlpatterns = [
    path('<int:pk>/', AlertDetailView.as_view(), name='alert_detail'),
]