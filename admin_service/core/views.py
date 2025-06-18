from django.shortcuts import render
import requests
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views import View


# Create your views here.
def service_list_view(request):
        try:
            res = requests.get('http://localhost:8500/v1/agent/services')
            return JsonResponse(res.json())
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
        

class HealthCheckView(View):
    def get(self, request):
        return JsonResponse({"status": "ok"})