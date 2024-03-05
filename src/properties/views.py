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
