# pages/views.py
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'home.html'


class SignupView(TemplateView):
    template_name = 'signup.html'
    
class LoginView(TemplateView):
    template_name = 'login.html'

class ProfileView(TemplateView):
    template_name = 'profile.html'
