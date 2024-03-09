from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Booking

from .serializers import BookingSerializer
from .repositories import BookingRepository

from drf_yasg.utils import swagger_auto_schema


class BookingsListCreateView(APIView):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self._repository = BookingRepository(
            booking_model=Booking,
            booking_serializer=BookingSerializer
        )

    @swagger_auto_schema(
        operation_description="Get all bookings",
        responses={200: BookingSerializer(many=True)},
    )
    def get(self, request):
        response = self._repository.get_all_bookings()
        return Response(response, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_description="Create a new booking",
        request_body=BookingSerializer,
        responses={201: BookingSerializer()},
    )
    def post(self, request):
        response = self._repository.create_booking(data=request.data)

        return Response(response, status=status.HTTP_201_CREATED)


class BookingsDetailView(APIView):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self._repository = BookingRepository(
            booking_model=Booking,
            booking_serializer=BookingSerializer
        )

    @swagger_auto_schema(
        operation_description="Get a booking by its id",
        responses={200: BookingSerializer()},
    )
    def get(self, request, pk):
        booking = self._repository.get_booking_by_id(code_booking=pk)
        return Response(booking, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_description="Delete a booking by its id",
        responses={204: "No content"},
    )
    def delete(self, request, pk):
        self._repository.delete_booking(code_booking=pk)
        return Response(status=status.HTTP_204_NO_CONTENT)
