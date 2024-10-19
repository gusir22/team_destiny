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
    Alert,
    AlertUpdate,
)
from .forms import (
    AlertCreateForm,
    AlertUpdateCreateForm,
)

# Create your views here.
class AlertDetailView(DetailView):
    model = Alert
    context_object_name = "alert"
    template_name = "alert_detail.html"
    

class AlertCreateView(CreateView):
    model = Alert
    template_name = 'alert_create.html'
    form_class = AlertCreateForm
    
    def form_valid(self, form):
        form.instance.author = self.request.user  # Set the author as the logged-in user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('alert_detail', kwargs={'pk': self.object.pk})
    
    
class AlertUpdateView(UpdateView):
    model = Alert
    template_name = 'alert_create.html'
    form_class = AlertCreateForm
    
    def get_success_url(self):
        return reverse_lazy('alert_detail', kwargs={'pk': self.object.pk})
    
    
class AlertUpdateCreateView(CreateView):
    model = AlertUpdate
    template_name = 'alert_update_create.html'
    form_class = AlertUpdateCreateForm
    
    def form_valid(self, form):
        # needed to pass alert object to context
        alert = get_object_or_404(Alert, id=self.kwargs['pk'])
        alert.save()  # saves parent instance to update modified date value
        form.instance.alert = alert
        
        form.instance.author = self.request.user  # Set the author as the logged-in user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('alert_detail', kwargs={'pk': self.object.alert.pk})
