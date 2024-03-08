from django.http import HttpResponseServerError, JsonResponse

from rest_framework import status

from bookings.exceptions import (
    BookingSerializerException,
    BookingCheckoutPreCheckinException,
    BookingNotFound,
)


class ExceptionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request, *args, **kwargs):
        response = self.get_response(request)

        return response

    def process_exception(self, request, exception):
        serializer_errors = getattr(exception, "serializer_errors", None)

        response_dict = {
            BookingSerializerException: JsonResponse(
                {"message": "Invalid data", "errors": serializer_errors},
                status=status.HTTP_400_BAD_REQUEST,
            ),
            BookingNotFound: JsonResponse(
                {"message": "Booking not found"},
                status=status.HTTP_404_NOT_FOUND,
            ),
            BookingCheckoutPreCheckinException: JsonResponse(
                {"message": "Checkout date must be after checkin date"},
                status=status.HTTP_400_BAD_REQUEST,
            ),
        }

        return response_dict.get(exception.__class__, HttpResponseServerError())