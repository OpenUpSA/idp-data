from django.test import TestCase, Client
from django.urls import reverse, resolve
from datetime import date
from idp_data.idp_data.models import MunicipalityHostname, Municipality, Event, Category


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.muniCode = "wc001"
        self.hostname = "localhost"

    def test_events_data_count_for_hostname(self):
        muni = Municipality.objects.create(
            code=self.muniCode,
            name="test"
        )

        MunicipalityHostname.objects.create(
            muni=muni,
            hostname=self.hostname
        )

        category = Category.objects.create(
            name='test',
            icon='test'
        )

        Event.objects.create(
            muni=muni,
            title='test',
            short_desc='test',
            category=category,
            confirmed_date=date.today()
        )

        Event.objects.create(
            muni=muni,
            title='test2',
            short_desc='test2',
            category=category,
            confirmed_date=date.today()
        )

        url = reverse('events', kwargs={'host': self.hostname})
        response = self.client.get(url)

        self.assertEquals(len(response.data), 2)

    def test_events_data_count_for_wrong_hostname(self):
        muni = Municipality.objects.create(
            code=self.muniCode,
            name="test"
        )
        otherMuni = Municipality.objects.create(
            code="otherMuni",
            name="test"
        )

        MunicipalityHostname.objects.create(
            muni=muni,
            hostname=self.hostname
        )

        MunicipalityHostname.objects.create(
            muni=otherMuni,
            hostname='wrongHostname'
        )

        category = Category.objects.create(
            name='test',
            icon='test'
        )

        Event.objects.create(
            muni=muni,
            title='test',
            short_desc='test',
            category=category,
            confirmed_date=date.today()
        )

        url = reverse('events', kwargs={'host': 'wrongHostname'})
        response = self.client.get(url)

        self.assertEquals(len(response.data), 0)

    def test_events_serialized_correctly(self):
        muni = Municipality.objects.create(
            code=self.muniCode,
            name="test"
        )

        MunicipalityHostname.objects.create(
            muni=muni,
            hostname=self.hostname
        )

        category = Category.objects.create(
            name='test',
            icon='test'
        )

        Event.objects.create(
            muni=muni,
            title='test event name',
            short_desc='test',
            category=category,
            confirmed_date=date.today()
        )

        url = reverse('events', kwargs={'host': self.hostname})
        response = self.client.get(url)

        self.assertEquals(response.data[0]['title'], 'test event name')

    def test_muni_serialized_correctly(self):
        muni = Municipality.objects.create(
            code=self.muniCode,
            name="test muni name"
        )

        MunicipalityHostname.objects.create(
            muni=muni,
            hostname=self.hostname
        )

        url = reverse('geo', kwargs={'host': self.hostname})
        response = self.client.get(url)

        self.assertEquals(response.data['name'], 'test muni name')