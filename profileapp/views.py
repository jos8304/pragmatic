from .models import Profile
from .forms import ProfileCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy


# Create your views here.
class ProfileCreateView(CreateView):
    model = Profile
    context_oject_name = 'targer_profile'    
    form_class = ProfileCreationForm
    succes_url = reverse_lazy('accountapp:login')
    template_name = 'profileapp/create.html'

    def form_valid(self, form):
        temp_profile = form.save(commit=False)
        temp_profile.user = self.request.user
        temp_profile.save()
        return super().form_valid(form)

