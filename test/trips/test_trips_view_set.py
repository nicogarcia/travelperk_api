from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_401_UNAUTHORIZED, HTTP_204_NO_CONTENT, \
    HTTP_200_OK, HTTP_404_NOT_FOUND
from rest_framework.test import APITestCase

from api.trips.trips_model import Trip
from api.users.users_model import User


class TripViewSetTest(APITestCase):
    API_ENDPOINT = '/v1/trips'

    @classmethod
    def setUpTestData(cls):
        cls.user_trip1 = User.objects.create_user(id=1, email='test1@test.com', password='testtest')
        cls.user_trip10 = User.objects.create_user(id=2, email='test2@test.com', password='testtest')

        cls.trip10 = Trip.objects.create(id=10, name='Trip 10', user=cls.user_trip10)
        cls.trip1 = Trip.objects.create(id=1, name='Trip 1', user=cls.user_trip1)

    '''
    Create
    '''

    def test_create__anonymous__unauthorized(self):
        data = {
            'name': 'Test name'
        }

        response = self.client.post(self.API_ENDPOINT, data)

        self.assertEqual(response.status_code, HTTP_401_UNAUTHORIZED, response.data)

    def test_create__signed_up__ok(self):
        self.client.force_authenticate(user=self.user_trip1)

        data = {
            'name': 'Test name'
        }

        response = self.client.post(self.API_ENDPOINT, data)

        self.assertEqual(response.status_code, HTTP_201_CREATED, response.data)

    def test_create__without_name__bad_request(self):
        self.client.force_authenticate(user=self.user_trip1)

        data = {}

        response = self.client.post(self.API_ENDPOINT, data)

        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST, response.data)

    def test_create__blank_name__bad_request(self):
        self.client.force_authenticate(user=self.user_trip1)

        data = {
            'name': ''
        }

        response = self.client.post(self.API_ENDPOINT, data)

        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST, response.data)

    '''
    List
    '''

    def test_list__anonymous__unauthorized(self):
        response = self.client.get(self.API_ENDPOINT)

        self.assertEqual(response.status_code, HTTP_401_UNAUTHORIZED, response.data)

    def test_list__only_own__ok(self):
        self.client.force_authenticate(user=self.user_trip10)

        response = self.client.get(self.API_ENDPOINT)

        self.assertEqual(response.status_code, HTTP_200_OK, response.data)
        self.assertEqual(response.data[0]['id'], self.trip10.id)

    '''
    Delete
    '''

    def test_delete__anonymous__unauthorized(self):
        response = self.client.delete('{}/{id}'.format(self.API_ENDPOINT, id=self.trip10.id))

        self.assertEqual(response.status_code, HTTP_401_UNAUTHORIZED, response.data)

    def test_delete__ok(self):
        self.client.force_authenticate(user=self.user_trip10)

        response = self.client.delete('{}/{id}'.format(self.API_ENDPOINT, id=self.trip10.id))

        self.assertEqual(response.status_code, HTTP_204_NO_CONTENT, response.data)

    def test_delete__not_own__not_found(self):
        self.client.force_authenticate(user=self.user_trip1)

        response = self.client.delete('{}/{id}'.format(self.API_ENDPOINT, id=self.trip10.id))

        self.assertEqual(response.status_code, HTTP_404_NOT_FOUND, response.data)

    '''
    Retrieve
    '''

    def test_retrieve__anonymous__unauthorized(self):
        response = self.client.get('{}/{id}'.format(self.API_ENDPOINT, id=self.trip10.id))

        self.assertEqual(response.status_code, HTTP_401_UNAUTHORIZED, response.data)

    def test_retrieve__owner__ok(self):
        self.client.force_authenticate(user=self.user_trip10)

        response = self.client.get('{}/{id}'.format(self.API_ENDPOINT, id=self.trip10.id))

        self.assertEqual(response.status_code, HTTP_200_OK, response.data)
        self.assertEqual(response.data['id'], self.trip10.id)

    def test_retrieve__not_owner__not_found(self):
        self.client.force_authenticate(user=self.user_trip1)

        response = self.client.get('{}/{id}'.format(self.API_ENDPOINT, id=self.trip10.id))

        self.assertEqual(response.status_code, HTTP_404_NOT_FOUND, response.data)
