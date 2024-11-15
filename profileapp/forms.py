from django.forms import ModelForm
from .models import *

class ProfileCreationForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['image','nickname', 'message']