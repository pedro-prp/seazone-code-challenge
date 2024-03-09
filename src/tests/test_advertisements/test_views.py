from rest_framework import status
from rest_framework.test import APITestCase

from advertisements.models import Advertisement
from properties.models import Property


class AdvertisementAPITest(APITestCase):
    def setUp(self):
        self.property = Property.objects.create(
            name="Casa de praia",
            cod_property="8021e85b-41b7-4b2a-b66e-9a3d69371c99",
            guests_limit=10,
            bath_quant=3,
            acceptable_pets=True,
            cleaning_fee=100.00,
            activation_date="2021-01-01",
        )
        self.advertisement = Advertisement.objects.create(
            id_advertisement="8021e85b-41b7-4b2a-b66e-9a3d69371c90",
            property=self.property,
            platform_name="Airbnb",
            platform_fee=20.00,
        )

    def test_advertisement_list(self):
        response = self.client.get("/advertisements/")

        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_advertisement_create(self):
        data = {
            "property": self.property.cod_property,
            "platform_name": "olx",
            "platform_fee": 30.00
        }
        response = self.client.post("/advertisements/", data)

        self.assertEqual(response.data["property"], self.property.cod_property)
        self.assertEqual(response.data["platform_name"], "olx")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_advertisement_detail(self):
        pk_advertisement = self.advertisement.id_advertisement

        response = self.client.get(f"/advertisements/{pk_advertisement}/")

        self.assertEqual(response.data["id_advertisement"], self.advertisement.id_advertisement)
        self.assertEqual(response.data["platform_name"], "Airbnb")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_advertisement_detail_not_found(self):
        pk_advertisement = "8021"

        response = self.client.get(f"/advertisements/{pk_advertisement}/")

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.json()["message"], "Advertisement not found")

    def test_advertisement_update(self):
        pk_advertisement = self.advertisement.id_advertisement

        data = {
            "platform_name": "olx",
            "platform_fee": 25.00,
            "property": "8021e85b-41b7-4b2a-b66e-9a3d69371c99"
        }

        response = self.client.put(f"/advertisements/{pk_advertisement}/", data)

        self.assertEqual(response.data["platform_name"], "olx")
        self.assertEqual(response.data["platform_fee"], '25.00')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
