from django.db import models
from django.utils import timezone

from advertisements.models import Advertisement

from uuid import uuid4


class Booking(models.Model):
    code_booking = models.CharField(max_length=100, primary_key=True)
    advertisement = models.ForeignKey(Advertisement, related_name='reservations', on_delete=models.CASCADE)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    comment = models.TextField(blank=True)
    number_of_guests = models.IntegerField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.advertisement.property.name} - {self.check_in_date} - {self.check_out_date}'
