import tkinter as tk
from tkinter import *
import os, cv2
import shutil
import csv
import numpy as np
from PIL import ImageTk, Image
import pandas as pd
import datetime
import time
import tkinter.font as font
import pyttsx3

# project module
import show_attendance
import takeImage
import trainImage
import automaticAttedance




def text_to_speech(user_text):
    engine = pyttsx3.init()
    engine.say(user_text)
    engine.runAndWait()


haarcasecade_path = "C:\\Users\\9yash\\Desktop\\github_reloaded\\haarcascade_frontalface_default.xml"
trainimagelabel_path = (
    "C:\\Users\\9yash\\Desktop\\github_reloaded\\TrainingImageLabel\\Trainner.yml"
)
trainimage_path = "C:\\Users\\9yash\\Desktop\\github_reloaded\\TrainingImage"
studentdetail_path = (
    "C:\\Users\\9yash\\Desktop\\github_reloaded\\StudentDetails\\studentdetails.csv"
)
attendance_path = "C:\\Users\\9yash\\Desktop\\github_reloaded\\Attendance"

#main window layout
window = Tk()
window.title("Face recognizer")
window.geometry("1500x800")
dialog_title = "QUIT"
dialog_text = "Are you sure want to close?"
window.configure(background="#e4f1fe")


# to destroy screen
def del_sc1():
    sc1.destroy()


# error message for name and mobile no.
def err_screen():
    global sc1
    sc1 = tk.Tk()
    sc1.geometry("400x110")
    sc1.iconbitmap("AMS.ico")
    sc1.title("Warning!!")
    sc1.configure(background="#e4f1fe")
    sc1.resizable(0, 0)
    tk.Label(
        sc1,
        text="Mobile Number & Name required!!!",
        fg="#dbd8e3",
        bg="#e4f1fe",
        font=("times", 20, " bold "),
    ).pack()
    tk.Button(
        sc1,
        text="OK",
        command=del_sc1,
        fg="#dbd8e3",
        bg="#e4f1fe",
        width=9,
        height=1,
        activebackground="Red",
        font=("times", 20, " bold "),
    ).place(x=110, y=50)

# check the input value as string or int 
def testVal(inStr, acttyp):
    if acttyp == "1":  # insert
        if not inStr.isdigit():
            return False
    return True


logo = Image.open("UI_Image/0001.png")
logo = logo.resize((50, 47), Image.ANTIALIAS)
logo1 = ImageTk.PhotoImage(logo)
titl = tk.Label(window, bg="#e4f1fe", relief=RIDGE, bd=10, font=("arial", 35))
titl.pack(fill=X)
l1 = tk.Label(window, image=logo1, bg="#e4f1fe",)
l1.place(x=470, y=10)

titl = tk.Label(
    window, text="FACE-FAST", bg="#e4f1fe", fg="#34495e", font=("bebas neue", 27),
)
titl.place(x=650, y=12)

a = tk.Label(
    window,
    text="Welcome to the Face Recognition Based\nTicketing system",
    bg="#e4f1fe",
    fg="#34495e",
    bd=10,
    font=("arial", 30),
)
a.pack()

ri = Image.open("UI_Image/register.png")
r = ImageTk.PhotoImage(ri)
label1 = Label(window, image=r)
label1.image = r
label1.place(x=200, y=270)

vi = Image.open("UI_Image/verifyy.png")
v = ImageTk.PhotoImage(vi)
label3 = Label(window, image=v)
label3.image = v
label3.place(x=650, y=270)

ai = Image.open("UI_Image/attendance.png")
a = ImageTk.PhotoImage(ai)
label2 = Label(window, image=a)
label2.image = a
label2.place(x=1000, y=270)




def TakeImageUI():
    ImageUI = Tk()
    ImageUI.title("Take User Image..")
    ImageUI.geometry("780x480")
    ImageUI.configure(background="#e4f1fe")
    ImageUI.resizable(0, 0)
    titl = tk.Label(ImageUI, bg="#e4f1fe", relief=RIDGE, bd=10, font=("arial", 35))
    titl.pack(fill=X)
    # image and title
    titl = tk.Label(
        ImageUI, text="Register Your Face", bg="#e4f1fe", fg="#34495e", font=("arial", 30),
    )
    titl.place(x=270, y=12)

    # heading
    a = tk.Label(
        ImageUI,
        text="Enter the Details",
        bg="#e4f1fe",
        fg="#34495e",
        bd=10,
        font=("arial", 24),
    )
    a.place(x=280, y=75)

    # Mobile no
    lbl1 = tk.Label(
        ImageUI,
        text="Mobile No",
        width=10,
        height=2,
        bg="#34495e",
        fg="#e4f1fe",
        bd=5,
        relief=RIDGE,
        font=("times new roman", 12),
    )
    lbl1.place(x=120, y=130)
    txt1 = tk.Entry(
        ImageUI,
        width=17,
        bd=5,
        validate="key",
        bg="#e4f1fe",
        fg="#34495e",
        relief=RIDGE,
        font=("times", 25, "bold"),
    )
    txt1.place(x=250, y=130)
    txt1["validatecommand"] = (txt1.register(testVal), "%P", "%d")

    # name
    lbl2 = tk.Label(
        ImageUI,
        text="Name",
        width=10,
        height=2,
        bg="#34495e",
        fg="#e4f1fe",
        bd=5,
        relief=RIDGE,
        font=("times new roman", 12),
    )
    lbl2.place(x=120, y=200)
    txt2 = tk.Entry( 
        ImageUI,
        width=17,
        bd=5,
        bg="#e4f1fe",
        fg="#34495e",
        relief=RIDGE,
        font=("times", 25, "bold"),
    )
    txt2.place(x=250, y=200)

    lbl3 = tk.Label(
        ImageUI,
        text="Notification",
        width=10,
        height=2,
        bg="#34495e",
        fg="#e4f1fe",
        bd=5,
        relief=RIDGE,
        font=("times new roman", 12),
    )
    lbl3.place(x=120, y=270)
    # txt3 = tk.Entry(
    #     ImageUI,
    #     width=17,
    #     bd=5,
    #     bg="#e4f1fe",
    #     fg="#dbd8e3",
    #     relief=RIDGE,
    #     font=("times", 25, "bold"),
    # )
    # txt3.place(x=250, y=270)

    message = tk.Label(
        ImageUI,
        text="",
        width=32,
        height=2,
        bd=5,
        bg="#34495e",
        fg="#e4f1fe",
        relief=RIDGE,
        font=("times", 12, "bold"),
    )
    message.place(x=250, y=270)

    #storing face data for given name and mobile no.
    def take_image():
        l1 = txt1.get()
        l2 = txt2.get()
       # l3 = txt3.get() input function
        takeImage.TakeImage(
            l1,
            l2,
            haarcasecade_path,
            trainimage_path,
            message,
            err_screen,
            text_to_speech,
        )
        txt1.delete(0, "end")
        txt2.delete(0, "end")

    # take Image button
    # image
    takeImg = tk.Button(
        ImageUI,
        text="Scan face",
        command=take_image,
        bd=10,
        font=("times new roman", 18),
        bg="#34495e",
        fg="#e4f1fe",
        height=2,
        width=12,
        relief=RIDGE,
    )
    takeImg.place(x=130, y=350)

    def train_image():
        trainImage.TrainImage(
            haarcasecade_path,
            trainimage_path,
            trainimagelabel_path,
            message,
            text_to_speech,
        )

    # train Image function call
    trainImg = tk.Button(
        ImageUI,
        text="Train Image",
        command=train_image,
        bd=10,
        font=("times new roman", 18),
        bg="#34495e",
        fg="#e4f1f2",
        height=2,
        width=12,
        relief=RIDGE,
    )
    trainImg.place(x=360, y=350)


r = tk.Button(
    window,
    text="Register a new passenger",
    command=TakeImageUI,
    bd=10,
    font=("times new roman", 16),
    bg="#34495e",
    fg="#e4f1f2",
    height=2,
    width=17,
)
r.place(x=200, y=520)

# Scan registered Image function call
def automatic_attedance():
    automaticAttedance.subjectChoose(text_to_speech)


r = tk.Button(
    window,
    text="Scan your Face",
    command=automatic_attedance,
    bd=10,
    font=("times new roman", 16),
    bg="#34495e",
    fg="#e4f1f2",
    height=2,
    width=17,
)
r.place(x=650, y=520)


def view_user_data():
    show_attendance.subjectchoose(text_to_speech)
def Attf():
        # sub = tx.get()
        # if sub == "":
        #     t = "Please enter the station name!!!"
        #     text_to_speech(t)
        # else:
            os.startfile(
                "c:\\Users\\9yash\\Desktop\\github_reloaded\\Attendance\\station.csv"
            )

r = tk.Button(
    window,
    text="View Records",
    command= Attf,
    bd=10,
    font=("times new roman", 16),
    bg="#34495e",
    fg="#e4f1fe",
    height=2,
    width=17,
)
r.place(x=1000, y=520)
r = tk.Button(
    window,
    text="EXIT",
    bd=10,
    command=quit,
    font=("times new roman", 16),
    bg="#34495e",
    fg="#e4f1fe",
    height=2,
    width=17,
)
r.place(x=650, y=660)

window.mainloop()
