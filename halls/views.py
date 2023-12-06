from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# Create your views here.
def home(request):
    return render(request,'halls/home.html')

class SignUp(generic.CreateView):
    form_class=UserCreationForm
    model=User
    template_name='registration/signup.html'
    success_url=reverse_lazy('home')
