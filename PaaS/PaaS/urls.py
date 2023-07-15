from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/kubernetes/', include('Core.KubernetesConnector.urls')),
    path('api/v1/kubernetes/deployments/', include('Core.DeploymentHandler.urls')),
]