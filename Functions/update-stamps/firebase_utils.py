from firebase_admin import firestore

def save_to_firestore(db, data):
    for stamp_id, stamp_info in data.items():
        # Create or get a reference to the document for the stamp
        stamp_ref = db.collection('stamps').document(stamp_id)
        
        # Prepare the stamp data
        stamp_data = {
            "id": stamp_info['id'],
            "name": stamp_info['name'],
            "coordinates": firestore.GeoPoint(stamp_info['coordinates']['latitude'], stamp_info['coordinates']['longitude']),
            "type": stamp_info['type'],
            "icon": stamp_info['icon'],
            "notes": stamp_info['notes'],
            "secondaryIdentifier": stamp_info['secondaryIdentifier']
        }
        
        # Update the stamp document with the data
        stamp_ref.set(stamp_data)
