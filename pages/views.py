from django.shortcuts import render

from django.views.generic import TemplateView

# Create your views here.from django.views.generic import TemplateView
class HomePageView(TemplateView):
    template_name="home.html"
# Create your views here.
