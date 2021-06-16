import cv2
import numpy as np
import face_recognition
import os
import pyttsx3 as txtspch
from datetime import datetime
import random


def face_rec():
    path = 'Authorized'
    images = []
    classNames = []
    myList = os.listdir(path)

    for cl in myList:
        curImage = cv2.imread(f'{path}/{cl}')
        images.append(curImage)
        classNames.append(os.path.splitext(cl)[0])

    def access_list(name):
        with open('Access_Register.txt', 'r+') as f:
            access_data = f.readlines()
            name_list = []
            for line in access_data:
                entry = line.split(',')
                name_list.append(entry[0])
            if name not in name_list:
                now = datetime.now()
                dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
                f.writelines(f'\n{name},{dt_string}')

    def findEncodings(images):
        encodeList = []
        for img in images:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            encode = face_recognition.face_encodings(img)[0]
            encodeList.append(encode)
        return encodeList

    encodeListKnown = findEncodings(images)

    engine = txtspch.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 180)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)

    def talk(text):
        engine.say(text)
        engine.runAndWait()

    talk('please step infront of the camera and lower your mask')
    print('encoding complete')
    cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)

    while True:
        success, img = cap.read()
        imgS = cv2.resize(img, (0,0), None, 0.25, 0.25)
        imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

        facesCurFrame = face_recognition.face_locations(imgS)
        encodeCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

        for encodeFace, faceLoc in zip(encodeCurFrame, facesCurFrame):
            matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
            faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
            matchIndex = np.argmin(faceDis)

            if min(faceDis) < 0.4:
                print(faceDis)
                name = classNames[matchIndex].lower()
                talk(f'Access granted, hello {name}, put your mask on')
                now = datetime.now()
                dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
                access_list(name + str(random.randint(1, 1000)))
                filename_path = "AccessGranted/" + str(name) + str(random.randint(1, 1000)) + ".jpg"
                cv2.imwrite(filename_path, img=imgS)
                return True

            else:
                talk('Unknown person, access denied')
                print('Unknown person, access denied')
                print(faceDis)
                now = datetime.now()
                dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
                access_list('Unknown user' + str(random.randint(1, 1000)))
                filename_path = "AccessDenied/" + "Unknown" + str(random.randint(1, 1000)) + ".jpg"
                cv2.imwrite(filename_path, img=imgS)
                return False
            cv2.destroyAllWindows()
            break

        cv2.imshow('Webcam', img)
        cv2.waitKey(1)

face_rec()




