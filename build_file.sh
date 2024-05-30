#!/bin/bash

# Activate virtual environment (if applicable)
source /path/to/your/virtualenv/bin/activate  # Replace /path/to/your/virtualenv with the actual path to your virtual environment

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput
