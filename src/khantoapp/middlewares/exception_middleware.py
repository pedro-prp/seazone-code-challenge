from properties.exceptions import (
    PropertyNotFoundException,
    PropertyAlreadyExistsException,
    PropertySerializerException,
)

from advertisements.exceptions import (
    AdvertisementsNotFoundException,
    AdvertisementSerializerException,
)

from bookings.exceptions import (
    BookingNotFoundException,
    BookingCheckoutPreCheckinException,
    BookingSerializerException,
)

from django.http import JsonResponse, HttpResponseServerError

from rest_framework import status


class ExceptionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request, *args, **kwargs):
        response = self.get_response(request)
        return response

    def process_exception(self, request, exception):
        serializer_errors = getattr(exception, "serializer_errors", None)

        response_dict = {
            PropertySerializerException: JsonResponse(
                {"message": "Invalid data", "errors": serializer_errors},
                status=status.HTTP_400_BAD_REQUEST,
            ),
            PropertyAlreadyExistsException: JsonResponse(
                {"message": "Property already exists"},
                status=status.HTTP_400_BAD_REQUEST,
            ),
            PropertyNotFoundException: JsonResponse(
                {"message": "Property not found"},
                status=status.HTTP_404_NOT_FOUND,
            ),
            AdvertisementSerializerException: JsonResponse(
                {"message": "Invalid data", "errors": serializer_errors},
                status=status.HTTP_400_BAD_REQUEST,
            ),
            AdvertisementsNotFoundException: JsonResponse(
                {"message": "Advertisement not found"},
                status=status.HTTP_404_NOT_FOUND,
            ),
            BookingSerializerException: JsonResponse(
                {"message": "Invalid data", "errors": serializer_errors},
                status=status.HTTP_400_BAD_REQUEST,
            ),
            BookingNotFoundException: JsonResponse(
                {"message": "Booking not found"},
                status=status.HTTP_404_NOT_FOUND,
            ),
            BookingCheckoutPreCheckinException: JsonResponse(
                {"message": "Checkout date is before checkin date"},
                status=status.HTTP_400_BAD_REQUEST,
            ),
        }

        return response_dict.get(exception.__class__, HttpResponseServerError())
