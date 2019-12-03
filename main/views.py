from django.http import HttpResponse
from django.shortcuts import render
from .models import Tutorial
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def homepage(request):
    return render(request = request,
                  template_name='main/home.html',
                  context = {"tutorials":Tutorial.objects.all})

def register(request):
    form = UserCreationForm
    return render(request = request,
                  template_name = "main/register.html",
                  context={"form":form})
