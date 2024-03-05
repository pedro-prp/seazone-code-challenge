#!/bin/bash
echo "Creating Migrations..."
python ./src/manage.py makemigrations
python ./src/manage.py makemigrations properties
echo ====================================

echo "Starting Migrations..."
python ./src/manage.py migrate
python ./src/manage.py migrate properties
echo ====================================

echo "Starting Server..."
python ./src/manage.py runserver 0.0.0.0:8000
