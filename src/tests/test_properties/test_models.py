from django.test import TestCase

from properties.models import Property


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
