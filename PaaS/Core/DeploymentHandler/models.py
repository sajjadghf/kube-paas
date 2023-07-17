from django.db import models


class Deployments(models.Model):
    dep_name = models.CharField(max_length=30)
    pod_name = models.CharField(max_length=30)
    image = models.CharField(max_length=60)
    ports = models.CharField(max_length=30)
    resources_cpu_request = models.CharField(max_length=30)
    resources_cpu_limit = models.CharField(max_length=30)
    resources_memory_request = models.CharField(max_length=30)
    resources_memory_limit = models.CharField(max_length=30)
    main_label_name = models.CharField(max_length=30)
    main_label_value = models.CharField(max_length=30)
    pod_replicas = models.CharField(max_length=30)
