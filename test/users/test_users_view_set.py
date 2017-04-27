from rest_framework.status import HTTP_201_CREATED
from rest_framework.test import APITestCase


class UserViewSetTest(APITestCase):
    API_ENDPOINT = '/v1/users'

    def test_create__ok(self):
        data = {
            'email': 'test@test.com',
            'password': 'testtest'
        }

        response = self.client.post(self.API_ENDPOINT, data)

        self.assertEqual(response.status_code, HTTP_201_CREATED, response.data)
