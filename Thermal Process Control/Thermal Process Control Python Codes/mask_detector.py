import numpy as np
import keras
import keras.backend as k
from keras.layers import Conv2D,MaxPooling2D,SpatialDropout2D,Flatten,Dropout,Dense
from keras.models import Sequential,load_model
from keras.optimizers import Adam
from keras.preprocessing import image
import cv2
import datetime

def mask_detector():
    mymodel = load_model('mask_model.h5')

    cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    while cap.isOpened():
        _, img = cap.read()
        face = face_cascade.detectMultiScale(img, scaleFactor=1.1, minNeighbors=4)
        for (x, y, w, h) in face:
            face_img = img[y:y + h, x:x + w]
            cv2.imwrite('temp.jpg', face_img)
            test_image = image.load_img('temp.jpg', target_size=(150, 150, 3))
            test_image = image.img_to_array(test_image)
            test_image = np.expand_dims(test_image, axis=0)
            pred = mymodel.predict_classes(test_image)[0][0]

            if pred == 1:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                cv2.putText(img, 'NO MASK', ((x + w) // 2, y + h + 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                print('False')
                return False
            else:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
                cv2.putText(img, 'MASK', ((x + w) // 2, y + h + 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)
                print("True")
                return True

            datet = str(datetime.datetime.now())
            cv2.putText(img, datet, (400, 450), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

        cv2.imshow('mask detector', img)

        if cv2.waitKey(1) == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

