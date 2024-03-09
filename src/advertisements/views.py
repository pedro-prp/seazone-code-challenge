from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Advertisement

from .serializers import AdvertisementSerializer
from .repositories import AdvertisementRepository

from drf_yasg.utils import swagger_auto_schema


class AdvertisementListCreateView(APIView):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self._repository = AdvertisementRepository(
            advertisement_model=Advertisement,
            advertisement_serializer=AdvertisementSerializer
        )

    @swagger_auto_schema(
        operation_description="Get all advertisements",
        responses={200: AdvertisementSerializer(many=True)},
    )
    def get(self, request):
        response = self._repository.get_all_advertisements()
        return Response(response, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_description="Create a new advertisement",
        request_body=AdvertisementSerializer,
        responses={201: AdvertisementSerializer()},
    )
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

    @swagger_auto_schema(
        operation_description="Get an advertisement by its id",
        responses={200: AdvertisementSerializer()},
    )
    def get(self, request, pk):
        advertisement = self._repository.get_advertisement_by_id(pk)
        return Response(advertisement, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_description="Update an advertisement by its id",
        request_body=AdvertisementSerializer,
        responses={200: AdvertisementSerializer()},
    )
    def put(self, request, pk):
        response = self._repository.update_advertisement(pk, request.data)
        return Response(response, status=status.HTTP_200_OK)
