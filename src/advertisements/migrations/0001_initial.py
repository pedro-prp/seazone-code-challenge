# Generated by Django 5.0.3 on 2024-03-06 21:37

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('properties', '0002_remove_property_id_alter_property_cod_property'),
    ]

    operations = [
        migrations.CreateModel(
            name='Advertisement',
            fields=[
                ('id_advertisement', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('platform_name', models.CharField(max_length=100)),
                ('platform_fee', models.DecimalField(decimal_places=2, max_digits=10)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='advertisements', to='properties.property')),
            ],
        ),
    ]
