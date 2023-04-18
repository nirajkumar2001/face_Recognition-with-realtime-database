
from firebase_admin import db
import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{


    'databaseURL': "https://faceattendancerealtime-db360-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "12111464":
        {
            "name": "Niraj Kumar",
            "major": "Computer Science",
            "starting_year": 2022,
            "total_attendance": 0,
            "standing": "A",
            "year": 1,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "12112511":
        {
            "name": "Akash Chaudhary",
            "major": "Artificial Intelligence",
            "starting_year": 2023,
            "total_attendance": 0,
            "standing": "B",
            "year": 1,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "12112432":
        {
            "name": "Shanmukh sai",
            "major": "Data base administrator",
            "starting_year": 2023,
            "total_attendance": 12,
            "standing": "D",
            "year": 1,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "12108334":
        {
            "name": "Shivani Singh",
            "major": "Artificial Intelligence",
            "starting_year": 2023,
            "total_attendance": 5,
            "standing": "C",
            "year": 1,
            "last_attendance_time": "2022-12-11 00:54:34"
        },

}

for key, value in data.items():
    ref.child(key).set(value)