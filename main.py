from recog import name, known_face_name
from hand import className

permission_dict = {
    "Person 1": "peace",
    "Person 2": "stop",
    "Person 3": "fist"
}

recognized_name = name
if recognized_name in known_face_name:
    print(f"Face recognized: {recognized_name}")
    
    recognized_gesture = className
    print(f"Gesture detected: {recognized_gesture}")
    if recognized_name in permission_dict:
        expected_gesture = permission_dict[recognized_name]
        if recognized_gesture == expected_gesture:
            print("Permission Granted")
        else:
            print("Permission Denied!")
    else:
        print("No permission rules found for this person!")
else:
    print("Permission Denied!")
