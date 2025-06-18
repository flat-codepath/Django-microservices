from django.apps import AppConfig


class CatalogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'catalog'

    def ready(self):
        from consul_register import register_to_consul
        print("📦 Catalog app is ready, registering to Consul...")
        register_to_consul("product-service", "product-service-1", 8002)
        
    
    
