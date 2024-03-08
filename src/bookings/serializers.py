from rest_framework import serializers
from .models import Booking

from advertisements.models import Advertisement


class BookingSerializer(serializers.ModelSerializer):
    advertisement = serializers.SerializerMethodField()

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
        read_only_fields = ["code_booking"]

    def get_advertisement(self, obj):
        advertisement = Advertisement.objects.get(id_advertisement=obj.advertisement.id_advertisement)

        advertisement_data = {
            "id_advertisement": advertisement.id_advertisement,
            "platform_name": advertisement.platform_name,
            "platform_fee": advertisement.platform_fee,
            "created_at": advertisement.created_at,
            "updated_at": advertisement.updated_at,
        }

        return advertisement_data
