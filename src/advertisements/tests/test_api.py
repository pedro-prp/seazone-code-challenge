from django.test import TestCase

from advertisements.models import Advertisement
from properties.models import Property

from rest_framework import status
from rest_framework.test import APITestCase


class AdvertisementAPITest(TestCase):
    def setUp(self):
        self.property = Property.objects.create(
            name="Casa de praia",
            cod_property="CP001",
            guests_limit=10,
            bath_quant=3,
            acceptable_pets=True,
            cleaning_fee=100.00,
            activation_date="2021-01-01",
        )

        self.advertisement = Advertisement.objects.create(
            id_advertisement="6600bf1e-7456-4bd3-b8f5-0f63b170c5e6",
            property="CP001",
            platform_name="olx",
            platform_fee=150.00,
        )

    def test_advertisement_list(self):
        response = self.client.get("/advertisements/")

        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_advertisement_create(self):
        data = {
            "id_advertisement": "6600bf1e-7456-4bd3-b8f5-0f63b170c5e6",
            "property": "CP001",
            "platform_name": "olx",
            "platform_fee": 150.00,
        }
        response = self.client.post("/advertisements/", data)

        self.assertEqual(response.data["id_advertisement"], "6600bf1e-7456-4bd3-b8f5-0f63b170c5e6")
        self.assertEqual(response.data["platform_name"], "olx")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_advertisement_detail(self):
        pk_advertisement = "6600bf1e-7456-4bd3-b8f5-0f63b170c5e6"
        response = self.client.get(f"/advertisements/{pk_advertisement}/")

        self.assertEqual(response.data["id_advertisement"], "6600bf1e-7456-4bd3-b8f5-0f63b170c5e6")
        self.assertEqual(response.data["platform_name"], "olx")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_advertisement_update(self):
        pk_advertisement = "6600bf1e-7456-4bd3-b8f5-0f63b170c5e6"
        data = {
            "id_advertisement": "6600bf1e-7456-4bd3-b8f5-0f63b170c5e6",
            "property": "CP001",
            "platform_name": "airbnb",
            "platform_fee": 200.00,
        }

        response = self.client.put(f"/advertisements/{pk_advertisement}/", data)

        self.assertEqual(response.data["id_advertisement"], "6600bf1e-7456-4bd3-b8f5-0f63b170c5e6")
        self.assertEqual(response.data["platform_name"], "airbnb")
        self.assertEqual(response.data["platform_fee"], "200.00")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_advertisement_delete(self):
        pk_advertisement = "6600bf1e-7456-4bd3-b8f5-0f63b170c5e6"
        response = self.client.delete(f"/advertisements/{pk_advertisement}/")

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_advertisement_not_found(self):
        pk_advertisement_not_found = "6600bf1e-7456-4bd3-b8f5-0f63b170c5e7"
        response = self.client.get(f"/advertisements/{pk_advertisement_not_found}/")

        self.assertEqual(response.data["message"], "Advertisement not found")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
