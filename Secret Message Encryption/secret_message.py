from tkinter import *
from tkinter import messagebox
import base64
import os


def decrypt():
    print("")
    
def encrypt():
    password=sode.get()
    
    if password=="1234":
        screen1=Toplevel(screen)
        screen1.title("encryption")
        screen1.geometry("400x200")
        

def main_screen():
    
    global screen
    global sode
    global text1
        
    screen=Tk()
    screen.geometry("375x398")
    
    #icon
    #! image_icon=PhotoImage(file="keys.png")
    #! screen.iconphptp(False,image_icon)
    screen.title("PctApp")
    
    def reset(): 
        sode.set("")
        text1.delete(1.0,END)
    
    Label(text="Enter text for encryption ans decryption", fg="black", font=("calbri", 13)).place(x=10, y=10)
    text1=Text(font="Robote 20", bg="white", relief=GROOVE, wrap=WORD, bd=0)
    text1.place(x=10, y=50, width=355, height=100)
    
    Label(text="Enter secret key for encryption ans decryption", fg="black", font=("calibri", 13)).place(x=10, y=170)
    
    sode=StringVar()
    Entry(textvariable=sode, width=19, bd=0, font=("arial",25),show="*").place(x=10,y=200)
    
    Button(text="ENCRYPT", height="2", width=23, bg="#ed3833", fg="white", bd=0, command=encrypt).place(x=10, y=250)
    Button(text="DECRYPT", height="2", width=23, bg="#00bd56", fg="white", bd=0, command=decrypt).place(x=200,y=250)
    Button(text="RESET", height="2", width=50, bg="#1089ff", fg="white", bd=0, command=reset).place(x=10,y=300)
    
    screen.mainloop()
    
main_screen()