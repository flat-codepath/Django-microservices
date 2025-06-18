from py_zipkin.zipkin import zipkin_span, ZipkinAttrs
from django.utils.deprecation import MiddlewareMixin
import uuid
import requests

def default_transport_handler(encoded_span):
    requests.post(
        "http://localhost:9411/api/v2/spans",
        data=encoded_span,
        headers={'Content-Type': 'application/x-thrift'},
    )

class ZipkinMiddleware(MiddlewareMixin):
    def process_request(self, request):
        trace_id = uuid.uuid4().hex[:16]
        span_id = uuid.uuid4().hex[:16]
        request.zipkin_attrs = ZipkinAttrs(
            trace_id=trace_id,
            span_id=span_id,
            parent_span_id=None,
            flags='0',
            is_sampled=True,
        )

    def process_response(self, request, response):
        if hasattr(request, 'zipkin_attrs'):
            with zipkin_span(
                service_name=request.get_host(),
                zipkin_attrs=request.zipkin_attrs,
                span_name=request.path,
                transport_handler=default_transport_handler,
                sample_rate=100.0,
            ):
                pass
        return response
    

from django.http import JsonResponse

class APIKeyMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.valid_api_key = "super-secret-api-key"

    def __call__(self, request):
        if request.path.startswith("/api/"):
            print("🔑 Checking API key for request:", request.path)
            api_key = request.headers.get("X-API-KEY")
            if api_key != self.valid_api_key:
                print("❌ Unauthorized access attempt with API key:", api_key)
                return JsonResponse({"error": "Unauthorized"}, status=401)
        return self.get_response(request)