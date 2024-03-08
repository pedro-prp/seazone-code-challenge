from advertisements.exceptions import (
    AdvertisementsNotFound,
    AdvertisementSerializerException,
)

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
            raise AdvertisementsNotFound()

        serializer = self._advertisement_serializer(data=advertisement_object.__dict__)

        if serializer.is_valid():
            advertisement_data = {
                **serializer.validated_data,
                "id_advertisement": id_advertisement,
            }

            return advertisement_data

        raise AdvertisementSerializerException(serializer.errors)

    def update_advertisement(self, id_advertisement, data):
        try:
            self._advertisement_model.objects.get(
                id_advertisement=id_advertisement,
            )
        except self._advertisement_model.DoesNotExist:
            raise AdvertisementsNotFound()

        serializer = self._advertisement_serializer(data=data)

        if serializer.is_valid():
            advertisement_data = serializer.validated_data

            advertisement_object = self._advertisement_model.objects.get(id_advertisement=id_advertisement)
            advertisement_object.update(**advertisement_data)
            advertisement_object[0].save()

            return serializer.data

        raise AdvertisementSerializerException(serializer.errors)

    def delete_advertisement(self, id_advertisement):
        try:
            advertisement_obj = self._advertisement_model.objects.get(id_advertisement=id_advertisement)
        except self._advertisement_model.DoesNotExist:
            raise AdvertisementsNotFound()

        advertisement_obj.delete()
