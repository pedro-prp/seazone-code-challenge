from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Advertisement

from .serializers import AdvertisementSerializer
from .repositories import AdvertisementRepository


class AdvertisementListCreateView(APIView):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self._repository = AdvertisementRepository(
            advertisement_model=Advertisement,
            advertisement_serializer=AdvertisementSerializer
        )

    def get(self, request):
        response = self._repository.get_all_advertisements()
        return Response(response, status=status.HTTP_200_OK)

    def post(self, request):
        response = self._repository.create_advertisement(data=request.data)

        return Response(response, status=status.HTTP_201_CREATED)


class AdvertisementDetailView(APIView):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self._repository = AdvertisementRepository(
            advertisement_model=Advertisement,
            advertisement_serializer=AdvertisementSerializer
        )

    def get(self, request, pk):
        advertisement = self._repository.get_advertisement_by_id(pk)
        return Response(advertisement, status=status.HTTP_200_OK)

    def put(self, request, pk):
        response = self._repository.update_advertisement(pk, request.data)
        return Response(response, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        self._repository.delete_advertisement(pk)
        return Response(status=status.HTTP_204_NO_CONTENT)
