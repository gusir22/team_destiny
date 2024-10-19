from django.views.generic import DetailView

from .models import (
    ProfilePage,
)

# Create your views here.
class ProfilePageView(DetailView):
    model = ProfilePage
    template_name = "profile_page.html"
    context_object_name = "profile"