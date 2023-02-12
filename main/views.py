from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView, CreateView  # new
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy
# Create your views here.

class MainView(TemplateView):
  #The template View displays our template
  template_name = 'main/base.html' 
  
class SignupPageView(CreateView):
  form_class = CustomUserCreationForm
  success_url = reverse_lazy('login')
  template_name = 'signup.html' 


  
  
