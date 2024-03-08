class BookingNotFound(Exception):
    pass


class BookingSerializerException(Exception):
    def __init__(self, serializer_errors):
        self.serializer_errors = serializer_errors


class BookingCheckoutPreCheckinException(Exception):
    pass
