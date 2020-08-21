from django.test import TestCase, Client
from django.urls import reverse, resolve
from idp_data.idp_data.models import HostnameMunicipality, Municipality


class TestUrls(TestCase):
    def setUp(self):
        self.client = Client()
        self.muniCode = "wc001"
        self.hostname = "localhost"

    def test_events_url_GET(self):
        muni = Municipality.objects.create(
            code=self.muniCode,
            name="test"
        )

        HostnameMunicipality.objects.create(
            muni=muni,
            hostname=self.hostname
        )

        url = reverse('events', kwargs={'host': self.hostname})
        response = self.client.get(url)

        self.assertEquals(response.status_code, 200)
        self.assertEquals(Municipality.objects.count(), 1)
        self.assertEquals(HostnameMunicipality.objects.count(), 1)

    def test_events_url_POST(self):
        url = reverse('events', kwargs={'host': self.hostname})
        response = self.client.post(url)

        self.assertEquals(response.status_code, 405)    #not allowed

    def test_events_url_DELETE(self):
        url = reverse('events', kwargs={'host': self.hostname})
        response = self.client.delete(url)

        self.assertEquals(response.status_code, 405)    #not allowed


    def test_geography_details_url_GET(self):
        muni = Municipality.objects.create(
            code=self.muniCode,
            name="test"
        )

        HostnameMunicipality.objects.create(
            muni=muni,
            hostname=self.hostname
        )

        url = reverse('geo', kwargs={'host': self.hostname})
        response = self.client.get(url)

        self.assertEquals(response.status_code, 200)
        self.assertEquals(Municipality.objects.count(), 1)
        self.assertEquals(HostnameMunicipality.objects.count(), 1)

    def test_geography_details_url_POST(self):
        url = reverse('geo', kwargs={'host': self.hostname})
        response = self.client.post(url)

        self.assertEquals(response.status_code, 405)    #not allowed

    def test_geography_details_url_DELETE(self):
        url = reverse('geo', kwargs={'host': self.hostname})
        response = self.client.delete(url)

        self.assertEquals(response.status_code, 405)    #not allowed