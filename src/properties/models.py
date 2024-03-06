from django.db import models


class Property(models.Model):
    name = models.CharField(max_length=100)
    cod_property = models.CharField(max_length=100, primary_key=True)
    guests_limit = models.IntegerField()
    bath_quant = models.IntegerField()
    acceptable_pets = models.BooleanField()
    cleaning_fee = models.DecimalField(max_digits=10, decimal_places=2)
    activation_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
