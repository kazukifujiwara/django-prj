from django.urls import path, include
from . import views

app_name = 'myapp'

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('jsondata_detail/<int:pk>', views.JsonDataDetail.as_view(), name='jsondata_detail'),
    path('jsondata_list', views.JsonDataList.as_view(), name='jsondata_list'),
    path('jsondata_latest', views.JsonDataLatest.as_view(), name='jsondata_latest'),
]
