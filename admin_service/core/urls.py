from django.urls import path
from .views import service_list_view

urlpatterns = [
    path('api/services/',service_list_view),
]
