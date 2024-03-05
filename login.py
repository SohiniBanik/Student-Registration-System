from tkinter import *
from operator import itemgetter
from tkinter import ttk
from tkinter import messagebox
import Student as s
import pymysql
mainwin=Tk()
mainwin.title("Login and Registration")
mainwin.geometry("400x400")
bixT=Label(text="Login and Registration",font="Verdana 20 bold")
bixT.place(x=30,y=40)
def Register():
    con = pymysql.connect(host="localhost", user="root", password="", database="lar")
    cur = con.cursor()
    registerwin=Tk()
    registerwin.title("User Registration")
    registerwin.geometry("400x400")
    bixT=Label(registerwin,text=" Register Here",font="Verdana 20 bold")
    bixT.place(x=100,y=30)
    name=Label(registerwin,text="Name")
    name.place(x=90,y=100)
    email=Label(registerwin,text="Email")
    email.place(x=90, y=140)
    password=Label(registerwin,text="Password")
    password.place(x=90,y=180)
    repassword = Label(registerwin, text="RePassword")
    repassword.place(x=90, y=220)

    e1=Entry(registerwin)
    e1.place(x=180,y=100)
    e2 = Entry(registerwin)
    e2.place(x=180, y=140)
    e3 = Entry(registerwin,show="*")
    e3.place(x=180, y=180)
    e4 = Entry(registerwin,show="*")
    e4.place(x=180, y=220)
    def clearEnt():
        e1.delete(first=0,last=100)
        e2.delete(first=0, last=100)
        e3.delete(first=0, last=100)
        e4.delete(first=0, last=100)

    def errors():
        messagebox.showerror(title="Error",message="Password doesn't match")

    def insert():
        insert=("insert into register (name,email,password,repassword) values(%s,%s,%s,%s)")
        values=[e1.get(),e2.get(),e3.get(),e4.get()]
        cur.execute(insert,values)
        if e3.get()==e4.get():
            con.commit()
            clearEnt()
            messagebox.showinfo(title="Done",message="Account Created")
        else:
            errors()

    register = Button(registerwin, text="Register", fg="green", command=insert)
    register.place(x=200, y=300)
    Exitbtn = Button(registerwin, text="EXIT", bg="red", command=registerwin.destroy)
    Exitbtn.place(x=350, y=350)
    mainwin.destroy()
    registerwin.mainloop()

def Login():
    con = pymysql.connect(host="localhost", user="root", password="", database="lar")
    cur = con.cursor()
    conn = pymysql.connect(host="localhost", user="root", password="", database="lar")
    curr = conn.cursor()
    logwin = Tk()
    logwin.title("User Login")
    logwin.geometry("400x400")
    bixT = Label(logwin, text=" Login Here", font="Verdana 20 bold")
    bixT.place(x=140, y=30)

    email = Label(logwin, text="Email")
    email.place(x=100, y=150)
    password = Label(logwin,text="Password")
    password.place(x=100,y=180)

    e1 = Entry(logwin)
    e1.place(x=160,y=150)
    e2 = Entry(logwin,show="*")
    e2.place(x=160, y=180)

    def check():
        sqlC = "select email from register"
        sqlC2 = "select password from register"

        cur.execute(sqlC)
        curr.execute(sqlC2)

        em = e1.get()
        pw = e2.get()
        if em == "" or pw == "":
            messagebox.showerror("Please fill the details")
        e = []
        p = []
        for i in cur:
            e.append(i)
        for j in curr:
            p.append(j)

        res = list(map(itemgetter(0), e))
        res2 = list(map(itemgetter(0), p))
        k = len(res)
        i = 1
        while (i < k) :
            if res[i] == em and res2[i] == pw:
                messagebox.showinfo(title="Success",message="Login successful")
                root = Tk()
                s.Student(root)
                logwin.destroy()
                root.mainloop()
                break
            i += 1
        else:
            messagebox.showerror(title="error",message="username or password incorrect")

    log = Button(logwin, text="Login", fg="green", command=check)
    log.place(x=160, y=200)
    exitbtn = Button(logwin, text="EXIT", bg="red", command=logwin.destroy)
    exitbtn.place(x=350, y=350)

    mainwin.destroy()
    logwin.mainloop()

gotoLog=Button(mainwin,text="Login",fg="green",font="Verdana 10 bold",command=Login)
gotoLog.place(x=120,y=200)
gotoReg=Button(mainwin,text="Register",fg="green",font="Verdana 10 bold",command=Register)
gotoReg.place(x=180,y=200)
Exitbtn=Button(mainwin,text="EXIT",bg="red",command=mainwin.destroy)
Exitbtn.place(x=350,y=350)
mainwin.mainloop()