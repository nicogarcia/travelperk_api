from api.trips.trips_viewset import TripViewset


def set_trips_routes(router):
    router.register(r'trips', TripViewset)
