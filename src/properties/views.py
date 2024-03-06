from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import PropertySerializer
from .models import Property

from drf_yasg.utils import swagger_auto_schema

from .exceptions import PropertySerializerException

from .repositories import PropertyRepository


class PropertyListCreateView(APIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self._repository = PropertyRepository(
            property_model=Property,
            property_serializer=PropertySerializer,
        )
    @swagger_auto_schema(
        operation_description="Get all properties",
        responses={200: PropertySerializer(many=True)},
    )
    def get(self, request):
        response = self._repository.get_all_properties()

        return Response(response, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_description="Create a new property",
        request_body=PropertySerializer,
        responses={201: PropertySerializer()},
    )
    def post(self, request):

        response = self._repository.create_property(data=request.data)

        return Response(response, status=status.HTTP_201_CREATED)


class PropertyDetailView(APIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._repository = PropertyRepository(
            property_model=Property,
            property_serializer=PropertySerializer,
        )

    @swagger_auto_schema(
        operation_description="Get a property by its cod_property",
        responses={200: PropertySerializer()},
    )
    def get(self, request, pk):
        response = self._repository.get_property_by_cod_property(
            cod_property=pk
        )
        return Response(response, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_description="Update a property by its cod_property",
        request_body=PropertySerializer,
        responses={200: PropertySerializer()},
    )
    def put(self, request, pk):
        response = self._repository.update_property(cod_property=pk, data=request.data)

        return Response(response, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_description="Delete a property by its cod_property",
        responses={204: "No Content"},
    )
    def delete(self, request, pk):

        self._repository.delete_property(cod_property=pk)

        return Response(status=status.HTTP_204_NO_CONTENT)
