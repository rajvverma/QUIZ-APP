#### Databse and login page #####

from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
import mysql.connector
import datetime
import random
import smtplib

#connect database to python
con=mysql.connector.connect(host="localhost",user="root",passwd="",database="mailinfo")
cursor=con.cursor()


root = Tk()
root.geometry("1525x785")
root.resizable(False, False)
root.title("QUIZ")

dt=datetime.datetime.now()
x = dt.strftime("%Y-%m-%d %H:%M:%S")

bg = ImageTk.PhotoImage(file="2.jpg")
bg_img = Label(root, image=bg).place(x=0, y=0, relwidth=1, relheight=1)
frame = Frame(root, borderwidth=8, bg="#abd6d6")
frame.pack(side=TOP, anchor="w", padx=120, pady=250)
root.attributes('-fullscreen',True)

l2 = Label(root, text="LOGIN", font=("Arial", 35, "bold"), bg="#65bff5")
l2.place(x=255, y=125)
root.overrideredirect(True)

u1 = Label(frame, text="Email ID  : ", font=("Arial", 15, "bold"), bg="#abd6d6")
p1 = Label(frame, text="OTP       : ", font=("Arial", 15, "bold"), bg="#abd6d6")
u1.grid(padx=10, column=0)
p1.grid(padx=10, row=1, column=0)

user = StringVar()
password = StringVar()
userentry = Entry(frame, textvariable=user, font=("Arial", 18))
passentry = Entry(frame, textvariable=password, font=("Arial", 18, "bold"))
userentry.grid(row=0, column=1, pady=25, padx=25)
passentry.grid(row=1, column=1, pady=25, padx=25)


lable=Label(root,text="Powered by",font=("Arial",10,"bold"),bg="white",fg="black").place(x=1180,y=25)
lable=Label(root,text="SSJ IT Solutions Pvt. Ltd. ",font=("Arial",14,"bold"),bg="white",fg="black").place(x=1220,y=60)

def send():
    global otp

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login('coolarunshishodia@gmail.com', "sjdzcvifchvgaktt")
        otp = random.randint(1000, 9999)
        otp = str(otp)
        msg = ("You have succesfully registered on QUIZER! \n Use the OTP given below to verify your email ID. " + otp)
        server.sendmail("coolarunshishodia@gmail.com", userentry.get(), msg)
        messagebox.showinfo("Send OTP via Email", f"OTP sent to {userentry.get()}")
        server.quit()

    except:
        messagebox.showinfo("Send OTP via Email","Please enter the valid email address or check your internet connection")
        b3 = Button(root, text="Resend OTP", fg="white", bg="#77bdbd", relief=RAISED, font=("Arial", 12, "bold"),command=send)
        b3.place(x=185, y=530, anchor="w", relwidth=.08, relheight=.08)




def nextpage():
    con = mysql.connector.connect(host="localhost", user="root", passwd="", database="mailinfo")
    cursor = con.cursor()
    cursor.execute("INSERT INTO logindetails VALUES(%s,%s)", (userentry.get(),x))
    print("data updated")
    con.commit()
    con.close()
    root.destroy()
    import choice

# def email():
#     eid = userentry.get()
#     return

def login():
    if (passentry.get() == otp):
        nextpage()

    else:
        messagebox.showinfo("Error", "Please enter correct OTP")

b1 = Button(root, text="Get OTP", fg="white", bg="#77bdbd", relief=RAISED, font=("Arial", 12, "bold"), command=send)
b1.place(x=185, y=530, anchor="w", relwidth=.08, relheight=.08)

b2 = Button(root, text="LOGIN", fg="white", bg="#77bdbd", relief=RAISED, font=("Arial", 12, "bold"), command=login)
b2.place(x=390, y=530, anchor="w", relwidth=.08, relheight=.08)

Exitbtn = Button(root, text='EXIT',border=8, bg='red', fg='white',font=("Arial", 12, "bold"),relief=GROOVE, command=root.destroy)
Exitbtn.place(x=1450,y=753,anchor="ne",relwidth=.06,relheight=.06)





root.mainloop()
