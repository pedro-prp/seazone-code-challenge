from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import PropertySerializer
from .models import Property


class PropertyListCreateView(APIView):
    def get(self, request):
        properties = Property.objects.all()
        serializer = PropertySerializer(properties, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PropertySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PropertyDetailView(APIView):
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
