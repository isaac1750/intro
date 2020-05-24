from django.conf.urls import re_path

from django.urls import path, include
from . import views

# wait i will see



urlpatterns = [
    path('', views.HomePageView.as_view(), name = 'home'),
    ]