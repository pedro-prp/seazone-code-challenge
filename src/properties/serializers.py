from rest_framework import serializers
from .models import Property

from advertisements.serializers import AdvertisementSerializer


class PropertySerializer(serializers.ModelSerializer):

    advertisements = AdvertisementSerializer(many=True, read_only=True)

    class Meta:
        model = Property
        fields = [
            "name",
            "cod_property",
            "guests_limit",
            "bath_quant",
            "acceptable_pets",
            "cleaning_fee",
            "activation_date",
            "created_at",
            "updated_at",
            "advertisements",
        ]

        read_only_fields = ["cod_property"]
