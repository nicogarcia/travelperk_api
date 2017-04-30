from rest_framework.serializers import ModelSerializer

from api.trips.trips_model import Trip


class TripSerializer(ModelSerializer):
    class Meta:
        model = Trip

        fields = ('id', 'name', 'created_at', 'user')

        read_only_fields = ('created_at', 'user')
