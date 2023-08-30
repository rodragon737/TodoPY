import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# cred = credentials.Certificate('./flask-rrosales-firebase-adminsdk-wmyr7-35dd467f30.json')
# firebase_admin.initialize_app(cred)

credential = credentials.ApplicationDefault()
firebase_admin.initialize_app(credential)

db = firestore.client()

def get_users():
    db.collection('users').get()