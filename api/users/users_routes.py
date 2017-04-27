from api.users.users_view_set import UsersViewSet


def set_users_routes(router):
    router.register(r'users', UsersViewSet)
