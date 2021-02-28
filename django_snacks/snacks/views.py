from django.shortcuts import render
from django.views.Generated import TemplateView

class HomePageView(TemplateView):
  tempalte_name = 'home.html'

class AboutView(TemplateView):
  tempalte_name = 'about.html'



# Create your views here.
