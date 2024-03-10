from advertisements.exceptions import (
    AdvertisementsNotFoundException,
    AdvertisementSerializerException,
)

from properties.repositories import PropertyRepository
from properties.models import Property
from properties.serializers import PropertySerializer

from uuid import uuid4


class AdvertisementRepository:
    def __init__(self, advertisement_model, advertisement_serializer):
        self._advertisement_model = advertisement_model
        self._advertisement_serializer = advertisement_serializer

    def get_all_advertisements(self):
        advertisements = self._advertisement_model.objects.all()

        serializer = self._advertisement_serializer(advertisements, many=True)

        return serializer.data

    def create_advertisement(self, data):
        print("kjhfasjdflkjasl")
        serializer = self._advertisement_serializer(data=data)
        if serializer.is_valid():

            id_advertisement = uuid4()

            advertisement_object = self._advertisement_model(
                **serializer.validated_data,
                id_advertisement=id_advertisement,
            )
            advertisement_object.save()

            advertisement_data = serializer.data
            advertisement_data["id_advertisement"] = id_advertisement

            return advertisement_data

        raise AdvertisementSerializerException(serializer.errors)

    def get_advertisement_by_id(self, id_advertisement):
        try:
            advertisement_object = self._advertisement_model.objects.get(
                id_advertisement=id_advertisement,
            )
        except self._advertisement_model.DoesNotExist:
            raise AdvertisementsNotFoundException()

        advertisement_data = {
            "id_advertisement": advertisement_object.id_advertisement,
            "platform_fee": advertisement_object.platform_fee,
            "platform_name": advertisement_object.platform_name,
            "property": advertisement_object.property_id,
            "created_at": advertisement_object.created_at,
            "updated_at": advertisement_object.updated_at,
        }

        serializer = self._advertisement_serializer(data=advertisement_data)

        if serializer.is_valid():
            return advertisement_data

        raise AdvertisementSerializerException(serializer.errors)

    def update_advertisement(self, id_advertisement, data):
        try:
            self._advertisement_model.objects.get(
                id_advertisement=id_advertisement,
            )
        except self._advertisement_model.DoesNotExist:
            raise AdvertisementsNotFoundException()

        serializer = self._advertisement_serializer(data=data)

        if serializer.is_valid():
            serializer_data = serializer.data

            advertisement_object = self._advertisement_model.objects.filter(
                id_advertisement=id_advertisement
            )
            advertisement_object.update(**serializer_data)
            advertisement_object[0].save()

            return serializer_data

        raise AdvertisementSerializerException(serializer.errors)
