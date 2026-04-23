#!/bin/bash

# Set environment variables
export DJANGO_SETTINGS_MODULE=music_club.settings
export PYTHONPATH=$PYTHONPATH:$PWD

# Collect static files
python manage.py collectstatic --noinput

# Run migrations
python manage.py migrate --noinput

# Start the server
python manage.py runserver 0.0.0.0:$PORT
