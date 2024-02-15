import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate('fig.json')


firebase_admin.initialize_app(cred,{}:'')

ref = db.reference('py/')
user_ref = ref.child('users')
user_ref.set({
    ''
})
