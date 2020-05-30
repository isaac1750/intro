# from django.shortcuts import render
from django.db.models import Q
from django.views.generic import TemplateView, ListView, CreateView
from .models import City
from .models import Contact
from .forms import ContactForm
from django.urls import reverse_lazy

# Create your views here.from django.views.generic import TemplateView
class HomePageView(TemplateView):
    template_name="home.html"


class ContactPageView(CreateView):

	model = Contact
	form_class = ContactForm
	template_name="contact.html"
	success_url = reverse_lazy('home')


# Create your views here.

class SearchResultsView(ListView):
    model = City
    template_name = 'search_results.html'

    def get_queryset(self): # new
        query = self.request.GET.get('q')
        object_list = City.objects.filter(
            Q(name__icontains=query) | Q(state__icontains=query)
        )
        return object_list