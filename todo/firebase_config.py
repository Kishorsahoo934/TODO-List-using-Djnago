import os
import json
import firebase_admin
from firebase_admin import credentials, db

# Initialize Firebase only once
if not firebase_admin._apps:
    # Load Firebase credentials from Render environment variable
    cred = credentials.Certificate(json.loads(os.environ['FIREBASE_CREDENTIALS']))
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://chromacart-fo6vc-default-rtdb.firebaseio.com'  # 🔥 your Firebase DB URL
    })

# Function to get a reference to the "todos" node
def get_todo_ref():
    return db.reference('todos')
