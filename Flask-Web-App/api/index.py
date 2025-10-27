from flask import Flask, send_from_directory
from website import create_app
from http.server import HTTPServer, BaseHTTPRequestHandler
import os

# Initialize Flask app
app = create_app()

# Handler for Vercel serverless function
def handler(request, response):
    # Set FLASK_ENV for development/production
    os.environ['FLASK_ENV'] = os.getenv('VERCEL_ENV', 'production')
    
    # Handle the request through Flask
    with app.request_context(request):
        return app.full_dispatch_request()

# Required for Vercel - handles all routes
def index(request):
    return handler(request, None)