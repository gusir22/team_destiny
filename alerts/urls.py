# alerts/urls.py
from django.urls import path

from .views import (
    AlertDetailView,
    AlertCreateView,
    AlertUpdateCreateView,
)


urlpatterns = [
    path('create/', AlertCreateView.as_view(), name='alert_create'),
    path('<int:pk>/create_update/', AlertUpdateCreateView.as_view(), name='alert_update_create'),
    path('<int:pk>/', AlertDetailView.as_view(), name='alert_detail'),
]