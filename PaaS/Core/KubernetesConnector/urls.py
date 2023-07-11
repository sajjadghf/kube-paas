from django.urls import path
from . import views


urlpatterns = [
    path('GetPods/', views.get_data_from_cluster),
]