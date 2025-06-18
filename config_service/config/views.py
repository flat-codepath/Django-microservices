from django.shortcuts import render
from django.http import JsonResponse
from django.views import View

# Create your views here.
CENTRAL_CONFIG = {
    "user_service": {
        "DB_HOST": "localhost",
        "DB_PORT": "5432",
        "ZIPKIN_URL": "http://localhost:9411"
    },
    "product_service": {
        "DB_HOST": "localhost",
        "DB_PORT": "5432",
        "ZIPKIN_URL": "http://localhost:9411"
    }
}


class ConfigView(View):
    def get(self, request, service_name):
        config = CENTRAL_CONFIG.get(service_name, {})
        return JsonResponse(config)