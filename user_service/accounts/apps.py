from django.apps import AppConfig
from accounts.views import load_config


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'
   
    def ready(self):
        from consul_register import register_to_consul
        print('Registering user-service to Consul...')
        register_to_consul("user-service", "user-service-1", 8001)
    
    def ready(self):
        print("[Config] Fetching centralized config...")
        load_config()