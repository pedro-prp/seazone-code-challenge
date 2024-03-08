from rest_framework import serializers
from .models import Advertisement
from properties.models import Property

from bookings.serializers import BookingSerializer


class AdvertisementSerializer(serializers.ModelSerializer):

    reservations = BookingSerializer(many=True, read_only=True)

    class Meta:
        model = Advertisement
        fields = [
            "id_advertisement",
            "property",
            "platform_name",
            "platform_fee",
            "created_at",
            "updated_at",
            "reservations",
        ]
        read_only_fields = ["id_advertisement", "created_at", "updated_at"]
