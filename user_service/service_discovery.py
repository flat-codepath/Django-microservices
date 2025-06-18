# service_discovery.py
import requests

def get_service_url(service_name):
    url = f"http://localhost:8500/v1/agent/services"
    try:
        res = requests.get(url)
        services = res.json()
        for service_id, details in services.items():
            if details["Service"] == service_name:
                address = details["Address"]
                port = details["Port"]
                return f"http://{address}:{port}"
        raise Exception(f"Service {service_name} not found")
    except Exception as e:
        print(f"❌ Service discovery error: {e}")
        return None
