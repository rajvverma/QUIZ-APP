####medium quiz####
from tkinter import *
from tkinter import messagebox
import time
import random
from PIL import Image, ImageTk

root = Tk()
root.title("Login System")
root.geometry("1204x600+80+50")
root.config(background="#ffffff")
root.attributes('-fullscreen', True)
# bg=ImageTk.PhotoImage(file="4.jpg")
# bg_img = Label(root, image=bg).place(x=0, y=0, relwidth=1, relheight=1)
def isChecked():
    if var1.get() == 1:
        btnStartquiz['state'] = NORMAL

    elif var1.get() == 0:
        btnStartquiz['state'] = DISABLED


global var1


def startIspressed():
    # def rgb_hack(rgb):
    #     return "#%02x%02x%02x" % rgb

    # root.config(bg=rgb_hack((255, 0, 122)))

    global hour, minute, second
    hour = StringVar()
    minute = StringVar()
    second = StringVar()

    # setting the default value as 0
    hour.set("00")
    minute.set("00")
    second.set("00")

    global lbltimer1
    lbltimer1 = Label(root, text=":    :", font=("Consolas", 16), bg="white", fg="black")
    lbltimer1.place(x=745, y=30)

    # Use of Entry class to take input from the user
    global hourEntry, minuteEntry, secondEntry
    hourEntry = Label(root, width=3, font=("Arial", 18, ""),
                      textvariable=hour, foreground='white', background='green')
    hourEntry.place(x=700, y=30)

    minuteEntry = Label(root, width=3, font=("Arial", 18, ""),
                        textvariable=minute, foreground='white', background='green')
    minuteEntry.place(x=760, y=30)

    secondEntry = Label(root, width=3, font=("Arial", 18, ""),
                        textvariable=second, foreground='white', background='green')
    secondEntry.place(x=820, y=30)

    heading.destroy()
    lbl_Instr.destroy()
    i1.destroy()
    i2.destroy()
    i3.destroy()
    i4.destroy()
    i5.destroy()
    i6.destroy()
    i7.destroy()
    i8.destroy()
    i9.destroy()
    i10.destroy()
    i11.destroy()

    btnStartquiz.destroy()
    # C1.destroy()

    FrameW = Frame(root, bg="white")
    FrameW.place(x=450, y=245, height=150, width=300)

    gen()
    startquiz()


questions = [
    "Who of the following was the first female Olympic Champion ?",
    "Who is largest serving Chief Minister in India ?",
    "Which country has the most number of Lakes ?",
    "Which among the following teams was the first winner of \"World Cup Hockey\" ?",
    "Rama's Bridge or Rama Setu is located in which among the following straits?",
    "'The Naked Face', a very popular book is written by ?",
    "The National Anthem of India 'Jana Gana Mana' was first sung at?",
    "What is the upper limit of RTGS Transaction in India ?",
    "On which among the following dates, 'Army Day' is observed ?",
    "How long can a snail sleep for ?",
]

answers_choice = [
    ["Helen Jackson", "Charlotte Cooper", "Agnes Morton", "Louise Martin", ],
    ["Chimanbhai Patel", "Bhajan Lal", "Hiteshwar Saikia", "Jyoti Basu", ],
    ["Canada", "USA", "Finland", "Brazil", ],
    ["India", "Australia", "Pakistan", "Spain", ],
    ["Bering Strait", "Palk Strait", "Cook Strait", "Strait of Tebrau", ],
    ["Dominique Lapierre", "Larry Collins", "Sidney Sheldon", "Juan Benet", ],
    ["Delhi, 1911", "Calcutta, 1911", "Bengluru, 1912", "Mumbai, 1912", ],
    ["Rs. 25 Lakhs", "Rs. 10 Lakhs", "Rs. 15 Lakhs", "No Limit", ],
    ["January 15", "February 15", "March 15", "April 15", ],
    ["1 year", "3 years", "4 years", "2 years", ],
]

answers = [1, 3, 0, 2, 1, 2, 1, 3, 0, 1]

user_answer = []

indexes = []

questions_and_answers = [
    ["Q. Who of the following was the first female Olympic Champion ?\t\t\tAns: Charlotte Cooper"],
    ["Q. Who is largest serving Chief Minister in India ?\t\t\t\t\tAns: Jyoti Basu"],
    ["Q. Which country has the most number of Lakes ?\t\t\t\tAns: Canada"],
    ["Q. Which among the following teams was the first winner of World Cup Hockey ?\t\tAns: Pakistan"],
    ["Q. Rama's Bridge or Rama Setu is located in which among the following straits?\t\tAns: Palk Strait"],
    ["Q. 'The Naked Face', a very popular book is written by ?\t\t\t\tAns: Sidney Sheldon"],
    ["Q. The National Anthem of India 'Jana Gana Mana' was first sung at?\t\t\tAns: Calcutta, 1911"],
    ["Q. What is the upper limit of RTGS Transaction in India ?\t\t\t\tAns: No Limit"],
    ["Q. On which among the following dates, 'Army Day' is observed ?\t\t\tAns: January 15"],
    ["Q. How long can a snail sleep for ?\t\t\t\t\t\tAns: 3 years"],
]


def answersq():
    # labelimage.destroy()
    # labelresulttext.destroy()
    # btnquit.destroy()
    # btnanswer.destroy()

    newWindow = Toplevel()
    newWindow.resizable(False, False)
    newWindow.title("Answers")
    newWindow.geometry("1204x670+80+20")
    newWindow.config(background="#ffffff")

    lblQuestion1 = Label(newWindow, text=questions_and_answers[0], font=("verdana", 15), background="white", )
    lblQuestion1.place(x=0, y=80)
    lblQuestion2 = Label(newWindow, text=questions_and_answers[1], font=("verdana", 15), background="white")
    lblQuestion2.place(x=0, y=120)
    lblQuestion3 = Label(newWindow, text=questions_and_answers[2], font=("verdana", 15), background="white")
    lblQuestion3.place(x=0, y=160)
    lblQuestion4 = Label(newWindow, text=questions_and_answers[3], font=("verdana", 15), background="white")
    lblQuestion4.place(x=0, y=200)
    lblQuestion5 = Label(newWindow, text=questions_and_answers[4], font=("verdana", 15), background="white")
    lblQuestion5.place(x=0, y=240)
    lblQuestion6 = Label(newWindow, text=questions_and_answers[5], font=("verdana", 15), background="white")
    lblQuestion6.place(x=0, y=280)
    lblQuestion7 = Label(newWindow, text=questions_and_answers[6], font=("verdana", 15), background="white")
    lblQuestion7.place(x=0, y=320)
    lblQuestion8 = Label(newWindow, text=questions_and_answers[7], font=("verdana", 15), background="white")
    lblQuestion8.place(x=0, y=360)
    lblQuestion9 = Label(newWindow, text=questions_and_answers[8], font=("verdana", 15), background="white")
    lblQuestion9.place(x=0, y=400)
    lblQuestion10 = Label(newWindow, text=questions_and_answers[9], font=("verdana", 15), background="white")
    lblQuestion10.place(x=0, y=440)
    btnquit = Button(newWindow, text="QUIT", font=("Consolas", 15, "bold"), bg="gray", fg="black",
                     command=root.destroy)
    btnquit.place(x=480, y=580, width=250, height=50)


def gen():
    global indexes
    while (len(indexes) < 5):
        x = random.randint(0, 9)
        if x in indexes:
            continue
        else:
            indexes.append(x)
            # print(indexes)


def showresult(score):
    lbltimer1.destroy()
    lblQuestion.destroy()
    r1.destroy()
    r2.destroy()
    r3.destroy()
    r4.destroy()
    btnNext.destroy()

    labelimage = Label(root, background="#ffffff")
    labelimage.pack(pady=(50, 30))
    lbltimer.destroy()
    hourEntry.destroy()
    minuteEntry.destroy()
    secondEntry.destroy()

    labelresulttext = Label(root, font=("Consolas", 20), background="#ffffff")
    labelresulttext.pack()

    root.config(bg="white")
    global btnquit, btnanswer
    btnanswer = Button(root, text="Click Here for answers", font=("Consolas", 15, "bold"), bg="green", fg="white"
                       , command=answersq)
    btnanswer.place(x=460, y=480, width=300, height=50)

    if score >= 23:
        img_1 = PhotoImage(file="excellent.png")
        labelimage.configure(image=img_1)
        labelimage.image = img_1
        labelresulttext.configure(text="You are Excellent!!!\n Your Score is :- " + str(result), bg="white")
    elif (score >= 10 and score < 23):
        img_2 = PhotoImage(file="good.png")
        labelimage.configure(image=img_2)
        labelimage.image = img_2
        labelresulttext.configure(text="You can Be Better!!!\n Your Score is :- " + str(result), bg="white")
    else:
        img_3 = PhotoImage(file="sad.png")
        labelimage.configure(image=img_3)
        labelimage.image = img_3
        labelresulttext.configure(text="You Should Work Hard!!!\n Your Score is :- " + str(result), bg="white")


def calc():
    global indexes, user_answer, answers, result
    x = 0
    score = 0
    for i in indexes:
        if user_answer[x] == answers[i]:
            score += 5
            print(score)
        else:
            score -= 1
            print(score)
        x += 1
    result = score
    print(score)
    showresult(score)


ques = 1


def selected():
    global radiovar, user_answer
    global lblQuestion, r1, r2, r3, r4
    global ques
    x = radiovar.get()
    # print(x)

    user_answer.append(x)
    radiovar.set(-1)
    if ques < 5:
        lblQuestion.config(text=questions[indexes[ques]])
        r1["text"] = answers_choice[indexes[ques]][0]
        r2["text"] = answers_choice[indexes[ques]][1]
        r3["text"] = answers_choice[indexes[ques]][2]
        r4["text"] = answers_choice[indexes[ques]][3]
        ques = ques + 1
    else:
        calc()


def startquiz():
    # C1.destroy()
    global lblcolon
    global lbltimer

    lbltimer = Label(root, text="  Time remaining is", font=("Consolas", 16), bg="white", fg="red")
    lbltimer.pack(pady=(0, 10))

    global lblQuestion, r1, r2, r3, r4
    lblQuestion = Label(root, text=questions[indexes[0]], font=("Consolas", 16), width=500, justify="center",
                        wraplength=400, background="light gray", )
    lblQuestion.pack(pady=(100, 30))

    global radiovar
    radiovar = IntVar()
    radiovar.set(-1)

    r1 = Radiobutton(root, text=answers_choice[indexes[0]][0], font=("Times", 12), value=0, variable=radiovar,
                     background="#ffffff")
    r1.place(x=700, y=260)

    r2 = Radiobutton(root, text=answers_choice[indexes[0]][1], font=("Times", 12), value=1, variable=radiovar,
                     background="#ffffff")
    r2.place(x=700, y=320)

    r3 = Radiobutton(root, text=answers_choice[indexes[0]][2], font=("Times", 12), value=2, variable=radiovar,
                     background="#ffffff")
    r3.place(x=700, y=380)

    r4 = Radiobutton(root, text=answers_choice[indexes[0]][3], font=("Times", 12), value=3, variable=radiovar,
                     background="#ffffff")
    r4.place(x=700, y=440)
    global btnNext
    btnNext = Button(root, text="Save & Next", font=("Comic sans MS", 15, "bold"), command=selected, bg="green",
                     fg="WHITE")

    btnNext.place(x=700, y=600)

    global t
    t = 0 * 3600 + 4 * 60 + 0

    while t > -1:

        mins, secs = divmod(t, 60)

        hours = 0
        if mins > 60:
            hours, mins = divmod(mins, 60)

        hour.set("{0:2d}".format(hours))
        minute.set("{0:2d}".format(mins))
        second.set("{0:2d}".format(secs))

        root.update()
        time.sleep(1)

        if (t == 0):
            lbltimer1.destroy()
            lblQuestion.destroy()
            r1.destroy()
            r2.destroy()
            r3.destroy()
            r4.destroy()
            btnNext.destroy()
            lbltimer.destroy()
            hourEntry.destroy()
            minuteEntry.destroy()
            secondEntry.destroy()
            root.config(bg="white")
            global btnquit, btnanswer
            btnquit = Button(root, text="QUIT", font=("Consolas", 15, "bold"), bg="red", fg="white",
                             command=root.destroy)
            btnquit.place(x=530, y=550, width=150, height=35)
            btnanswer = Button(root, text="Click Here for answers", font=("Consolas", 15, "bold"), bg="green",
                               fg="white"
                               , command=answersq)
            btnanswer.place(x=460, y=480, width=300, height=50)
            labelimage = Label(root, background="#ffffff")

            labelimage.pack(pady=(50, 30))

        t -= 1


global t
t = 0 * 3600 + 2 * 60 + 10

heading = Label(root, text="QUIZ INSTRUCTIONS", font=("Comic sans MS", 30, "bold"), fg="white", bg="#7D1935",
                width=200)
heading.pack()

lbl_Instr = Label(root, text="Please read all the instructions carefully before going ahead:",
                  font=("Comic sans MS", 22, "bold"), fg="black", bg="light gray")
lbl_Instr.place(x=50, y=100)

i1 = Label(root, text="1. The Quiz contains Total 5 questions.", font=("Verdana", 12), fg="black", bg="white")
i1.place(x=50, y=200)

i2 = Label(root, text="2. Each question is alloted 4 marks for correct response.", font=("Verdana", 12), fg="black",
           bg="white")
i2.place(x=50, y=250)

i3 = Label(root, text="3. 1 Mark will get deducted from Total score for every wrong answer.", font=("Verdana", 12),
           fg="black", bg="white")
i3.place(x=50, y=300)

i4 = Label(root, text="4. There are total 4 options for every single question.", font=("Verdana", 12), fg="black",
           bg="white")
i4.place(x=50, y=350)

i5 = Label(root, text="5. Total Time duration for quiz is 5 minutes.", font=("Verdana", 12), fg="black", bg="white")
i5.place(x=50, y=400)

i6 = Label(root, text="6. Click the radio button to indicate your choice.", font=("Verdana", 12), fg="black",
           bg="white")
i6.place(x=50, y=450)

i7 = Label(root, text="7. Only one answer can be selected for a multiple choice question.", font=("Verdana", 12),
           fg="black", bg="white")
i7.place(x=50, y=500)

i8 = Label(root, text="8. Select an answer for every question. ", font=("Verdana", 12), fg="black", bg="white")
i8.place(x=50, y=550)

i9 = Label(root,
           text="9. To get your score please complete quiz before the time",
           font=("Verdana", 12), fg="black", bg="white")
i9.place(x=50, y=600)
var1 = IntVar()
i10 = Checkbutton(root, text="I agree all terms and conditions", font=("Comic sans MS", 17, "bold"),
                  bg="white", fg="black", variable=var1, onvalue=1, offvalue=0, command=isChecked)

i10.place(x=50, y=650)
i11 = Label(root, text="Click here to Start", font=("Comic sans MS", 17, "bold"), bg="white", fg="black")
i11.place(x=700, y=770)

btnStartquiz = Button(root, text="START QUIZ", font=("Comic sans MS", 17, "bold"), fg="white", bg="green",
                      state=DISABLED, command=startIspressed)

btnStartquiz.place(x=725, y=700)

Exitbtn = Button(root, text='Quit',border=8, bg='red', fg='white',font=("Arial", 12, "bold"),relief=GROOVE, command=root.destroy)
Exitbtn.place(x=1500,y=800,anchor="ne",relwidth=.06,relheight=.06)

root.mainloop()