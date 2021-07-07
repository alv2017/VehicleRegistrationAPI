from rest_framework import generics
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from .models import Vehicle
from .serializers import VehicleSerializer


class VehicleListCreateView(generics.ListCreateAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    name = 'vehicles'

    authentication_classes = (
        TokenAuthentication,
        SessionAuthentication
    )
    permission_classes = (
        IsAuthenticated,
    )

    filter_backends = (SearchFilter, )
    search_fields = ('^number', )


class VehicleDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    name = 'vehicle-details'

    authentication_classes = (
        TokenAuthentication,
        SessionAuthentication
    )
    permission_classes = (
        IsAuthenticated,
    )
