from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, DetailView, ListView
from .models import Hostname, GetInterfaces
from django.urls import reverse_lazy
from django.contrib import messages
from django.db import models
from django.core.paginator import Paginator

class Index(TemplateView):
    template_name = 'myapp/index.html'
    
class GetInterfacesList(ListView):
    model = GetInterfaces
    paginate_by = 10
    template_name = 'myapp/get_interfaces_all.html'
    
    def get_queryset(self):
        return GetInterfaces.objects.all().order_by('-updated_at')
    
        
class GetInterfacesDetail(DetailView):
    model = GetInterfaces
    template_name = 'myapp/get_interfaces_detail.html'
    
class GetInterfacesLatest(ListView):
    model = GetInterfaces
    template_name = 'myapp/get_interfaces_latest.html'
    
    def get_context_data(self, *args, **kwargs):
        get_interfaces_all = GetInterfaces.objects.all()
        # sub query set
        sub_qs = get_interfaces_all.filter(
            hostname=models.OuterRef("hostname"),
            updated_at__gt=models.OuterRef("updated_at"),
        )
        qs = get_interfaces_all.filter(~models.Exists(sub_qs)).order_by('hostname')
        params = {
            'logs_list': qs,
        }
        return params
    
class GetInterfacesHistory(DetailView):
    model = Hostname
    template_name = 'myapp/get_interfaces_history.html'
    
    def get_context_data(self, *args, **kwargs):
        hostname = Hostname.objects.get(id = self.kwargs['pk'])
        logs = GetInterfaces.objects.filter(hostname=hostname).order_by('-updated_at')
        params = {
            'hostname' : hostname,
            'logs_list': logs,
        }
        return params