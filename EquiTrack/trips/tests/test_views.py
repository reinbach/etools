__author__ = 'unicef-leb-inn'

from datetime import timedelta, datetime
from rest_framework.reverse import reverse
from django.template.loader import render_to_string
from django.test import TestCase, Client, RequestFactory
from rest_framework.test import APIRequestFactory, force_authenticate, APITestCase


from EquiTrack.factories import TripFactory, UserFactory
from trips.models import Trip
from trips.views import TripsApprovedView, TripsListApi, TripsByOfficeView, TripActionView


class ViewTest(APITestCase):

    def setUp(self):
        self.client_stub = Client()
        self.trip = TripFactory(
            owner__first_name='Fred',
            owner__last_name='Test',
            purpose_of_travel='To test some trips'
        )

    def test_view_trips_approved(self):
        factory = APIRequestFactory()
        user = UserFactory()
        view = TripsApprovedView.as_view()
        # Make an authenticated request to the view...
        request = factory.get('/approved/')
        force_authenticate(request, user=user)
        response = view(request)
        response.render()
        self.assertEquals(response.status_code, 200)

    def test_view_trips_api(self):
        factory = APIRequestFactory()
        user = UserFactory()
        view = TripsListApi.as_view()
        # Make an authenticated request to the view...
        request = factory.get('/api/')
        force_authenticate(request, user=user)
        response = view(request)
        self.assertEquals(response.status_code, 200)

    def test_view_trips_api_action(self):

        user = UserFactory()

        # Make an authenticated request to the view...
        url = reverse('trips_api_action', args=[self.trip.id, 'submitted'])

        # request = factory.post('/api/' + str(self.trip.id) + '/submitted/', {})
        self.client.force_authenticate(user=self.trip.owner)
        response = self.client.post(url, {}, format='json')

        self.assertEquals(response.status_code, 200)
        self.assertEqual(response.data.get('status'), 'submitted')

    def test_view_trip_action(self):
        factory = APIRequestFactory()
        user = UserFactory()
        view = TripsByOfficeView.as_view()
        # Make an authenticated request to the view...
        request = factory.get('/offices/')
        force_authenticate(request, user=self.trip.owner)
        response = view(request)
        self.assertEquals(response.status_code, 200)

    def test_view_trips_dashboard(self):
        response = self.client_stub.get('/trips/')
        self.assertEquals(response.status_code, 200)

