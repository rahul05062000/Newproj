#!/bin/bash

# Activate virtual environment
source /c/Users/rahul/Desktop/New/env/Scripts/activate

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput
