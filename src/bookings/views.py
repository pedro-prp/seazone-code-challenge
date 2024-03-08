from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Booking

from .serializers import BookingSerializer
from .repositories import BookingRepository


class BookingsListCreateView(APIView):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self._repository = BookingRepository(
            booking_model=Booking,
            booking_serializer=BookingSerializer
        )

    def get(self, request):
        response = self._repository.get_all_bookings()
        return Response(response, status=status.HTTP_200_OK)

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

    def get(self, request, pk):
        booking = self._repository.get_booking_by_id(pk)
        return Response(booking, status=status.HTTP_200_OK)

    def put(self, request, pk):
        response = self._repository.update_booking(pk, request.data)
        return Response(response, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        self._repository.delete_booking(pk)
        return Response(status=status.HTTP_204_NO_CONTENT)
