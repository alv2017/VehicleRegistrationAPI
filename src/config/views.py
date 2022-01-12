from rest_framework import generics
from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from vehicle_registry.views import VehicleListCreateView


class ApiRootView(generics.GenericAPIView):
    name = 'api-root'
    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        return Response({
            'vehicles': reverse(VehicleListCreateView.name, request=request),
        })
