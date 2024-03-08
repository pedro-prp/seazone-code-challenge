from django.db import models
from django.utils import timezone

from properties.models import Property


class Advertisement(models.Model):
    id_advertisement = models.CharField(max_length=100, primary_key=True)
    property = models.ForeignKey(Property, related_name='advertisements', on_delete=models.CASCADE)
    platform_name = models.CharField(max_length=100)
    platform_fee = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.id_advertisement
