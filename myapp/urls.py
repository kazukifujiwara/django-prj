from django.urls import path, include
from . import views

app_name = 'myapp'

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('get_interfaces_all', views.GetInterfacesList.as_view(), name='get_interfaces_all'),
    path('get_interfaces_detail/<int:pk>', views.GetInterfacesDetail.as_view(), name='get_interfaces_detail'),
    path('get_interfaces_latest', views.GetInterfacesLatest.as_view(), name='get_interfaces_latest'),
    path('get_interfaces_history/<int:pk>', views.GetInterfacesHistory.as_view(), name='get_interfaces_history'),
]
