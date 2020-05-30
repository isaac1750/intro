from django.conf.urls import re_path
from .views import HomePageView, SearchResultsView, ContactPageView
from django.urls import path
from . import views

# wait i will see



urlpatterns = [
    path('', views.HomePageView.as_view(), name = 'home'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('contact/', ContactPageView.as_view(), name='contact'),

    ]