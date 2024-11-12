
from django.urls import path
from .views import AccountCreateView

urlpatterns = [
    path('create/', AccountCreateView.as_view(), name='account_create'),

]
