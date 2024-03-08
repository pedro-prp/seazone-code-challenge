from bookings.exceptions import (
    BookingSerializerException,
    BookingNotFound,
    BookingCheckoutPreCheckinException,
)

from uuid import uuid4


class BookingRepository:
    def __init__(self, booking_model, booking_serializer):
        self._booking_model = booking_model
        self._booking_serializer = booking_serializer

    def get_all_bookings(self):
        bookings = self._booking_model.objects.all()

        serializer = self._booking_serializer(bookings, many=True)

        return serializer.data

    def create_booking(self, data):
        serializer = self._booking_serializer(data=data)
        if serializer.is_valid():
            code_booking = uuid4()

            checkin = serializer.validated_data.get("check_in_date")
            checkout = serializer.validated_data.get("check_out_date")

            if checkin >= checkout:
                raise BookingCheckoutPreCheckinException()

            booking_object = self._booking_model(
                **serializer.validated_data,
                code_booking=code_booking,
            )
            booking_object.save()

            booking_data = serializer.data
            booking_data["code_booking"] = code_booking

            return booking_data

        raise BookingSerializerException(serializer.errors)

    def get_booking_by_id(self, id_booking):
        try:
            booking_object = self._booking_model.objects.get(
                id_booking=id_booking,
            )
        except self._booking_model.DoesNotExist:
            raise BookingNotFound()

        serializer = self._booking_serializer(data=booking_object.__dict__)

        if serializer.is_valid():
            booking_data = {
                **serializer.validated_data,
                "id_booking": id_booking,
            }

            return booking_data

        raise BookingSerializerException(serializer.errors)

    def update_booking(self, id_booking, data):
        try:
            self._booking_model.objects.get(
                id_booking=id_booking,
            )
        except self._booking_model.DoesNotExist:
            raise BookingNotFound()

        serializer = self._booking_serializer(data=data)

        if serializer.is_valid():
            checkin = serializer.validated_data.get("checkin")
            checkout = serializer.validated_data.get("checkout")

            if checkin >= checkout:
                raise BookingCheckoutPreCheckinException()

            self._booking_model.objects.filter(
                id_booking=id_booking,
            ).update(**serializer.validated_data)

            return serializer.data

        raise BookingSerializerException(serializer.errors)

    def delete_booking(self, id_booking):
        try:
            booking_obj = self._booking_model.objects.get(id_booking=id_booking)
        except self._booking_model.DoesNotExist:
            raise BookingNotFound()

        booking_obj.delete()