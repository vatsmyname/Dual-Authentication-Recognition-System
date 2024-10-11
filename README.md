# Dual Authentication Recognition System

The Dual Authentication Recognition System implements a two-step authentication process involving face recognition followed by hand sign recognition. The system is designed to grant or deny access based on whether the recognized face and hand sign match the enrolled user data.

## Features

1. **Face Recognition:** Utilizes computer vision algorithms to identify and verify users based on facial features.
2. **Hand Sign Recognition:** Captures and analyzes hand signs to ensure the user presents a valid sign for access.
3. **Access Control:** Grants or denies access based on the match between recognized face and hand sign.

## Instructions
1. **Install Required Packages:** After cloning the repository, navigate to the project directory and install the necessary dependencies:
```bash
pip install -r requirements.txt
```
2. **Upload Face Images:** Place the images of the faces you want to recognize in the pictures folder. Ensure that the file name of each image matches the name of the user. The system will automatically extract the user’s name from the image file name.
3. **Set Hand Gestures:** Define the passwords or hand gestures for each user in the main.py file. This can be done by updating the dictionary with the corresponding hand signs.
4. **Hand Gesture Training:** The system is trained on a specific dataset of hand gestures. Each user will use one of these trained gestures as their password for access.

## Usage
To utilize the recognition system, follow these commands based on the module you wish to run: 
1. To run the face recognition module, navigate to the system directory and execute:
```bash
python recog.py
```
2. For the hand sign gesture recognition module, change into the system directory and run:
```bash
python hand.py
```
3. To run the entire recognition system, simply navigate to the system directory and execute:
```bash
python main.py
```
These commands will allow you to access the specific functionalities of the recognition system seamlessly.


