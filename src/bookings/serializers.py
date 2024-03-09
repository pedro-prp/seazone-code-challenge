from rest_framework import serializers
from .models import Booking

from advertisements.models import Advertisement


class BookingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Booking
        fields = [
            "code_booking",
            "advertisement",
            "check_in_date",
            "check_out_date",
            "total_price",
            "comment",
            "number_of_guests",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["code_booking", "created_at", "updated_at"]
