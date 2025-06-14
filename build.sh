#!/usr/bin/env bash
    # exit on error
    set -o errexit
    
    # Install our dependencies
    pip install -r requirements.txt
    
    # Run our "shipping" command for static files
    python manage.py collectstatic --no-input
    
    # Run our database "construction" plan
    python manage.py migrate