from django.views.generic import (
    DetailView, 
    ListView, 
    CreateView, 
    UpdateView, 
    DeleteView,
)
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404

from .models import (
    ProfilePage,
    Companion,
)

from .forms import (
    CompanionCreateForm,
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
    

class CompanionCreateView(CreateView):
    model = Companion
    template_name = 'companion_create.html'
    form_class = CompanionCreateForm
    
    def form_valid(self, form):
        # needed to pass alert object to context
        # Save the Companion instance but don't commit to the database yet
        companion = form.save(commit=False)
        
        # Get the ProfilePage object using the pk from the URL
        profile = get_object_or_404(ProfilePage, id=self.kwargs['pk'])
        
        # Save the Companion instance to the database
        companion.save()
        
        # Add the companion to the profile's companion list
        profile.companion_list.add(companion)
        return super().form_valid(form)

    def get_success_url(self):
        # Get the ProfilePage object using the pk from the URL
        profile = get_object_or_404(ProfilePage, id=self.kwargs['pk'])
        return reverse_lazy('profile_page', kwargs={'pk': profile.id})
    