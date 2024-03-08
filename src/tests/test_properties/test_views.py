from django.test import TestCase

from rest_framework import status
from rest_framework.test import APITestCase

from properties.models import Property


class PropertyAPITest(APITestCase):
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

    def test_property_list(self):
        response = self.client.get("/properties/")

        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_property_create(self):
        data = {
            "name": "Casa de campo",
            "guests_limit": 8,
            "bath_quant": 2,
            "acceptable_pets": False,
            "cleaning_fee": 80.00,
            "activation_date": "2021-01-01",
        }
        response = self.client.post("/properties/", data)

        self.assertEqual(response.data["name"], "Casa de campo")
        self.assertEqual(response.data["guests_limit"], 8)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_property_detail(self):
        pk_property = "8021e85b-41b7-4b2a-b66e-9a3d69371c99"

        response = self.client.get(f"/properties/{pk_property}/")

        self.assertEqual(response.data["cod_property"], "8021e85b-41b7-4b2a-b66e-9a3d69371c99")
        self.assertEqual(response.data["name"], "Casa de praia")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_property_detail_not_found(self):
        pk_property = "8021"

        response = self.client.get(f"/properties/{pk_property}/")

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.json()["message"], "Property not found")

    def test_property_update(self):
        pk_property = "8021e85b-41b7-4b2a-b66e-9a3d69371c99"
        data = {
            "name": "Casa de campo",
            "guests_limit": 5,
            "bath_quant": 4,
            "acceptable_pets": True,
            "cleaning_fee": 80.00,
            "activation_date": "2021-01-01",
        }

        response = self.client.put(f"/properties/{pk_property}/", data)

        self.assertEqual(response.data["name"], "Casa de campo")
        self.assertEqual(response.data["guests_limit"], 5)
        self.assertEqual(response.data["bath_quant"], 4)
        self.assertEqual(response.data["acceptable_pets"], True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_property_update_not_found(self):
        pk_property = "8021"
        data = {
            "name": "Casa de campo",
            "guests_limit": 5,
            "bath_quant": 4,
            "acceptable_pets": True,
            "cleaning_fee": 80.00,
            "activation_date": "2021-01-01",
        }

        response = self.client.put(f"/properties/{pk_property}/", data)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.json()["message"], "Property not found")

    def test_property_delete(self):
        pk_property = "8021e85b-41b7-4b2a-b66e-9a3d69371c99"

        response = self.client.delete(f"/properties/{pk_property}/")

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_property_delete_not_found(self):
        pk_property = "8021"

        response = self.client.delete(f"/properties/{pk_property}/")

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.json()["message"], "Property not found")
