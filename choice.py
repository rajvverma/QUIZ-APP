##### choice #####
from tkinter import *
from PIL import ImageTk, Image

# from main import email

def nextpage():
    root1.destroy()
    import easy
def nextpagem():
    root1.destroy()
    import quiz
def nextpageh():
    root1.destroy()
    import hard

root1 = Tk()
root1.attributes('-fullscreen', True)
root1.title("QUIZ")
root1.overrideredirect(True)
title = Label(root1, text="SSJIT Pvt. Ltd. QUIZ", bg="#3e76a3", fg="white", font=("ariel", 20, "bold"))
title.pack(fill=X)
# root1.attributes('-alpha',0.9)
bg = ImageTk.PhotoImage(file="3.jpg")
canvas1 = Canvas(root1, width=400,height=400)
canvas1.pack(fill="both", expand=True)
canvas1.create_image(0, 0, image=bg,anchor="nw")
canvas1.create_text(750,100,text="Make Your Choice",font=("Arial",30,"bold"))
b1 = Button(root1, text="EASY", bg="#98bce0", relief=RIDGE, font=("Arial", 15, "bold"), cursor="circle",
            command=nextpage)
b1.place(x=380, y=300, relwidth=0.20, relheight=0.07)
b2 = Button(root1, text="MEDIUM", bg="#aaa6f0", relief=RIDGE, font=("Arial", 15, "bold"), cursor="circle",
            command=nextpagem)
b2.place(x=660, y=450, relwidth=0.20, relheight=0.07)
b3 = Button(root1, text="HARD", bg="#95e3ce", relief=RIDGE, font=("Arial", 15, "bold"), cursor="circle",
            command=nextpageh)
b3.place(x=940, y=600, relwidth=0.20, relheight=0.07)



# l1 = Label(text=, bg="#15449b", border="0", fg="white", font=("Comicsansms", 35, "bold"))
# l1.place(x=550, y=100)
Exitbtn = Button(root1, text='LOGOUT',border=8, bg='red', fg='white',font=("Arial", 12, "bold"),relief=GROOVE, command=root1.destroy)
Exitbtn.place(x=150,y=53,anchor="ne",relwidth=.06,relheight=.06)
root1.mainloop()