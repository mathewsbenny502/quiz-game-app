import tkinter as tk
from tkinter import *
import random
import sqlite3
from tkinter import font
import time

#image working, topic selection page working, math only , score calculation incorrect

def loginPage(logdata):
    sup.destroy()
    global login
    login = Tk()
    
    user_name = StringVar()
    password = StringVar()
    
    login_canvas = Canvas(login,width=720,height=440,bg="#101357")
    login_canvas.pack()

    login_frame = Frame(login_canvas,bg="white")
    login_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

    heading = Label(login_frame,text="Quiz App Login",fg="black",bg="white")
    heading.config(font=('calibri 40'))
    heading.place(relx=0.2,rely=0.1)

    #USER NAME
    ulabel = Label(login_frame,text="Username",fg='black',bg='white')
    ulabel.place(relx=0.21,rely=0.4)
    uname = Entry(login_frame,bg='#d3d3d3',fg='black',textvariable = user_name)
    uname.config(width=42)
    uname.place(relx=0.31,rely=0.4)

    #PASSWORD
    plabel = Label(login_frame,text="Password",fg='black',bg='white')
    plabel.place(relx=0.215,rely=0.5)
    pas = Entry(login_frame,bg='#d3d3d3',fg='black',textvariable = password)
    pas.config(width=42)
    pas.place(relx=0.31,rely=0.5)

    def check():
        global er
        for a,b,c,d in logdata:
            if b == uname.get() and c == pas.get():
                menu()
                break
        if uname.get() == "" or pas.get() == "":
                er = Label(login_frame,text="Enter the username and password",fg='black',bg='white')
                er.place(relx=0.34,rely=0.7)
        else:
            er.destroy()
            error = Label(login_frame,text="Wrong Username or Password!",fg='black',bg='white')
            error.place(relx=0.37,rely=0.7)
    
    #LOGIN BUTTON
    log = Button(login_frame,text='Login',padx=5,pady=5,width=5,command=check)
    log.configure(width = 15,height=1, activebackground = "#33B5E5", relief = FLAT)
    log.place(relx=0.4,rely=0.6)
    
    
    login.mainloop()

def signUpPage():
    root.destroy()
    global sup
    sup = Tk()
    
    fname = StringVar()
    uname = StringVar()
    passW = StringVar()
    country = StringVar()
    
    
    sup_canvas = Canvas(sup,width=720,height=440,bg="#101357")
    sup_canvas.pack()

    sup_frame = Frame(sup_canvas,bg="white")
    sup_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

    heading = Label(sup_frame,text="Quiz App SignUp",fg="black",bg="white")
    heading.config(font=('calibri 40'))
    heading.place(relx=0.2,rely=0.1)

    #full name
    flabel = Label(sup_frame,text="Full Name",fg='black',bg='white')
    flabel.place(relx=0.21,rely=0.4)
    fname = Entry(sup_frame,bg='#d3d3d3',fg='black',textvariable = fname)
    fname.config(width=42)
    fname.place(relx=0.31,rely=0.4)

    #username
    ulabel = Label(sup_frame,text="Username",fg='black',bg='white')
    ulabel.place(relx=0.21,rely=0.5)
    user = Entry(sup_frame,bg='#d3d3d3',fg='black',textvariable = uname)
    user.config(width=42)
    user.place(relx=0.31,rely=0.5)
    
    
    #password
    plabel = Label(sup_frame,text="Password",fg='black',bg='white')
    plabel.place(relx=0.215,rely=0.6)
    pas = Entry(sup_frame,bg='#d3d3d3',fg='black',textvariable = passW)
    pas.config(width=42)
    pas.place(relx=0.31,rely=0.6)
    
    
    
    #country
    clabel = Label(sup_frame,text="Country",fg='black',bg='white')
    clabel.place(relx=0.215,rely=0.7)
    c = Entry(sup_frame,bg='#d3d3d3',fg='black',textvariable = country)
    c.config(width=42)
    c.place(relx=0.31,rely=0.7)
    def addUserToDataBase():
        
        fullname = fname.get()
        username = user.get()
        password = pas.get()
        country = c.get()
        
        conn = sqlite3.connect('quiz.db')
        create = conn.cursor()
        create.execute('CREATE TABLE IF NOT EXISTS userSignUp(FULLNAME text, USERNAME text,PASSWORD text,COUNTRY text)')
        create.execute("INSERT INTO userSignUp VALUES (?,?,?,?)",(fullname,username,password,country)) 
        conn.commit()
        create.execute('SELECT * FROM userSignUp')
        z=create.fetchall()
        print(z)
#        L2.config(text="Username is "+z[0][0]+"\nPassword is "+z[-1][1])
        conn.close()
        loginPage(z)
    def gotoLogin():
        conn = sqlite3.connect('quiz.db')
        create = conn.cursor()
        conn.commit()
        create.execute('SELECT * FROM userSignUp')
        z=create.fetchall()
        loginPage(z)
    #signup BUTTON
    sp = Button(sup_frame,text='SignUp',padx=5,pady=5,width=5,command = addUserToDataBase)
    sp.configure(width = 15,height=1, activebackground = "#33B5E5", relief = FLAT)
    sp.place(relx=0.4,rely=0.8)

    log = Button(sup_frame,text='Already have a Account?',padx=5,pady=5,width=5,command = gotoLogin,bg="white")
    log.configure(width = 16,height=1, activebackground = "#33B5E5", relief = FLAT)
    log.place(relx=0.4,rely=0.9)

    sup.mainloop()
def menu():
    login.destroy()
    global menu 
    menu = Tk()
        
        
    menu_canvas = Canvas(menu,width=720,height=440,bg="#101357")
    menu_canvas.pack()

    menu_frame = Frame(menu_canvas,bg="white")
    menu_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

        
        
    wel = Label(menu_canvas,text=' W E L C O M E  T O  Q U I Z  S T A T I O N ',fg="white",bg="#101357") 
    wel.config(font=('Broadway 22'))
    wel.place(relx=0.1,rely=0.02)

    level = Label(menu_frame,text='Select your Quiz Topic',bg="white",font="calibri 20")
    level.place(relx=0.3,rely=0.05)

    myFont = font.Font(size=12)

    button = Button(menu_frame, text='Math',command = math) 
    button.configure(width = 16,height=3, activebackground = "#33B5E5", relief = RAISED,font=myFont)
    button.place(relx=0.05,rely=0.3,anchor='w')

    button = Button(menu_frame, text='Football',command = medium3) 
    button.configure(width = 16,height=3, activebackground = "#33B5E5", relief = RAISED,font=myFont)
    button.place(relx=0.05,rely=0.55,anchor='w')

    button = Button(menu_frame, text='Science',command = medium1) 
    button.configure(width = 16,height=3, activebackground = "#33B5E5", relief = RAISED,font=myFont)
    button.place(relx=0.5,rely=0.3,anchor='center')

    button = Button(menu_frame, text='Music',command = medium5) 
    button.configure(width = 16,height=3, activebackground = "#33B5E5", relief = RAISED,font=myFont)
    button.place(relx=0.5,rely=0.55,anchor='center')

    button = Button(menu_frame, text='Cricket',command = medium2) 
    button.configure(width = 16,height=3, activebackground = "#33B5E5", relief = RAISED,font=myFont)
    button.place(relx=0.95,rely=0.3,anchor='e')

    button = Button(menu_frame, text='Movies',command = medium6) 
    button.configure(width = 16,height=3, activebackground = "#33B5E5", relief = RAISED,font=myFont)
    button.place(relx=0.95,rely=0.55,anchor='e')

    button = Button(menu_frame, text='Countries',command = medium4) 
    button.configure(width = 16,height=3, activebackground = "#33B5E5", relief = RAISED,font=myFont)
    button.place(relx=0.5,rely=0.82,anchor='center')

    
    menu.mainloop()

def math():
    
    global e
    e = Tk()
    
    math_canvas = Canvas(e,width=720,height=440,bg="#101357")
    math_canvas.pack()

    math_frame = Frame(math_canvas,bg="white")
    math_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

    
    def countDown():
        check = 0
        for k in range(10, 0, -1):
            
            if k == 1:
                check=-1
            timer.configure(text=k)
            math_frame.update()
            time.sleep(1)
            
        timer.configure(text="Times up!")
        if check==-1:
            return (-1)
        else:
            return 0
    global score 
    score = 0
    question_data = []

    with open("math.txt", "r") as file:
        lines = file.readlines()
        question = []
        for line in lines:
            line = line.strip()
            if line:
                question.append(line)
            else:
                question_data.append(question)
                question = []

        question_data.append(question)  # Append the last question to the question_data list

    random.shuffle(question_data)  # Shuffle the questions
    global index
    index = 0

    ques = Label(math_frame, text="", font="calibri 12", bg="white")
    ques.place(relx=0.5, rely=0.2, anchor=CENTER)

    var = StringVar()

    current_question = question_data[index]
    ques.configure(text=current_question[0])

    a = Radiobutton(math_frame, text=current_question[1], font="calibri 10", value=current_question[1], variable=var, bg="white")
    a.place(relx=0.5, rely=0.42, anchor=CENTER)

    b = Radiobutton(math_frame, text=current_question[2], font="calibri 10", value=current_question[2], variable=var, bg="white")
    b.place(relx=0.5, rely=0.52, anchor=CENTER)

    c = Radiobutton(math_frame, text=current_question[3], font="calibri 10", value=current_question[3], variable=var, bg="white")
    c.place(relx=0.5, rely=0.62, anchor=CENTER)

    d = Radiobutton(math_frame, text=current_question[4], font="calibri 10", value=current_question[4], variable=var, bg="white")
    d.place(relx=0.5, rely=0.72, anchor=CENTER)


    timer = Label(m)
    timer.place(relx=0.8, rely=0.82, anchor=CENTER)



    def display():
        global index
        if index >= len(question_data):
            m.destroy()
            showMark(score)
            return
        
        current_question = question_data[index]

        ques.configure(text=current_question[0])

        var.set("")  # Clear the selected option

        a.configure(text=current_question[1], value=current_question[1])

        b.configure(text=current_question[2], value=current_question[2])

        c.configure(text=current_question[3], value=current_question[3])

        d.configure(text=current_question[4], value=current_question[4])

        index = index + 1
        y = countDown()
        if y == -1:
            display()


    def calc():
        global score
        if var.get() == question_data[index - 1][5]:
            score += 1
        display()
    
    submit = Button(math_frame, command=calc, text="Submit")
    submit.place(relx=0.5, rely=0.82, anchor=CENTER)

    nextQuestion = Button(math_frame, command=display, text="Next")
    nextQuestion.place(relx=0.87, rely=0.82, anchor=CENTER)

    y = countDown()
    if y == -1:
        display()
    e.mainloop()
    
    
def medium1():
    
    global m
    m = Tk()
    
    med1_canvas = Canvas(m,width=720,height=440,bg="#101357")
    med1_canvas.pack()

    med1_frame = Frame(med1_canvas,bg="white")
    med1_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

    
    def countDown():
        check = 0
        for k in range(10, 0, -1):
            
            if k == 1:
                check=-1
            timer.configure(text=k)
            med1_frame.update()
            time.sleep(1)
            
        timer.configure(text="Times up!")
        if check==-1:
            return (-1)
        else:
            return 0
        
    global score 
    score = 0
    question_data = []

    with open("science.txt", "r") as file:
        lines = file.readlines()
        question = []
        for line in lines:
            line = line.strip()
            if line:
                question.append(line)
            else:
                question_data.append(question)
                question = []

        question_data.append(question)  # Append the last question to the question_data list

    random.shuffle(question_data)  # Shuffle the questions
    global index
    index = 0

    ques = Label(med1_frame, text="", font="calibri 12", bg="white")
    ques.place(relx=0.5, rely=0.2, anchor=CENTER)

    var = StringVar()

    current_question = question_data[index]
    ques.configure(text=current_question[0])

    a = Radiobutton(med1_frame, text=current_question[1], font="calibri 10", value=current_question[1], variable=var, bg="white")
    a.place(relx=0.5, rely=0.42, anchor=CENTER)

    b = Radiobutton(med1_frame, text=current_question[2], font="calibri 10", value=current_question[2], variable=var, bg="white")
    b.place(relx=0.5, rely=0.52, anchor=CENTER)

    c = Radiobutton(med1_frame, text=current_question[3], font="calibri 10", value=current_question[3], variable=var, bg="white")
    c.place(relx=0.5, rely=0.62, anchor=CENTER)

    d = Radiobutton(med1_frame, text=current_question[4], font="calibri 10", value=current_question[4], variable=var, bg="white")
    d.place(relx=0.5, rely=0.72, anchor=CENTER)


    timer = Label(m)
    timer.place(relx=0.8, rely=0.82, anchor=CENTER)



    def display():
        global index
        if index >= len(question_data):
            m.destroy()
            showMark(score)
            return
        
        current_question = question_data[index]

        ques.configure(text=current_question[0])

        var.set("")  # Clear the selected option

        a.configure(text=current_question[1], value=current_question[1])

        b.configure(text=current_question[2], value=current_question[2])

        c.configure(text=current_question[3], value=current_question[3])

        d.configure(text=current_question[4], value=current_question[4])

        index = index + 1
        y = countDown()
        if y == -1:
            display()

            
    def calc():
        global score
        if var.get() == question_data[index - 1][5]:
            score += 1
        display()

    submit = Button(med1_frame,command=calc,text="Submit")
    submit.place(relx=0.5,rely=0.82,anchor=CENTER)
    
    nextQuestion = Button(med1_frame,command=display,text="Next")
    nextQuestion.place(relx=0.87,rely=0.82,anchor=CENTER) 

    y = countDown()
    if y == -1:
        display()
    e.mainloop()


def medium6():
    
    global m
    m = Tk()
    
    med6_canvas = Canvas(m,width=720,height=440,bg="#101357")
    med6_canvas.pack()

    med6_frame = Frame(med6_canvas,bg="white")
    med6_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

    
    def countDown():
        check = 0
        for k in range(10, 0, -1):
            
            if k == 1:
                check=-1
            timer.configure(text=k)
            med6_frame.update()
            time.sleep(1)
            
        timer.configure(text="Times up!")
        if check==-1:
            return (-1)
        else:
            return 0
        
    global score 
    score = 0
    question_data = []

    with open("movie.txt", "r") as file:
        lines = file.readlines()
        question = []
        for line in lines:
            line = line.strip()
            if line:
                question.append(line)
            else:
                question_data.append(question)
                question = []

        question_data.append(question)  # Append the last question to the question_data list

    random.shuffle(question_data)  # Shuffle the questions
    global index
    index = 0

    ques = Label(med6_frame, text="", font="calibri 12", bg="white")
    ques.place(relx=0.5, rely=0.2, anchor=CENTER)

    var = StringVar()

    current_question = question_data[index]
    ques.configure(text=current_question[0])

    a = Radiobutton(med6_frame, text=current_question[1], font="calibri 10", value=current_question[1], variable=var, bg="white")
    a.place(relx=0.5, rely=0.42, anchor=CENTER)

    b = Radiobutton(med6_frame, text=current_question[2], font="calibri 10", value=current_question[2], variable=var, bg="white")
    b.place(relx=0.5, rely=0.52, anchor=CENTER)

    c = Radiobutton(med6_frame, text=current_question[3], font="calibri 10", value=current_question[3], variable=var, bg="white")
    c.place(relx=0.5, rely=0.62, anchor=CENTER)

    d = Radiobutton(med6_frame, text=current_question[4], font="calibri 10", value=current_question[4], variable=var, bg="white")
    d.place(relx=0.5, rely=0.72, anchor=CENTER)


    timer = Label(m)
    timer.place(relx=0.8, rely=0.82, anchor=CENTER)



    def display():
        global index
        if index >= len(question_data):
            m.destroy()
            showMark(score)
            return
        
        current_question = question_data[index]

        ques.configure(text=current_question[0])

        var.set("")  # Clear the selected option

        a.configure(text=current_question[1], value=current_question[1])

        b.configure(text=current_question[2], value=current_question[2])

        c.configure(text=current_question[3], value=current_question[3])

        d.configure(text=current_question[4], value=current_question[4])

        index = index + 1
        y = countDown()
        if y == -1:
            display()

            
    def calc():
        global score
        if var.get() == question_data[index - 1][5]:
            score += 1
        display()

    submit = Button(med6_frame,command=calc,text="Submit")
    submit.place(relx=0.5,rely=0.82,anchor=CENTER)
    
    nextQuestion = Button(med6_frame,command=display,text="Next")
    nextQuestion.place(relx=0.87,rely=0.82,anchor=CENTER) 
       
    y = countDown()
    if y == -1:
        display()
    e.mainloop()

def medium4():
    
    global m
    m = Tk()
    
    med4_canvas = Canvas(m,width=720,height=440,bg="#101357")
    med4_canvas.pack()

    med4_frame = Frame(med4_canvas,bg="white")
    med4_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

    
    def countDown():
        check = 0
        for k in range(10, 0, -1):
            
            if k == 1:
                check=-1
            timer.configure(text=k)
            med4_frame.update()
            time.sleep(1)
            
        timer.configure(text="Times up!")
        if check==-1:
            return (-1)
        else:
            return 0
        
    global score 
    score = 0
    question_data = []

    with open("country.txt", "r") as file:
        lines = file.readlines()
        question = []
        for line in lines:
            line = line.strip()
            if line:
                question.append(line)
            else:
                question_data.append(question)
                question = []

        question_data.append(question)  # Append the last question to the question_data list

    random.shuffle(question_data)  # Shuffle the questions
    global index
    index = 0

    ques = Label(med4_frame, text="", font="calibri 12", bg="white")
    ques.place(relx=0.5, rely=0.2, anchor=CENTER)

    var = StringVar()

    current_question = question_data[index]
    ques.configure(text=current_question[0])

    a = Radiobutton(med4_frame, text=current_question[1], font="calibri 10", value=current_question[1], variable=var, bg="white")
    a.place(relx=0.5, rely=0.42, anchor=CENTER)

    b = Radiobutton(med4_frame, text=current_question[2], font="calibri 10", value=current_question[2], variable=var, bg="white")
    b.place(relx=0.5, rely=0.52, anchor=CENTER)

    c = Radiobutton(med4_frame, text=current_question[3], font="calibri 10", value=current_question[3], variable=var, bg="white")
    c.place(relx=0.5, rely=0.62, anchor=CENTER)

    d = Radiobutton(med4_frame, text=current_question[4], font="calibri 10", value=current_question[4], variable=var, bg="white")
    d.place(relx=0.5, rely=0.72, anchor=CENTER)


    timer = Label(m)
    timer.place(relx=0.8, rely=0.82, anchor=CENTER)



    def display():
        global index
        if index >= len(question_data):
            m.destroy()
            showMark(score)
            return
        
        current_question = question_data[index]

        ques.configure(text=current_question[0])

        var.set("")  # Clear the selected option

        a.configure(text=current_question[1], value=current_question[1])

        b.configure(text=current_question[2], value=current_question[2])

        c.configure(text=current_question[3], value=current_question[3])

        d.configure(text=current_question[4], value=current_question[4])

        index = index + 1
        y = countDown()
        if y == -1:
            display()

            
    def calc():
        global score
        if var.get() == question_data[index - 1][5]:
            score += 1
        display()

    submit = Button(med4_frame,command=calc,text="Submit")
    submit.place(relx=0.5,rely=0.82,anchor=CENTER)
    
    nextQuestion = Button(med4_frame,command=display,text="Next")
    nextQuestion.place(relx=0.87,rely=0.82,anchor=CENTER) 
       
    y = countDown()
    if y == -1:
        display()
    e.mainloop()

def medium5():
    
    global m
    m = Tk()
    
    med5_canvas = Canvas(m,width=720,height=440,bg="#101357")
    med5_canvas.pack()

    med5_frame = Frame(med5_canvas,bg="white")
    med5_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

    
    def countDown():
        check = 0
        for k in range(10, 0, -1):
            
            if k == 1:
                check=-1
            timer.configure(text=k)
            med5_frame.update()
            time.sleep(1)
            
        timer.configure(text="Times up!")
        if check==-1:
            return (-1)
        else:
            return 0
        
    global score 
    score = 0
    question_data = []

    with open("music.txt", "r") as file:
        lines = file.readlines()
        question = []
        for line in lines:
            line = line.strip()
            if line:
                question.append(line)
            else:
                question_data.append(question)
                question = []

        question_data.append(question)  # Append the last question to the question_data list

    random.shuffle(question_data)  # Shuffle the questions
    global index
    index = 0

    ques = Label(med5_frame, text="", font="calibri 12", bg="white")
    ques.place(relx=0.5, rely=0.2, anchor=CENTER)

    var = StringVar()

    current_question = question_data[index]
    ques.configure(text=current_question[0])

    a = Radiobutton(med5_frame, text=current_question[1], font="calibri 10", value=current_question[1], variable=var, bg="white")
    a.place(relx=0.5, rely=0.42, anchor=CENTER)

    b = Radiobutton(med5_frame, text=current_question[2], font="calibri 10", value=current_question[2], variable=var, bg="white")
    b.place(relx=0.5, rely=0.52, anchor=CENTER)

    c = Radiobutton(med5_frame, text=current_question[3], font="calibri 10", value=current_question[3], variable=var, bg="white")
    c.place(relx=0.5, rely=0.62, anchor=CENTER)

    d = Radiobutton(med5_frame, text=current_question[4], font="calibri 10", value=current_question[4], variable=var, bg="white")
    d.place(relx=0.5, rely=0.72, anchor=CENTER)


    timer = Label(m)
    timer.place(relx=0.8, rely=0.82, anchor=CENTER)



    def display():
        global index
        if index >= len(question_data):
            m.destroy()
            showMark(score)
            return
        
        current_question = question_data[index]

        ques.configure(text=current_question[0])

        var.set("")  # Clear the selected option

        a.configure(text=current_question[1], value=current_question[1])

        b.configure(text=current_question[2], value=current_question[2])

        c.configure(text=current_question[3], value=current_question[3])

        d.configure(text=current_question[4], value=current_question[4])

        index = index + 1
        y = countDown()
        if y == -1:
            display()

            
    def calc():
        global score
        if var.get() == question_data[index - 1][5]:
            score += 1
        display()

    submit = Button(med5_frame,command=calc,text="Submit")
    submit.place(relx=0.5,rely=0.82,anchor=CENTER)
    
    nextQuestion = Button(med5_frame,command=display,text="Next")
    nextQuestion.place(relx=0.87,rely=0.82,anchor=CENTER) 
       
    y = countDown()
    if y == -1:
        display()
    e.mainloop()

def medium3():
    
    global m
    m = Tk()
    
    med3_canvas = Canvas(m,width=720,height=440,bg="#101357")
    med3_canvas.pack()

    med3_frame = Frame(med3_canvas,bg="white")
    med3_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

    
    def countDown():
        check = 0
        for k in range(10, 0, -1):
            
            if k == 1:
                check=-1
            timer.configure(text=k)
            med3_frame.update()
            time.sleep(1)
            
        timer.configure(text="Times up!")
        if check==-1:
            return (-1)
        else:
            return 0
        
    global score 
    score = 0
    question_data = []

    with open("football.txt", "r") as file:
        lines = file.readlines()
        question = []
        for line in lines:
            line = line.strip()
            if line:
                question.append(line)
            else:
                question_data.append(question)
                question = []

        question_data.append(question)  # Append the last question to the question_data list

    random.shuffle(question_data)  # Shuffle the questions
    global index
    index = 0

    ques = Label(med3_frame, text="", font="calibri 12", bg="white")
    ques.place(relx=0.5, rely=0.2, anchor=CENTER)

    var = StringVar()

    current_question = question_data[index]
    ques.configure(text=current_question[0])

    a = Radiobutton(med3_frame, text=current_question[1], font="calibri 10", value=current_question[1], variable=var, bg="white")
    a.place(relx=0.5, rely=0.42, anchor=CENTER)

    b = Radiobutton(med3_frame, text=current_question[2], font="calibri 10", value=current_question[2], variable=var, bg="white")
    b.place(relx=0.5, rely=0.52, anchor=CENTER)

    c = Radiobutton(med3_frame, text=current_question[3], font="calibri 10", value=current_question[3], variable=var, bg="white")
    c.place(relx=0.5, rely=0.62, anchor=CENTER)

    d = Radiobutton(med3_frame, text=current_question[4], font="calibri 10", value=current_question[4], variable=var, bg="white")
    d.place(relx=0.5, rely=0.72, anchor=CENTER)


    timer = Label(m)
    timer.place(relx=0.8, rely=0.82, anchor=CENTER)



    def display():
        global index
        if index >= len(question_data):
            m.destroy()
            showMark(score)
            return
        
        current_question = question_data[index]

        ques.configure(text=current_question[0])

        var.set("")  # Clear the selected option

        a.configure(text=current_question[1], value=current_question[1])

        b.configure(text=current_question[2], value=current_question[2])

        c.configure(text=current_question[3], value=current_question[3])

        d.configure(text=current_question[4], value=current_question[4])

        index = index + 1
        y = countDown()
        if y == -1:
            display()

            
    def calc():
        global score
        if var.get() == question_data[index - 1][5]:
            score += 1
        display()

    submit = Button(med3_frame,command=calc,text="Submit")
    submit.place(relx=0.5,rely=0.82,anchor=CENTER)
    
    nextQuestion = Button(med3_frame,command=display,text="Next")
    nextQuestion.place(relx=0.87,rely=0.82,anchor=CENTER) 
       
    y = countDown()
    if y == -1:
        display()
    e.mainloop()

def medium2():
    
    global m
    m = Tk()
    
    med2_canvas = Canvas(m,width=720,height=440,bg="#101357")
    med2_canvas.pack()

    med2_frame = Frame(med2_canvas,bg="white")
    med2_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

    
    def countDown():
        check = 0
        for k in range(10, 0, -1):
            
            if k == 1:
                check=-1
            timer.configure(text=k)
            med2_frame.update()
            time.sleep(1)
            
        timer.configure(text="Times up!")
        if check==-1:
            return (-1)
        else:
            return 0
        
    global score 
    score = 0
    question_data = []

    with open("cricket.txt", "r") as file:
        lines = file.readlines()
        question = []
        for line in lines:
            line = line.strip()
            if line:
                question.append(line)
            else:
                question_data.append(question)
                question = []

        question_data.append(question)  # Append the last question to the question_data list

    random.shuffle(question_data)  # Shuffle the questions
    global index
    index = 0

    ques = Label(med2_frame, text="", font="calibri 12", bg="white")
    ques.place(relx=0.5, rely=0.2, anchor=CENTER)

    var = StringVar()

    current_question = question_data[index]
    ques.configure(text=current_question[0])

    a = Radiobutton(med2_frame, text=current_question[1], font="calibri 10", value=current_question[1], variable=var, bg="white")
    a.place(relx=0.5, rely=0.42, anchor=CENTER)

    b = Radiobutton(med2_frame, text=current_question[2], font="calibri 10", value=current_question[2], variable=var, bg="white")
    b.place(relx=0.5, rely=0.52, anchor=CENTER)

    c = Radiobutton(med2_frame, text=current_question[3], font="calibri 10", value=current_question[3], variable=var, bg="white")
    c.place(relx=0.5, rely=0.62, anchor=CENTER)

    d = Radiobutton(med2_frame, text=current_question[4], font="calibri 10", value=current_question[4], variable=var, bg="white")
    d.place(relx=0.5, rely=0.72, anchor=CENTER)


    timer = Label(m)
    timer.place(relx=0.8, rely=0.82, anchor=CENTER)



    def display():
        global index
        if index >= len(question_data):
            m.destroy()
            showMark(score)
            return
        
        current_question = question_data[index]

        ques.configure(text=current_question[0])

        var.set("")  # Clear the selected option

        a.configure(text=current_question[1], value=current_question[1])

        b.configure(text=current_question[2], value=current_question[2])

        c.configure(text=current_question[3], value=current_question[3])

        d.configure(text=current_question[4], value=current_question[4])

        index = index + 1
        y = countDown()
        if y == -1:
            display()

            
    def calc():
        global score
        if var.get() == question_data[index - 1][5]:
            score += 1
        display()

    submit = Button(med2_frame,command=calc,text="Submit")
    submit.place(relx=0.5,rely=0.82,anchor=CENTER)
    
    nextQuestion = Button(med2_frame,command=display,text="Next")
    nextQuestion.place(relx=0.87,rely=0.82,anchor=CENTER) 
       
    y = countDown()
    if y == -1:
        display()
    e.mainloop()


def showMark(mark):
    global sh
    sh = Tk()
    
    show_canvas = Canvas(sh,width=720,height=440,bg="#101357")
    show_canvas.pack()

    show_frame = Frame(show_canvas,bg="white")
    show_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)
    
    st = "Your score is "+str(mark)
    mlabel = Label(show_canvas,text=st,fg="black")
    mlabel.place(relx=0.5,rely=0.2,anchor=CENTER)
    
    sh.mainloop()

def start():
    global root
    root = Tk()
    canvas = Canvas(root, width=720, height=480, bg='yellow')
    canvas.grid(column=0, row=1)

    img = PhotoImage(file="image.png")

    # Adjust the coordinates for proper image placement within the canvas
    image_x = 0
    image_y = 0

    canvas.create_image(image_x, image_y, image=img, anchor="nw")

    button = Button(root, text='Start', command=signUpPage)
    button.configure(width=102, height=4, activebackground="#33B5E5", relief="raised")
    button.grid(column=0, row=2)

    root.mainloop()

    root.mainloop()
start()