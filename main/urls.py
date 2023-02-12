from django.urls import path
from django.views.decorators.cache import cache_page

from . import views

urlpatterns = [
  path('home/',
         views.MainView.as_view(),
         name='student_registration'),    
  path('signup/', views.SignupPageView.as_view(), name='signup'),
]