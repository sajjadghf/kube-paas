from django.shortcuts import render
from rest_framework import views, generics
from rest_framework.response import Response
from types import SimpleNamespace
import json
import requests
import os
from rest_framework import status
from rest_framework import permissions
from rest_framework.views import APIView
from django.http import HttpResponse
from django.http import JsonResponse
from django.core.cache import cache
from django.conf import settings
from kubernetes import client, config
import yaml
from kubernetes import client
from kubernetes.client import Configuration
from kubernetes.config import kube_config


class KubeCluster(object):
    def __init__(self, configuration_yaml):
        self.configuration_yaml = configuration_yaml
        self._configuration_yaml = None

    @property
    def config(self):
        with open(self.configuration_yaml, 'r') as f:
            if self._configuration_yaml is None:
                self._configuration_yaml = yaml.safe_load(f)
        return self._configuration_yaml

    @property
    def client(self):
        k8_loader = kube_config.KubeConfigLoader(self.config)
        call_config = type.__call__(Configuration)
        k8_loader.load_and_set(call_config)
        Configuration.set_default(call_config)
        return client.CoreV1Api()


kube_one = KubeCluster(configuration_yaml='C:/Users/s.ghafarian/Desktop/repo/AsaPaaS/PaaS/Config/kube-config')


def get_all_pods(self):
    result = kube_one.client.list_pod_for_all_namespaces(watch=False)
    all_pods = [item.metadata.name for item in result.items]
    return JsonResponse({"RunningPods": all_pods})


def get_all_services(self):
    result = kube_one.client.list_service_for_all_namespaces(watch=False)
    all_services = [item.metadata.name for item in result.items]
    return JsonResponse({"Services": all_services})


def get_all_nodes(self):
    result = kube_one.client.list_node(watch=False)
    all_nodes = [item.metadata.name for item in result.items]
    return JsonResponse({"Nodes": all_nodes})


def get_all_namespaces(self):
    result = kube_one.client.list_namespace(watch=False)
    all_ns = [item.metadata.name for item in result.items]
    return JsonResponse({"Namespaces": all_ns})


def get_all_pods_detailed(self):
    result = kube_one.client.list_pod_for_all_namespaces(watch=False)
    pod = {}
    all_pods = []
    for i in result.items:
        pod["Name"] = i.metadata.name
        pod["IP"] = i.status.pod_ip
        pod["Namespace"] = i.metadata.namespace
        all_pods.append(pod.copy())
    return JsonResponse({"RunningPods": all_pods})