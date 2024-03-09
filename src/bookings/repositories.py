from bookings.exceptions import (
    BookingSerializerException,
    BookingNotFoundException,
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

            print(data.keys())

            booking_object = self._booking_model(
                **serializer.validated_data,
                code_booking=code_booking,
                # advertisement_id=data.get("advertisement"),
            )
            booking_object.save()

            booking_data = serializer.data
            booking_data["code_booking"] = code_booking

            return booking_data

        raise BookingSerializerException(serializer.errors)

    def get_booking_by_id(self, code_booking):
        try:
            booking_object = self._booking_model.objects.get(
                code_booking=code_booking,
            )
        except self._booking_model.DoesNotExist:
            raise BookingNotFoundException()

        booking_data = {
            "code_booking": booking_object.code_booking,
            "advertisement": booking_object.advertisement_id,
            "check_in_date": booking_object.check_in_date,
            "check_out_date": booking_object.check_out_date,
            "total_price": booking_object.total_price,
            "comment": booking_object.comment,
            "number_of_guests": booking_object.number_of_guests,
            "created_at": booking_object.created_at,
            "updated_at": booking_object.updated_at,
        }

        serializer = self._booking_serializer(data=booking_data)

        if serializer.is_valid():
            return booking_data

        raise BookingSerializerException(serializer.errors)

    def delete_booking(self, code_booking):
        try:
            booking_obj = self._booking_model.objects.get(code_booking=code_booking)
        except self._booking_model.DoesNotExist:
            raise BookingNotFoundException()

        booking_obj.delete()
