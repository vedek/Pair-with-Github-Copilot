from platform import python_branch


%python
%define function to call firebase authentication api with credentials
def firebase_auth(email, password):
    #import firebase_admin
    #from firebase_admin import credentials
    #from firebase_admin import auth
    #cred = credentials.Certificate('firebase-credentials.json')
    #default_app = firebase_admin.initialize_app(cred)
    #user = auth.create_user(email=email, password=password)
    #return user.uid
    return "test"

%python
%define function to check credentials against firebase
def check_credentials(email, password):
    #import firebase_admin
    #from firebase_admin import credentials
    #from firebase_admin import auth
    #cred = credentials.Certificate('firebase-credentials.json')
    #default_app = firebase_admin.initialize_app(cred)
    #user = auth.get_user_by_email(email)
    #return user.uid
    return "test"

%python
%define function to check if user is already registered
def check_user(email):
    #import firebase_admin
    #from firebase_admin import credentials
    #from firebase_admin import auth
    #cred = credentials.Certificate('firebase-credentials.json')
    #default_app = firebase_admin.initialize_app(cred)
    #user = auth.get_user_by_email(email)
    #return user.uid
    return "test"

%python
%define function to convert camera image to barcode string
def convert_image_to_barcode(image):
    #import pyzbar.pyzbar
    #decoded = pyzbar.pyzbar.decode(image)
    #return decoded[0].data.decode("utf-8")
    return "test"

%python
%define function to check if barcode is in database
def check_barcode(barcode):
    #import firebase_admin
    #from firebase_admin import credentials
    #from firebase_admin import firestore
    #cred = credentials.Certificate('firebase-credentials.json')

    #default_app = firebase_admin.initialize_app(cred)
    #db = firestore.client()

    #doc_ref = db.collection('barcodes').document(barcode)
    #doc = doc_ref.get()
    #return doc.exists
    return "test"

%python
%define function to add barcode to database
def add_barcode(barcode):
    #import firebase_admin
    #from firebase_admin import credentials
    #from firebase_admin import firestore
    #cred = credentials.Certificate('firebase-credentials.json')

    #default_app = firebase_admin.initialize_app(cred)
    #db = firestore.client()

    #doc_ref = db.collection('barcodes').document(barcode)
    #doc = doc_ref.get()
    #return doc.exists
    return "test"

    