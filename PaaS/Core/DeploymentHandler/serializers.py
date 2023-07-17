from rest_framework import serializers
from .models import Deployment


class DeploymentSerializer(serializers.ModelSerializer):
    dep_name = serializers.CharField(max_length=30)
    pod_name = serializers.CharField(max_length=30)
    image = serializers.CharField(max_length=60)
    ports = serializers.CharField(max_length=30)
    resources_cpu_request = serializers.CharField(max_length=30)
    resources_cpu_limit = serializers.CharField(max_length=30)
    resources_memory_request = serializers.CharField(max_length=30)
    resources_memory_limit = serializers.CharField(max_length=30)
    main_label_name = serializers.CharField(max_length=30)
    main_label_value = serializers.CharField(max_length=30)
    pod_replicas = serializers.CharField(max_length=30)

    class Meta:
        model = Deployment
        fields = ('__all__')

    def create(self, validated_data):
        """
        Create and return a new `Deployment` instance, given the validated data.
        """
        return Deployment.objects.create(**validated_data)
