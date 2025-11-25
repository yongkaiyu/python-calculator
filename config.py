# config.py
import os

# Get configuration from environment variables
API_KEY = os.getenv('API_KEY', 'test-api-key-12345')
DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///local.db')
DEBUG_MODE = os.getenv('DEBUG_MODE', 'true').lower() == 'true'