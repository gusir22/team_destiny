from django.views.generic import DetailView, ListView

from .models import (
    ProfilePage,
)

# Create your views here.
class ProfilePageListView(ListView):
    model = ProfilePage
    template_name = "profiles_list.html"
    context_object_name = "profiles"


class ProfilePageDetailView(DetailView):
    model = ProfilePage
    template_name = "profile_page.html"
    context_object_name = "profile"