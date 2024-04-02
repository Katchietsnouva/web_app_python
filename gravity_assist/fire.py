import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate('fig.json')


firebase_admin.initialize_app(cred,{'databaseURL':'https://plan1-e1ebc-default-rtdb.europe-west1.firebasedatabase.app/'})

ref = db.reference('parking_web_app_db/')
user_ref = ref.child('users')
user_ref.set({
    '1st user ':{
        'name': 'a',
        'number':11,
        'id': 'a1'
    },
    '2nd user':{
        'name': 'b',
        'number':31,
        'id': 'a5'
    }
})
