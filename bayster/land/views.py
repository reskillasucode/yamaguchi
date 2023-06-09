from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from .forms import LandReviewForm
from .models import Land, LandReview

# Create your views here.

class LandListView(ListView):
    model = Land
    template_name = 'land/land_list.html'
    context_object_name = 'land_list'
    ordering = ['-applied_date']  # 申請日の降順でソート

class LandReviewView(CreateView):
    form_class = LandReviewForm
    model = LandReview
    template_name = 'land/land_review.html'
    success_url = reverse_lazy('land-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['land'] = Land.objects.get(pk=self.kwargs['land_id'])
        return context

class LandCreateView(CreateView):
    model = Land
    template_name = 'land/land_create.html'
    fields= ('title', 'address', 'size', 'purchase_price', 'estimated_profit', 'cost', 'project_background')
    success_url = reverse_lazy('land-list')