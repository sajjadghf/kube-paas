from django.urls import path
from . import views


urlpatterns = [
    path('GetDataFromCluster/', views.get_data_from_cluster),
]