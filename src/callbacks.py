import windows
from other import *
from tkinter import messagebox

def newUser(window):
    window.clearWindow()
    windows.createUserPage(window)

def addUser(window):
    user_info = []
    for widget in window.top_frame.winfo_children():
        if widget.winfo_class() == 'Entry': user_info.append(widget.get())
    user_info.append(val_gender)
    user_info.append(val_ethnicity)

    msg = checkValidEntries(user_info)

    if msg: messagebox.showerror('Error', msg, icon=messagebox.WARNING)
    else: 
        window.clearWindow()
        saveUser(user_info[0] + " " + user_info[1], user_info)
        # add code to go to dashboard

def existingUser(window):
    window.clearWindow()
    windows.createExistingUserPage(window)    

def placeholder(window): print("placeholder function")

def getGender(*args): 
    global val_gender 
    val_gender = args[0]

def getEthnicity(*args): 
    global val_ethnicity
    val_ethnicity = args[0]