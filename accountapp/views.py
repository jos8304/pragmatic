from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm



# Create your views here.
class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:login')    
    template_name = 'accountapp/create.html'





