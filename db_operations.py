import logging
from datetime import datetime

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate('key.json')
firebase_admin.initialize_app(cred,
                            {'databaseURL': 'https://missingchild-e630d.firebaseio.com/'}  # nopep8
)
print('Connection to DB established')


def add_to_pending(image_encoding, caseId, name, father_name, age, mob,email):
    unique_id = caseId + "@" + mob;
    try:
        root = db.reference('stationID')
        new_user = root.child('ABC123').child('pending').child(unique_id).set(
            {'encoded': image_encoding,
             'caseId' : caseId,
             'name' : name,
             'father_name':father_name,
             'age':age,
             'mobile':mob,
             'email' :email
             })
        return True
    except Exception as e:
        logging.error("Insertion Error" + str(e))
        return False


def add_to_confirmed(unique_key,caseId, name, father_name, age, mobile, email, location, image):
    try:
        date = str(datetime.now())
        root = db.reference('stationID')
        new_user = root.child('ABC123').child('confirmed').child(unique_key).set(
            {'caseId': caseId,
             'name': name,
             'father_name': father_name,
             'age': age,
             'mobile': mobile,
             'email' : email,
             'image': image,
             'location': location,
             'date': date
             })
        return True
    except Exception as e:
        logging.error("Insertion Error" + str(e))
        return False


def fetch_pending_cases(station_id='ABC123'):
    result = db.reference('stationID').child(station_id).child('pending').get()
    return result

def fetch_pending_cases_by_unique_id(unique_id,station_id='ABC123'):
    result = db.reference('stationID').child(station_id).child('pending').child(unique_id).get()
    return result

def fetch_confirmed_cases(station_id='ABC123'):
    result = db.reference('stationID').child(station_id).child('confirmed').get()
    return result


def delete_from_pending(unique_key, station_id='ABC123'):
    try:
        ref = db.reference('stationID').child(station_id).child('pending').child(unique_key).delete()  # nopep8
    except Exception as e:
        print("key = " + unique_key)
        print(str(e))
