import csv
import imp
import os, cv2
import tkinter
import numpy as np
import pandas as pd
import datetime
import time
from tkinter import messagebox, Tk



# take Image of user
def TakeImage(l1, l2, haarcasecade_path, trainimage_path, message, err_screen,text_to_speech):
    if (l1 == "") and (l2==""):
        t='Please Enter the your Mobile Number and Name.'
        # text_to_speech(t)
        Tk().withdraw()
        show_method = getattr(messagebox, 'show{}'.format('info'))
        show_method('ALERT', t)
       # print(t)
    elif l1=='':
        t='Please Enter the your Enrollment Number.'
        # text_to_speech(t)
        Tk().withdraw()
        show_method = getattr(messagebox, 'show{}'.format('info'))
        show_method('ALERT', t)
        print(t)
    elif l2 == "":
        t='Please Enter the your Name.'
        Tk().withdraw()
        show_method = getattr(messagebox, 'show{}'.format('info'))
        show_method('ALERT', t)
        print(t)
        # text_to_speech(t)
    else:
        try:
            cam = cv2.VideoCapture(0)
            detector = cv2.CascadeClassifier(haarcasecade_path)
            mobile = l1
            Name = l2
            sampleNum = 0
            directory = mobile + "_" + Name
            path = os.path.join(trainimage_path, directory)
            os.mkdir(path)
            while True:
                ret, img = cam.read()
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                faces = detector.detectMultiScale(gray, 1.3, 5)
                for (x, y, w, h) in faces:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                    sampleNum = sampleNum + 1
                    cv2.imwrite(
                        f"{path}\ "
                        + Name
                        + "_"
                        + mobile
                        + "_"
                        + str(sampleNum)
                        + ".jpg",
                        gray[y : y + h, x : x + w],
                    )
                    cv2.imshow("Frame", img)
                if cv2.waitKey(1) & 0xFF == ord("q"):
                    break
                elif sampleNum > 50:
                    break
            cam.release()
            cv2.destroyAllWindows()
            row = [mobile, Name]
            with open(
                "C:\\Users\\9yash\\Desktop\\github_reloaded\\StudentDetails\\studentdetails.csv",
                "a+",
            ) as csvFile:
                writer = csv.writer(csvFile, delimiter=",")
                writer.writerow(row)
                csvFile.close()
            res = "Images Saved for mobile No:" + mobile + " Name:" + Name
            message.configure(text=res)
            text_to_speech(res)
        except FileExistsError as F:
            F = "Student Data already exists"
            text_to_speech(F)
