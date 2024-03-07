class AdvertisementsNotFound(Exception):
    pass


class AdvertisementSerializerException(Exception):
    def __init__(self, serializer_errors):
        self.serializer_errors = serializer_errors
