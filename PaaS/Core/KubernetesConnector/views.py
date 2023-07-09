from django.shortcuts import render
from rest_framework import views, generics
from rest_framework.response import Response
from types import SimpleNamespace
import json
import requests
from rest_framework import status
from rest_framework import permissions
from rest_framework.views import APIView
from django.http import HttpResponse
from django.http import JsonResponse
from django.core.cache import cache
from django.conf import settings
from kubernetes import client, config

def get_data_from_cluster(self, *args, **kwargs):
    # todo
    return ;