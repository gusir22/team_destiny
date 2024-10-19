# pages/views.py
from typing import Any
from django.views.generic import TemplateView
from django.views.generic import DetailView, ListView

from alerts.models import Alert


class HomePageView(ListView):
    model = Alert
    context_object_name = "alerts"
    template_name = 'home.html'
    
    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        return context


class SignupView(TemplateView):
    template_name = 'signup.html'
    
class LoginView(TemplateView):
    template_name = 'login.html'

class ProfileView(TemplateView):
    template_name = 'profile.html'
