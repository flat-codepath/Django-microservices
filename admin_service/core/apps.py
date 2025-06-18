from django.apps import AppConfig
import atexit
import requests


class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'


    def ready(self):
        # Register service
        payload = {
            "Name": "admin-service",
            "ID": "admin-service-1",
            "Address": "localhost",
            "Port": 8003,
        }
        try:
            requests.put("http://localhost:8500/v1/agent/service/register", json=payload)
        except Exception as e:
            print("Failed to register admin-service:", e)

        # Deregister on shutdown
        atexit.register(self.deregister_service)

    def deregister_service(self):
        try:
            requests.put("http://localhost:8500/v1/agent/service/deregister/admin-service-1")
        except Exception as e:
            print("Failed to deregister:", e)



    