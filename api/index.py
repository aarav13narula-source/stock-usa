"""Vercel serverless entry point — replaces passenger_wsgi.py and gunicorn_start.sh"""
import sys
import os

# Make project root importable
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import create_app

# Vercel looks for a variable named `app` or `handler`
app = create_app()
handler = app
