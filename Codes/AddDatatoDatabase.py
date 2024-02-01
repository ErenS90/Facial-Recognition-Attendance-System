import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("C:/Users/LEGION/OneDrive/Documents/Face Recognition Attendance System/Codes/serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://attendanceusingfacerecog-5d23c-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "321654":
        {
            "name": "Rishav Saha",
            "major": "CS AIML",
            "starting_year": 2024,
            "total_attendance": 7,
            "standing": "O",
            "year": 3,
            "last_attendance_time": "2024-1-22 00:19:47"
        },
    "852741":
        {
            "name": "Saurabh",
            "major": "CS",
            "starting_year": 2023,
            "total_attendance": 12,
            "standing": "A",
            "year": 1,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "963852":
        {
            "name": "Elon Musk",
            "major": "Physics",
            "starting_year": 2020,
            "total_attendance": 7,
            "standing": "O",
            "year": 2,
            "last_attendance_time": "2022-12-11 00:54:34"
        }
}

for key, value in data.items():
    ref.child(key).set(value)