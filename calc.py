from tkinter import *
from functools import partial
from tkinter import simpledialog
from tkinter import messagebox
import mysql.connector
mydb = mysql.connector.connect(host="localhost",user="root",password="123456",database="calcgpa")
cur = mydb.cursor()

#username = "swasti"
#password = "patra"


#closes all existing gui's
def qw():
    n_screen.quit()
    n_screen.destroy()

#reopens gui(1) and the insertion process continues    
def nu():
    n_screen.destroy()
    new_window.deiconify()
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)

#shows grade of the student  
def ge():
    z=((mm1+mm2+mm3)/30)
    if (z==10):
        g=("O")
    elif(z>=9 and z<10):
        g=("E")
    elif(z>=8 and z<9):
        g=("A")
    elif(z>=7 and z<8):
        g=("B")
    elif(z>=6 and z<7):
        g=("C")
    elif(z>=5 and z<6):
        g=("D")
    elif(z<5):
        g=("F")
    ru=Label(n_screen,text=g,font=("Goudy old style",20),bg="yellow").place(x=400,y=190,width=100)

#shows cgpa of the student     
def sz():
    global z
    z=((mm1+mm2+mm3)/30)
    Label(n_screen,text=z,font=("Goudy old style",20),bg="yellow").place(x=400,y=120,width=280)

#gui(3) which consists of buttons to click and get results   
def com():
    screen.withdraw()
    global n_screen
    n_screen=Tk()
    n_screen.geometry("700x500+0+0")
    n_screen.title("CGPA CALCULATOR")
    Button(n_screen,text="CGPA",bg="red",width=15,font=("times new roman",20),command=sz).place(x=90,y=120)
    Button(n_screen,text="GRADE",bg="red",width=15,font=("times new roman",20),command=ge).place(x=90,y=190)
    Button(n_screen,text="NEW INPUT",bg="red",width=15,font=("times new roman",20),command=nu).place(x=90,y=260)
    Button(n_screen,text="CLOSE",bg="red",width=15,font=("times new roman",20),command=qw).place(x=90,y=330)
    su="UPDATE student SET Maths_marks = %s , Chem_marks = %s , PPS_marks = %s WHERE id = %s"
    val = (mm1,mm2,mm3,current_id)
    cur.execute(su,val)
    mydb.commit()

#asks to input marks
def get1():
    global mm1,mm2,mm3
    mm1=simpledialog.askfloat("Input here","Please enter your maths marks")
    mm2=simpledialog.askfloat("Input here","Please enter your chemistry marks")
    mm3=simpledialog.askfloat("Input here","Please enter your pps marks")    

#gui(2) shows the subjects and asks to enter marks which is stored in the database 
def onclick2():
    new_window.withdraw()
    global screen,current_id
    screen=Tk()
    screen.geometry("750x500+0+0")
    screen.title("CGPA CALCULATOR")
    Label(screen,text="Subjects",bg="pink",font=("Impact",40)).pack(side=TOP,fill=X)
    Button(screen,text="MATHS",bg="lightblue",font=("times new roman",20),command=get1).place(x=90,y=160)
    Button(screen,text="CHEMISTRY",bg="lightblue",font=("times new roman",20),command=get1).place(x=90,y=260)
    Button(screen,text="PPS",bg="lightblue",font=("times new roman",20),command=get1).place(x=90,y=360)
    Button(screen,text="Submit",bg="pink",font=("goudy old times",20),command=com).place(x=320,y=420)
    s="INSERT INTO student(Name,Branch,Registration_ID) VALUES(%s,%s,%s)"
    b1=(name.get(),branch.get(),registration_ID.get())
    cur.execute(s,b1)
    row_id = cur.lastrowid
    mydb.commit()
    current_id = row_id

#gui(1) for input window and inputs are stored in a database after clicking submit 
def onclick1():
    if(Username.get() == "swasti" and Password.get() == "patra"): 
        window.destroy()
        global new_window,name,branch,registration_ID,e1,e2,e3
        new_window = Tk()
        new_window.geometry("800x550+0+0")
        new_window.title("CGPA CALCULATOR")
        Label(new_window,text="WELCOME",bg="lightgreen",font=("Impact",45)).pack(side=TOP,fill=X)
        Label(new_window,text="Name",font=("Impact",20)).place(x=90,y=130)
        name = StringVar()
        e1 = Entry(new_window,textvariable=name)
        e1.place(x=90,y=175,width=450,height=35)
        branch=StringVar()
        Label(new_window,text="Branch",font=("Impact",20)).place(x=90,y=215)
        e2 = Entry(new_window,textvariable=branch)
        e2.place(x=90,y=260,width=450,height=35)
        registration_ID=StringVar()
        Label(new_window,text="Registration ID",font=("Impact",20)).place(x=90,y=305)
        e3 = Entry(new_window,textvariable=registration_ID)
        e3.place(x=90,y=350,width=450,height=35)
        su_btn=Button(new_window,text="Submit",bg="lightgreen",font=("times new roman",20),command=onclick2).place(x=300,y=450)
        new_window.mainloop()
    else:
        messagebox.showerror("Error","Invalid Username or Password")


#gui for login page      
window=Tk()
window.geometry("1300x700+0+0")
window.title("CGPA CALCULATOR")
Label(window,text="Login Window",bg="light blue",font=("Impact",50)).pack(side=TOP,fill=X)
Frame_login=Frame(window,bg="pink")
Frame_login.place(x=200,y=200,height=340,width=500)
Label(Frame_login,text="Login Here",font=("times new roman",30,"bold"),bg="pink").pack(side=TOP,fill=X)
Username=StringVar()
Label(Frame_login,text="Username",font=("times new roman",25),bg="pink").place(x=90,y=100)
Entry(Frame_login,textvariable=Username).place(x=90,y=140,width=350,height=35)
Password=StringVar()
Label(Frame_login,text="Password",font=("times new roman",25),bg="pink").place(x=90,y=180)
Entry(Frame_login,textvariable=Password,show='*').place(x=90,y=220,width=350,height=35)
sub_btn=Button(Frame_login,text="Submit",bg="lightblue",font=("times new roman",20),command=onclick1).place(x=200,y=280)
window.mainloop()