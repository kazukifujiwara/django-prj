from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, DetailView, ListView
from .models import JsonData
from django.urls import reverse_lazy
from django.contrib import messages

class Index(TemplateView):
    template_name = 'myapp/index.html'
    
class JsonDataDetail(DetailView):
    model = JsonData
    
class JsonDataList(ListView):
    model = JsonData
    
    def get_queryset(self):
        return JsonData.objects.all().order_by('-updated_at')
    
class JsonDataLatest(ListView):
    model = JsonData
    template_name = 'myapp/jsondata_latest.html'
    def get_queryset(self):
        # return JsonData.objects.all().order_by('-updated_at')
        # return JsonData.objects.filter(name="Router1")
        return JsonData.objects.latest("updated_at")