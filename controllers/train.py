# -*- coding: utf-8 -*-
import numpy
import cv2
def index():
    img_array = []
    label_array = []
    cascade = cv2.CascadeClassifier("https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_frontalface_alt.xml")
    recognizer = cv2.createLBPHFaceRecognizer()
    for row in db(db.faces.id > 0).select():
        rtn = row
        img = cv2.imread(rtn.file, 0)
        faces = face_cascade.detectMultiScale(img, 1.3, 5)
        for (x,y,w,h) in faces:
            img_array.append(img[y: y + h, x: x + w])
            label_array.append(rtn.user_id)
    recognizer.train(img_array, label_array)
    recognizer.save("trained_recognizer.xml")
    return response.download("trained_recognizer.xml")
