import google.cloud.logging
import logging
import os

def setup_logging():
    K_SERVICE = os.getenv('K_SERVICE')
    if K_SERVICE:
        client = google.cloud.logging.Client()
        client.setup_logging()
    else:
        logging.basicConfig(level=logging.INFO)