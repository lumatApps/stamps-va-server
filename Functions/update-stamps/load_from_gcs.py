from google.cloud import storage
import json

def load_from_gcs(bucket_name, file_name):
    """Load JSON data from a Google Cloud Storage bucket"""
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(file_name)
    # Ensure compatibility and proper error handling
    data = json.loads(blob.download_as_bytes().decode('utf-8'))
    return data
