from django.test import TestCase

from rest_framework import status
from rest_framework.test import APITestCase

from .models import Property


class PropertyModelTest(TestCase):
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

    def test_property_str(self):
        self.assertEqual(str(self.property), "Casa de praia")


class PropertyAPITest(APITestCase):
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

    def test_property_list(self):
        response = self.client.get("/properties/")

        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_property_create(self):
        data = {
            "name": "Casa de campo",
            "cod_property": "CC001",
            "guests_limit": 8,
            "bath_quant": 2,
            "acceptable_pets": False,
            "cleaning_fee": 80.00,
            "activation_date": "2021-01-01",
        }
        response = self.client.post("/properties/", data)

        self.assertEqual(response.data["cod_property"], "CC001")
        self.assertEqual(response.data["name"], "Casa de campo")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_property_create_already_exists(self):
        data = {
            "name": "Casa de praia",
            "cod_property": "CP001",
            "guests_limit": 10,
            "bath_quant": 3,
            "acceptable_pets": True,
            "cleaning_fee": 100.00,
            "activation_date": "2021-01-01",
        }
        response = self.client.post("/properties/", data)

        self.assertEqual(response.data["message"], "Property already exists")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_property_detail(self):
        pk_property = "CP001"

        response = self.client.get(f"/properties/{pk_property}/")

        self.assertEqual(response.data["cod_property"], "CP001")
        self.assertEqual(response.data["name"], "Casa de praia")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_property_not_found(self):
        pk_property_not_found = "CP002"

        response = self.client.get(f"/properties/{pk_property_not_found}/")

        self.assertEqual(response.data["message"], "Property not found")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_property_update(self):
        pk_property = "CP001"
        data = {
            "name": "Casa de campo",
            "cod_property": "CP001",
            "guests_limit": 8,
            "bath_quant": 2,
            "acceptable_pets": False,
            "cleaning_fee": 80.00,
            "activation_date": "2021-01-01",
        }
        response = self.client.put(f"/properties/{pk_property}/", data)

        self.assertEqual(response.data["cod_property"], "CP001")
        self.assertEqual(response.data["name"], "Casa de campo")
        self.assertEqual(response.data["guests_limit"], 8)
        self.assertEqual(response.data["bath_quant"], 2)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_property_update_not_found(self):
        pk_property_not_found = "CP002"
        data = {
            "name": "Casa de campo",
            "cod_property": "CP002",
            "guests_limit": 8,
            "bath_quant": 2,
            "acceptable_pets": False,
            "cleaning_fee": 80.00,
            "activation_date": "2021-01-01",
        }
        response = self.client.put(f"/properties/{pk_property_not_found}/", data)

        self.assertEqual(response.data["message"], "Property not found")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_property_delete(self):
        pk_property = "CP001"

        response = self.client.delete(f"/properties/{pk_property}/")

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_property_delete_not_found(self):
        pk_property_not_found = "CP002"

        response = self.client.delete(f"/properties/{pk_property_not_found}/")

        self.assertEqual(response.data["message"], "Property not found")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
