# -*- coding: utf-8 -*-
import cv2
import numpy as np
import os
def index():
    img_array = []
    label_array = []
    face_cascade = cv2.CascadeClassifier("https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_frontalface_alt.xml")
    recognizer = cv2.createLBPHFaceRecognizer()
    for row in db(db.faces.id > 0).select():
        rtn = row
        path=os.path.join(request.folder, 'uploads', rtn.file)
#         image = response.download(open(path, 'rb'), chunk_size=4096)
        img = cv2.imread(path, 0)
        img_array.append(img)
#         faces = face_cascade.detectMultiScale(img, 1.3, 5)
#         for (x,y,w,h) in faces:
#             img_array.append(img[y: y + h, x: x + w])
        label_array.append(rtn.user_id)
    recognizer.train(img_array, np.array(label_array))
    recognizer.save(os.path.join(request.folder, 'private', "trained_recognizer.xml"))
    return response.download("trained_recognizer.xml")
