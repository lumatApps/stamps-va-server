import base64
import json
import functions_framework
import logging
from firebase_admin import initialize_app, firestore
from google.cloud.logging import Client
from google.cloud import storage
from firebase_utils import save_to_firestore
from load_from_gcs import load_from_gcs

# Initialize the Firebase app if it hasn't been initialized
initialize_app()
db = firestore.client()

# Instantiate a Cloud Logging client and set up logging
client = Client()
client.setup_logging()

@functions_framework.cloud_event
def update_stamps(cloud_event):
    """Main function to update stamps."""
    try:
        # Configuration
        bucket_name = 'stamps-va'
        file_name = 'stamps-va.json'
        
        # Load data from Google Cloud Storage
        logging.info(f"Loading data from bucket: {bucket_name}, file: {file_name}")
        data = load_from_gcs(bucket_name, file_name)
        
        # Save data to Firestore
        logging.info("Saving data to Firestore")
        save_to_firestore(db, data)
        
        logging.info("Process completed successfully.")
        return "Process completed successfully.", 200
    except FileNotFoundError as e:
        logging.error(f"File not found: {e}")
        return f"Error: File not found - {str(e)}", 404
    except json.JSONDecodeError as e:
        logging.error(f"Invalid JSON data: {e}")
        return f"Error: Invalid JSON data - {str(e)}", 400
    except Exception as e:
        logging.error(f"Error processing stamps: {e}")
        return f"Error: {str(e)}", 500
