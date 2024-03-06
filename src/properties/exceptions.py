class PropertyNotFoundException(Exception):
    pass


class PropertyAlreadyExistsException(Exception):
    pass


class PropertySerializerException(Exception):
    def __init__(self, serializer_errors):
        self.serializer_errors = serializer_errors
