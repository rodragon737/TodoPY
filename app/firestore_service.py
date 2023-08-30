import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# cred = credentials.Certificate('./user-project-secretgcloud.json')
# firebase_admin.initialize_app(cred)

##
credential = credentials.ApplicationDefault()
firebase_admin.initialize_app(credential)

db = firestore.client()

def get_users():
    return db.collection('users').get()

def get_todos():
    return db.collection('users').document(user_id).collection('todos').get()