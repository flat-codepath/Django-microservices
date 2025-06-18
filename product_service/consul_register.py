# consul_register.py
import requests

def register_to_consul(service_name, service_id, port):
    print(f"📡 Registering {service_name} on port {port}...")
    url = "http://localhost:8500/v1/agent/service/register"
    payload = {
        "Name": service_name,
        "ID": service_id,
        "Address": "localhost",
        "Port": port,
        "Check": {
        "HTTP": f"http://localhost:{port}/health/",
        "Interval": "10s",
        "Timeout": "1s"
    }
        
    }
    try:
        res = requests.put(url, json=payload)
        print(f"✅ Registered {service_name} to Consul: {res.status_code}")
    except Exception as e:
        print(f"❌ Failed to register to Consul: {e}")
