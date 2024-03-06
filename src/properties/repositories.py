from properties.models import Property

from properties.serializers import PropertySerializer

from properties.exceptions import (
    PropertyNotFoundException,
    PropertySerializerException,
    PropertyAlreadyExistsException,
)

from uuid import uuid4


class PropertyRepository:
    def __init__(self, property_model, property_serializer):
        self._property = property_model
        self._serializer = property_serializer

    def get_all_properties(self):

        properties = self._property.objects.all()

        serializer = self._serializer(properties, many=True)

        return serializer.data

    def create_property(self, data):
        serializer = self._serializer(data=data)
        if serializer.is_valid():
            cod_property = uuid4()

            property_object = self._property(
                **serializer.validated_data,
                cod_property=cod_property,
            )
            property_object.save()

            return serializer.data

        raise PropertySerializerException(serializer.errors)

    def get_property_by_cod_property(self, cod_property):

        try:
            property_object = self._property.objects.get(cod_property=cod_property)
        except self._property.DoesNotExist:
            raise PropertyNotFoundException()

        serializer = self._serializer(data=property_object.__dict__)

        if serializer.is_valid():
            property_data = {
                **serializer.validated_data,
                "cod_property": cod_property,
            }

            return property_data

        raise PropertySerializerException(serializer.errors)

    def update_property(self, cod_property, data):
        try:
            self._property.objects.get(cod_property=cod_property)
        except self._property.DoesNotExist:
            raise PropertyNotFoundException()

        serializer = self._serializer(data=data)

        if serializer.is_valid():
            serializer_data = serializer.validated_data

            property_object = self._property.objects.filter(cod_property=cod_property)
            property_object.update(**serializer_data)
            property_object[0].save()

            return serializer_data

        raise PropertySerializerException(serializer.errors)

    def delete_property(self, cod_property):
        try:
            property_obj = self._property.objects.get(cod_property=cod_property)
        except self._property.DoesNotExist:
            raise PropertyNotFoundException

        property_obj.delete()
