from .models import LandModel
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy

# Create your views here.
class LandListView(ListView):
    model = LandModel
    template_name = "land_list.html"
    context_object_name = 'lands'
    
class LandDetailView(DetailView):
    model = LandModel
    template_name = "land_detail.html"
    context_object_name = 'land'
    
class LandCreateView(CreateView):
    model = LandModel
    template_name = "land_create.html"
    fields = ["address", "size", "purchase_price", "estimated_profit", "cost", "project_background", "applied_date", "status"]
    success_url = reverse_lazy("list")

