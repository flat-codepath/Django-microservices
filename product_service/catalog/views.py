from django.shortcuts import render
from django.http import JsonResponse
from django.views import View

# Create your views here.
class ProductListView(View):
    def get(self, request):
        products = ["Smart Water Bottle", "AI Notebook", "Solar Charger"]
        return JsonResponse({"products": products})
    
class HealthCheckView(View):
    def get(self, request):
        return JsonResponse({"status": "ok"})