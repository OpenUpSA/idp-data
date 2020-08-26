from django.test import TestCase, Client
from django.urls import reverse, resolve
from datetime import date
from idp_data.idp_data.models import MunicipalityHostname, Municipality, Event, Category


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.muniCode = "wc001"
        self.hostname = "localhost"
        self.muni = Municipality.objects.create(
            code=self.muniCode,
            name="test"
        )
        self.category = Category.objects.create(
            name='test',
            icon='test'
        )

        MunicipalityHostname.objects.create(
            muni=self.muni,
            hostname=self.hostname
        )
        Event.objects.create(
            muni=self.muni,
            title='test',
            short_desc='test',
            category=self.category,
            end_date=date.today()
        )

    def test_events_data_count_for_hostname(self):
        Event.objects.create(
            muni=self.muni,
            title='test2',
            short_desc='test2',
            category=self.category,
            end_date=date.today()
        )

        url = reverse('events', kwargs={'host': self.hostname})
        response = self.client.get(url)

        self.assertEquals(len(response.data), 2)

    def test_events_data_count_for_wrong_hostname(self):
        otherMuni = Municipality.objects.create(
            code="otherMuni",
            name="test"
        )

        MunicipalityHostname.objects.create(
            muni=otherMuni,
            hostname='wrongHostname'
        )

        url = reverse('events', kwargs={'host': 'wrongHostname'})
        response = self.client.get(url)

        self.assertEquals(len(response.data), 0)

    def test_events_serialized_correctly(self):
        url = reverse('events', kwargs={'host': self.hostname})
        response = self.client.get(url)

        self.assertEquals(response.data[0]['title'], 'test')

    def test_muni_serialized_correctly(self):
        url = reverse('geo', kwargs={'host': self.hostname})
        response = self.client.get(url)

        self.assertEquals(response.data['name'], 'test')