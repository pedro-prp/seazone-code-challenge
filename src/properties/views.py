from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import PropertySerializer
from .models import Property

from drf_yasg.utils import swagger_auto_schema


class PropertyListCreateView(APIView):
    @swagger_auto_schema(
        operation_description="Get all properties",
        responses={200: PropertySerializer(many=True)},
    )
    def get(self, request):
        properties = Property.objects.all()
        serializer = PropertySerializer(properties, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_description="Create a new property",
        request_body=PropertySerializer,
        responses={201: PropertySerializer()},
    )
    def post(self, request):
        serializer = PropertySerializer(data=request.data)
        if serializer.is_valid():

            existing_property = Property.objects.filter(
                cod_property=request.data["cod_property"]
            )

            if existing_property.exists():
                return Response(
                    {"message": "Property already exists"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PropertyDetailView(APIView):
    @swagger_auto_schema(
        operation_description="Get a property by its cod_property",
        responses={200: PropertySerializer()},
    )
    def get(self, request, pk):
        try:
            property = Property.objects.get(cod_property=pk)
        except Property.DoesNotExist:
            return Response(
                {"message": "Property not found"},
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = PropertySerializer(property)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_description="Update a property by its cod_property",
        request_body=PropertySerializer,
        responses={200: PropertySerializer()},
    )
    def put(self, request, pk):
        try:
            property = Property.objects.get(cod_property=pk)
        except Property.DoesNotExist:
            return Response(
                {"message": "Property not found"},
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = PropertySerializer(property, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Delete a property by its cod_property",
        responses={204: "No Content"},
    )
    def delete(self, request, pk):
        try:
            property = Property.objects.get(cod_property=pk)
        except Property.DoesNotExist:
            return Response(
                {"message": "Property not found"},
                status=status.HTTP_404_NOT_FOUND,
            )

        property.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
