from django.urls import path
from . import views


urlpatterns = [
    path('getpods/', views.get_all_pods),
    path('getpodsdetailed/', views.get_all_pods_detailed),
    path('getservices/', views.get_all_services),
    path('getnodes/', views.get_all_nodes),
    path('getgamespaces/', views.get_all_namespaces),
]