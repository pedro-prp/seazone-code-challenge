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
            advertisement_object = self._advertisement_model(
                **serializer.validated_data,
            )
            advertisement_object.save()
            return serializer.data
        return serializer.errors

    def get_advertisement_by_id(self, pk):
        serializer = self._advertisement_model.objects.get(pk=pk)
        return self._advertisement_serializer(serializer).data

    def update_advertisement(self, pk, data):
        serializer = self._advertisement_serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return serializer.data
        return serializer.errors

    def delete_advertisement(self, pk):
        advertisement = self._advertisement_model.objects.get(pk=pk)
        advertisement.delete()
        return None
