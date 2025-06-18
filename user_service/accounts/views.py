from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
import requests, json
from rest_framework.response import Response


# Create your views here.
class UserListView(View):
    def get(self, request):
        users = ["Nagnath", "Anil", "Sneha"]
        return JsonResponse({"users": users})


# class UsersWithProductsView(View):
#     def get(self, request):
#         users = ["Nagnath", "Anil", "Sneha"]

#         try:
#             response = requests.get("http://127.0.0.1:8002/api/products/")
#             products = response.json().get("products", [])
#         except requests.exceptions.RequestException:
#             products = ["Could not fetch products"]

#         return JsonResponse({
#             "users": users,
#             "products": products
#         })


from service_discovery import get_service_url

class UsersWithProductsView(View):
    def get(self, request):
        users = ["Nagnath", "Anil", "Sneha"]

        product_service_url = get_service_url("product-service")
        if not product_service_url:
            return JsonResponse({"error": "Product service not available"}, status=503)

        try:
            response = requests.get(f"{product_service_url}/api/products/")
            print(f"Product service response: {response.status_code}")
            print(response.json())
            products = response.json().get("products", [])
        except requests.exceptions.RequestException as e:
            return JsonResponse({"error": str(e)}, status=500)

        return JsonResponse({
            "users": users,
            "products": products
        })

    
        # product_url = get_service_url("product-service")
        # print(f"Product service URL: {product_url}")
        # if product_url:
        #     res = requests.get(f"{product_url}/api/products/")
        #     return Response(res.json())
        # else:
        #     return Response({"error": "Product service not found"}, status=500)

class HealthCheckView(View):
    def get(self, request):
        return JsonResponse({"status": "ok"})
    



CONFIG_CACHE = {}

def load_config():
    global CONFIG_CACHE
    try:
        response = requests.get("http://localhost:8003/config/user_service/")
        if response.status_code == 200:
            CONFIG_CACHE = response.json()
        else:
            print(f"[Config] Failed to load config: {response.status_code}")
    except Exception as e:
        print(f"[Config] Error loading config: {e}")



from rest_framework.views import APIView
from py_zipkin.zipkin import zipkin_span
class ProductProxyView(APIView):
    def get(self, request):
        # with zipkin_span(
        #     service_name='user-service',
        #     span_name='call-product-service',
        #     transport_handler=lambda x: requests.post(
        #         CONFIG_CACHE.get("ZIPKIN_URL", "http://localhost:9411") + "/api/v2/spans",
        #         data=x,
        #         headers={'Content-Type': 'application/x-thrift'},
        #     ),
        #     sample_rate=100.0,
        # ):
            product_url = get_service_url("product-service")
            if product_url:
                headers = {"X-API-KEY": "super-secret-api-key"}  # ✅ Your shared key
                response = requests.get(f"{product_url}/api/products/", headers=headers)
                return Response(response.json())
            return Response({"error": "Service not available"}, status=500)