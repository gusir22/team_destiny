from django.views.generic import DetailView, ListView

from .models import Alert

# Create your views here.
class AlertDetailView(DetailView):
    model = Alert
    context_object_name = "alert"
    template_name = "alert_detail.html"
