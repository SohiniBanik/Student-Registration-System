from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql
class Student:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Management System")
        self.root.geometry("1400x900+0+0")

        title = Label(self.root,text="Student Registration System",bd=10,relief=GROOVE,font=("times new roman",40,"bold"),bg="light blue",fg="black")
        title.pack(side=TOP,fill=X)

        #=====all variables======
        self.roll_var = StringVar()
        self.name_var = StringVar()   #no calculations so string
        self.email_var = StringVar()
        self.gender_var = StringVar()
        self.contact_var = StringVar()
        self.dob_var = StringVar()
        self.search_by=StringVar()
        self.search_txt=StringVar()

        #=====Manage Frame======
        Manage_Frame = Frame(self.root,bd=4,relief=RIDGE,bg="light blue")
        Manage_Frame.place(x=20,y=100,width=450,height=600)

        m_title=Label(Manage_Frame,text="Manage Students",bg="light blue",fg="black",font=("times new roman",30,"bold"))
        m_title.grid(row=0,columnspan=2,pady=20)

        lbl_roll = Label(Manage_Frame,text="Roll No",bg="light blue",fg="black",font=("times new roman",20,"bold"))
        lbl_roll.grid(row=1,column=0,pady=5,padx=20,sticky="w")

        txt_Roll = Entry(Manage_Frame,textvariable=self.roll_var,font=("times new roman",13,"bold"),bd=5,relief=GROOVE)
        txt_Roll.grid(row=1, column=1, pady=5, padx=20, sticky="w")

        lbl_name = Label(Manage_Frame, text="Name", bg="light blue", fg="black", font=("times new roman", 20, "bold"))
        lbl_name.grid(row=2, column=0, pady=5, padx=20, sticky="w")

        txt_Name = Entry(Manage_Frame,textvariable=self.name_var, font=("times new roman", 13, "bold"), bd=5, relief=GROOVE)
        txt_Name.grid(row=2, column=1, pady=5, padx=20, sticky="w")

        lbl_email = Label(Manage_Frame, text="Email Address", bg="light blue", fg="black", font=("times new roman", 20, "bold"))
        lbl_email.grid(row=3, column=0, pady=5, padx=20, sticky="w")

        txt_Email = Entry(Manage_Frame,textvariable=self.email_var, font=("times new roman", 13, "bold"), bd=5, relief=GROOVE)
        txt_Email.grid(row=3, column=1, pady=5, padx=20, sticky="w")

        lbl_gen = Label(Manage_Frame, text="Gender", bg="light blue", fg="black", font=("times new roman", 20, "bold"))
        lbl_gen.grid(row=4, column=0, pady=5, padx=20, sticky="w")

        combo_gen = ttk.Combobox(Manage_Frame,textvariable=self.gender_var,font=("times new roman", 9, "bold"),state='readonly')
        combo_gen['values'] = ("Male","Female","Other")
        combo_gen.grid(row=4,column=1, pady=5, padx=20, sticky="w")

        lbl_dob = Label(Manage_Frame, text="Date of Birth", bg="light blue", fg="black", font=("times new roman", 20, "bold"))
        lbl_dob.grid(row=5, column=0, pady=5, padx=20, sticky="w")

        txt_Dob = Entry(Manage_Frame,textvariable=self.dob_var, font=("times new roman", 13, "bold"), bd=5, relief=GROOVE)
        txt_Dob.grid(row=5, column=1, pady=5, padx=20, sticky="w")

        lbl_con = Label(Manage_Frame, text="Contact", bg="light blue", fg="black",font=("times new roman", 20, "bold"))
        lbl_con.grid(row=6, column=0, pady=5, padx=20, sticky="w")

        txt_con = Entry(Manage_Frame,textvariable=self.contact_var, font=("times new roman", 13, "bold"), bd=5, relief=GROOVE)
        txt_con.grid(row=6, column=1, pady=5, padx=20, sticky="w")

        lbl_add = Label(Manage_Frame, text="Address", bg="light blue", fg="black",font=("times new roman", 20, "bold"))
        lbl_add.grid(row=7, column=0, pady=5, padx=20, sticky="w")
        self.txt_Add = Text(Manage_Frame,width=20,height=3)
        self.txt_Add.grid(row=7, column=1, pady=5, padx=20, sticky="w")


        #====Button Frame=====
        Buttons_Frame = Frame(Manage_Frame, bd=4, relief=RIDGE, bg="light blue")
        Buttons_Frame.place(x=15, y=450, width=420)

        Addbtn = Button(Buttons_Frame,text="Add",command=self.add_Students,width=10)
        Addbtn.grid(row=0,column=0,padx=10)

        Updtbtn = Button(Buttons_Frame,command=self.update, text="Update", width=10)
        Updtbtn.grid(row=0, column=1, padx=10)

        Delbtn = Button(Buttons_Frame,command=self.deletes, text="Delete", width=10)
        Delbtn.grid(row=0, column=2, padx=10)

        Clrbtn = Button(Buttons_Frame, command=self.clear,text="Clear", width=10)
        Clrbtn.grid(row=0, column=3, padx=10)

        # =====Detail Frame======
        Detail_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="light blue")
        Detail_Frame.place(x=500, y=100, width=750, height=580)

        lbl_search = Label(Detail_Frame, text="Search By", bg="light blue", fg="black",
                        font=("times new roman", 10, "bold"))
        lbl_search.grid(row=0, column=0, pady=10, padx=10, sticky="w")

        combo_search = ttk.Combobox(Detail_Frame,textvariable=self.search_by, font=("times new roman", 13, "bold"), state='readonly')
        combo_search['values'] = ("Roll_No", "Name", "Email")
        combo_search.grid(row=0, column=1, pady=10, padx=10, sticky="w")

        txt_Search = Entry(Detail_Frame,textvariable=self.search_txt, font=("times new roman", 13, "bold"), bd=5, relief=GROOVE)
        txt_Search.grid(row=0, column=2, pady=10, padx=10, sticky="w")

        Searchbtn = Button(Detail_Frame,command=self.search_Data, text="Search", width=10)
        Searchbtn.grid(row=0, column=3, padx=10)

        ShowAllbtn = Button(Detail_Frame,command=self.fetch_Data, text="Show All", width=10)
        ShowAllbtn.grid(row=0, column=4, padx=10)

        #========Table Frame=========
        Table_Frame = Frame(Detail_Frame, bd=4, relief=RIDGE, bg="light blue")
        Table_Frame.place(x=10, y=70, width=700, height=450)

        Scrollx=Scrollbar(Table_Frame,orient=HORIZONTAL)
        Scrolly = Scrollbar(Table_Frame, orient=VERTICAL)

        self.Student_Table = ttk.Treeview(Table_Frame,columns=("Roll","Name","Email","Gender","DOB","Contact","Address"),xscrollcommand=Scrollx.set,yscrollcommand=Scrolly.set)

        Scrollx.pack(side=BOTTOM,fill=X)
        Scrolly.pack(side=RIGHT, fill=Y)

        Scrollx.config(command=self.Student_Table.xview)
        Scrolly.config(command=self.Student_Table.yview)

        self.Student_Table.heading("Roll",text="Roll No.")
        self.Student_Table.heading("Name", text="Name")
        self.Student_Table.heading("Email",text="Email")
        self.Student_Table.heading("Gender", text="Gender")
        self.Student_Table.heading("DOB", text="D.O.B")
        self.Student_Table.heading("Contact", text="Contact")
        self.Student_Table.heading("Address", text="Address")

        self.Student_Table['show'] = 'headings'

        self.Student_Table.column("Roll",width=100)
        self.Student_Table.column("Name", width=200)
        self.Student_Table.column("Email", width=200)
        self.Student_Table.column("Gender", width=100)
        self.Student_Table.column("DOB", width=150)
        self.Student_Table.column("Contact", width=200)
        self.Student_Table.column("Address", width=300)

        self.Student_Table.pack(fill=BOTH,expand=1)
        self.Student_Table.bind("<ButtonRelease-1>",self.getCur)
        self.fetch_Data()

    def add_Students(self):
        if self.roll_var.get()=="" or self.name_var.get()=="" or self.dob_var.get()=="" or self.txt_Add.get=="" or self.email_var.get()=="" or self.contact_var.get()=="" or self.gender_var.get()=="":
            messagebox.showerror("Error","Fields are required!!!")
        else:

            con=pymysql.connect(host="localhost",user="root",password="",database="srs")
            cur=con.cursor()
            cur.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s)",(
            self.roll_var.get(),self.name_var.get(),self.email_var.get(),self.gender_var.get(),self.dob_var.get(),
            self.contact_var.get(),self.txt_Add.get('1.0',END)
            ))
            con.commit()
            self.fetch_Data()
            self.clear()
            con.close()
            messagebox.showinfo("Success","Record has been inserted")
    def fetch_Data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="srs")
        cur = con.cursor()
        cur.execute("select * from students")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.Student_Table.delete(*self.Student_Table.get_children())
            for r in rows:
                self.Student_Table.insert('',END,values = r)
            con.commit()
        con.close()

    def clear(self):
        self.roll_var.set("")
        self.name_var.set("")
        self.email_var.set("")
        self.gender_var.set("")
        self.dob_var.set("")
        self.contact_var.set("")
        self.txt_Add.delete("1.0",END)

    def getCur(self,ev):
        cursor_row=self.Student_Table.focus()
        content=self.Student_Table.item(cursor_row)
        row=content['values']
        self.roll_var.set(row[0])
        self.name_var.set(row[1])
        self.email_var.set(row[2])
        self.gender_var.set(row[3])
        self.dob_var.set(row[4])
        self.contact_var.set(row[5])
        self.txt_Add.delete("1.0", END)
        self.txt_Add.insert(END,row[6])

    def update(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="srs")
        cur = con.cursor()
        cur.execute("update students set name=%s,email=%s,gender=%s,dob=%s,contact=%s,address=%s where roll_no=%s", (
             self.name_var.get(), self.email_var.get(), self.gender_var.get(), self.dob_var.get(),
            self.contact_var.get(), self.txt_Add.get('1.0', END),self.roll_var.get()
        ))
        con.commit()
        self.fetch_Data()
        self.clear()
        con.close()

    def deletes(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="srs")
        cur = con.cursor()
        cur.execute("delete from students where roll_no=%s",self.roll_var.get())
        con.commit()
        con.close()
        self.fetch_Data()
        self.clear()

    def search_Data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="srs")
        cur = con.cursor()
        cur.execute("select * from students WHERE "+str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%'")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.Student_Table.delete(*self.Student_Table.get_children())
            for r in rows:
                self.Student_Table.insert('',END,values = r)
            con.commit()
        con.close()


#root=Tk()
#ob=Student(root)
#root.mainloop()