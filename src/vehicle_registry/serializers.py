from rest_framework import serializers
from .models import Vehicle


class VehicleSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    create_timestamp = serializers.ReadOnlyField()

    class Meta:
        model = Vehicle
        fields = ('id',
                  'number',
                  'maker',
                  'manufacturing_date',
                  'create_timestamp'
                  )
