from cProfile import label
from tkinter import *
from tkinter import ttk
import string
import random

# Create an instance of tkinter frame
win= Tk()

win.title('OTP')
# Set the size of the tkinter window
win.geometry("300x200")

frame = Frame(win)
frame.pack(side="top", expand=False, fill="both")


# create a Label widget
my_label = Label(win, text = "Show Verify code here",  bg='blue',font= ('Aerial 17 bold italic'))
my_label.pack()

def save_data():
    length=6
    randomstr = ''.join(random.choices(string.ascii_letters+string.digits,k=length))
    f = open("VerifyFile.txt", "w")
    f.write(randomstr)    
    f.close()
       
def show_msg():
    
    #open and read the file after the appending:
    f1 = open("VerifyFile.txt", "r")
    a= f1.read()   
    f1.close()    
    
    my_label.config(text = a, bg='blue', font= ('Aerial 17 bold italic'))

ttk.Button(frame, text= "Create VerifyCode", command=save_data).pack(pady= 5)
ttk.Button(frame, text= "Show VerifyCode", command=show_msg).pack(pady= 5)
win.mainloop()