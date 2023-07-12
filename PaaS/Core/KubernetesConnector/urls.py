from django.urls import path
from . import views


urlpatterns = [
    path('GetPods/', views.get_all_pods),
    path('GetServices/', views.get_all_services),
    path('GetNodes/', views.get_all_nodes),
    path('GetNamespaces/', views.get_all_namespaces),
]