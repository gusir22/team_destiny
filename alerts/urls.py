# alerts/urls.py
from django.urls import path

from .views import (
    AlertDetailView,
    AlertCreateView,
    AlertUpdateCreateView,
    AlertUpdateView,
)


urlpatterns = [
    path('create/', AlertCreateView.as_view(), name='alert_create'),
    path('<int:pk>/alert_edit/', AlertUpdateView.as_view(), name='alert_edit'),
    path('<int:pk>/create_update/', AlertUpdateCreateView.as_view(), name='alert_update_create'),
    path('<int:pk>/', AlertDetailView.as_view(), name='alert_detail'),
]