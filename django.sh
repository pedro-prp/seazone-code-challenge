#!/bin/bash
echo "Creating Migrations..."
python ./src/manage.py makemigrations
python ./src/manage.py makemigrations properties
python ./src/manage.py makemigrations advertisements
python ./src/manage.py makemigrations bookings
echo "===================================="

echo "Starting Migrations..."
python ./src/manage.py migrate
python ./src/manage.py migrate properties
python ./src/manage.py migrate advertisements
python ./src/manage.py migrate bookings
echo "===================================="

echo "Checking if Super User Exists..."
user_exists=$(python ./src/manage.py shell -i python -c "from django.contrib.auth.models import User; print(User.objects.filter(username='admin').exists())")

if [ "$user_exists" = "False" ]; then
    echo "Creating Super User..."
    python ./src/manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'admin')"
else
    echo "Super User 'admin' already exists, skipping creation."
fi
echo "===================================="

echo "Seeding Database..."
python ./src/manage.py loaddata ./src/properties/fixtures/properties.json
python ./src/manage.py loaddata ./src/advertisements/fixtures/advertisements.json
python ./src/manage.py loaddata ./src/bookings/fixtures/bookings.json
echo "===================================="

echo "Starting Server..."
python ./src/manage.py runserver 0.0.0.0:8000
