from rest_framework.status import HTTP_200_OK
from rest_framework.test import APITestCase

from api.users.users_model import User


class AuthViewSetTest(APITestCase):
    API_ENDPOINT = '/v1/token'

    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            email='messi@messi.com',
            password='messimessi'
        )

    def test_create__ok(self):
        data = {
            'email': 'messi@messi.com',
            'password': 'messimessi'
        }

        response = self.client.post(self.API_ENDPOINT, data)

        self.assertEqual(response.status_code, HTTP_200_OK, response.data)
