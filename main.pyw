from time import sleep
from tkinter import *
import secrets
import string

class pwgenerator:
    global charset

    def passwordGenerator(length):
        return ''.join(secrets.choice(charset) for i in range(length))


root = Tk()
root.geometry("500x400")
root.title("Password Generator")
root.iconbitmap("icon.ico")

#Database and string variables
bg = root.cget('background')
data = open(f"saved/data.txt", "at")
password = StringVar(root)
length_pass = StringVar(root)
length_pass.set("Choose length")
length_list = [8, 9, 10, 11, 12, 13, 14, 15, 16]
charset = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
#Functions
def generatePass():
    global password
    global length_pass
    if length_pass.get() != "Choose length":
        ln = int(length_pass.get())
        ps = pwgenerator.passwordGenerator(ln)
        password.set(ps)
        CLEAR.config(state="normal")
        SAVE_PASS.config(state="normal")
    elif length_pass.get() == "Choose length":
        password.set("Please select length first!")

def savePass():
    PASSWORD = pw.get()
    data.write("\n" + PASSWORD)
def clear():
    password.set('')
    CLEAR.config(state="disabled")
    SAVE_PASS.config(state="disabled")

def blankSpace():
    Label(root, height=1).pack()


pw = Entry(root, state="readonly", textvariable=password)
GENERATOR = Button(root, text="Generate password", command=generatePass, anchor="center")
SAVE_PASS = Button(root, text="Save Password", state="disabled", command=savePass, anchor="center")
CLEAR = Button(root, text="Clear", command=clear,  state="disabled", anchor="center")
lengthMenu = OptionMenu(root, length_pass, *length_list)
blankSpace()
blankSpace()
pw.pack()
blankSpace()
GENERATOR.pack()
blankSpace()
SAVE_PASS.pack()
blankSpace()
CLEAR.pack()
blankSpace()
lengthMenu.pack()


root.mainloop()
