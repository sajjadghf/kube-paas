import datetime
import pytz
from kubernetes import client, config
from django.shortcuts import render
from .models import Deployment
from .serializers import DeploymentSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response


class DeploymentViewSet(viewsets.ViewSet):
    def list_deployments(self, request):
        dep_list = Deployment.objects.all()
        serializer = DeploymentSerializer(dep_list, many=True)
        return Response(serializer.data)

    def create_deployment(self, request):
        serializer = DeploymentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
