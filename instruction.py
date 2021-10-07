#### ssjit quiz gui ####
from tkinter import *
splash_root=Tk()
splash_root.geometry("777x383+400+200")
bg1=PhotoImage(file="6.png")
bg_img1=Label(splash_root,image=bg1).place(x=0,y=0,relwidth=1,relheight=1)
splash_root.overrideredirect(True)
# splash_root.attributes('-alpha',0.9)
lable=Label(splash_root,text="Powered by",font=("Arial",10,"bold"),bg="white",fg="black").place(x=20,y=25,anchor="sw")
lable=Label(splash_root,text="SSJ IT Solutions Pvt. Ltd. ",font=("Arial",14,"bold"),bg="white",fg="black").place(x=20,y=55,anchor="sw")


def main_window():
    splash_root.destroy()
    import main


splash_root.after(70000,main_window)

mainloop()