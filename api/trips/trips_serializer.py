from rest_framework.serializers import ModelSerializer

from api.trips.trips_model import Trip


class TripSerializer(ModelSerializer):
    class Meta:
        model = Trip

        fields = ('id', 'created_at', 'from_place', 'name', 'to_place', 'user')

        read_only_fields = ('created_at', 'user')
