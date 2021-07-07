from django.urls import path
from .views import VehicleListCreateView, VehicleDetailsView


urlpatterns = [
    path('', VehicleListCreateView.as_view(), name=VehicleListCreateView.name),
    path('<int:pk>/', VehicleDetailsView.as_view(), name=VehicleDetailsView.name),
]