from django.urls import path
from .views import ConfigView

urlpatterns = [
    path('config/<str:service_name>/', ConfigView.as_view(), name='get-config'),
]