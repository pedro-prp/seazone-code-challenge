from rest_framework import status
from rest_framework.test import APITestCase

from properties.models import Property
from advertisements.models import Advertisement
from bookings.models import Booking


class BookingAPITest(APITestCase):
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
            property=self.property,
            id_advertisement="8021e85b-41b7-4b2a-b66e-9a3d69371c90",
            platform_name="Airbnb",
            platform_fee=20.00,
        )
        self.booking = Booking.objects.create(
            code_booking="8021e85b-41b7-4b2a-b66e-9a3d69371c91",
            advertisement=self.advertisement,
            check_in_date="2021-01-01",
            check_out_date="2021-01-10",
            total_price=1000.00,
            comment="",
            number_of_guests=3,
        )

    def test_booking_list(self):
        response = self.client.get("/bookings/")

        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_booking_create(self):
        data = {
            "check_in_date": "2024-03-01",
            "check_out_date": "2024-03-10",
            "total_price": 1000,
            "number_of_guests": 3,
            "advertisement": self.advertisement.id_advertisement,
        }

        response = self.client.post("/bookings/", data)

        self.assertEqual(
            response.data["advertisement"], self.advertisement.id_advertisement
        )
        self.assertEqual(response.data["number_of_guests"], 3)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_booking_create_with_check_in_date_greater_than_check_out_date(self):
        data = {
            "check_in_date": "2024-03-04",
            "check_out_date": "2024-03-03",
            "total_price": 1000,
            "number_of_guests": 3,
            "advertisement": self.advertisement.id_advertisement,
        }

        response = self.client.post("/bookings/", data)

        self.assertEqual(
            response.json()["message"], "Checkout date is before checkin date"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_booking_detail(self):
        pk_booking = self.booking.code_booking

        response = self.client.get(f"/bookings/{pk_booking}/")

        self.assertEqual(response.data["code_booking"], self.booking.code_booking)
        self.assertEqual(response.data["number_of_guests"], 3)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_booking_detail_not_found(self):
        pk_booking = "8021"

        response = self.client.get(f"/bookings/{pk_booking}/")

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.json()["message"], "Booking not found")

    def test_booking_delete(self):
        pk_booking = self.booking.code_booking

        response = self.client.delete(f"/bookings/{pk_booking}/")

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(response.data, None)

    def test_booking_delete_not_found(self):
        pk_booking = "8021"

        response = self.client.delete(f"/bookings/{pk_booking}/")

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.json()["message"], "Booking not found")
