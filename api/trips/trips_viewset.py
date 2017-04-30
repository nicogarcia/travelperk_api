from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin, DestroyModelMixin
from rest_framework.viewsets import GenericViewSet

from api.trips.trips_model import Trip
from api.trips.trips_serializer import TripSerializer


class TripViewset(RetrieveModelMixin,
                  CreateModelMixin,
                  ListModelMixin,
                  DestroyModelMixin,
                  GenericViewSet):
    serializer_class = TripSerializer
    queryset = Trip.objects.all()

    def filter_queryset(self, queryset):
        return queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
