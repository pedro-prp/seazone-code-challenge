#!/bin/bash
echo "Creating Migrations..."
python ./src/manage.py makemigrations
echo ====================================

echo "Starting Migrations..."
python ./src/manage.py migrate
echo ====================================

echo "Starting Server..."
python ./src/manage.py runserver 0.0.0.0:8000