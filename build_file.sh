#!/bin/bash

# Use specific Python version
PYTHON=python3.9

# Install dependencies
echo "Installing dependencies..."
$PYTHON -m pip install -r requirements.txt

# Collect static files
echo "Collecting static files..."
$PYTHON manage.py collectstatic --noinput
