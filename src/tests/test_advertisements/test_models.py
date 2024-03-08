from django.test import TestCase

from advertisements.models import Advertisement
from properties.models import Property


class AdvertisementModelTest(TestCase):
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
            property=self.property,
            platform_name="olx",
            platform_fee=150.00,
        )

    def test_advertisement_str(self):
        self.assertEqual(str(self.advertisement), "6600bf1e-7456-4bd3-b8f5-0f63b170c5e6")