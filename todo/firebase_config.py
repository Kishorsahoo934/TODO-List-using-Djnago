import os
import firebase_admin
from firebase_admin import credentials, db
from django.conf import settings

# Initialize Firebase only once
if not firebase_admin._apps:
    cred = credentials.Certificate(
        os.path.join(settings.BASE_DIR, 'chromacart-fo6vc-firebase-adminsdk-fbsvc-4d9f9ab960.json')
    )
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://chromacart-fo6vc-default-rtdb.firebaseio.com'
    })

def get_todo_ref():
    return db.reference('todos')
