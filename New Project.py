from tkinter import *
import sqlite3 as m
from tkinter import messagebox as mb

DATABASE_file="student.db"

#To create a table The_Student
con=m.connect(DATABASE_file)
cur_db=con.cursor()
cur_db.execute("create table if not exists students(name varchar(50), passwd varchar(50), mobile varchar(10), email varchar(50), rollno varchar(10), batch varchar(20), dob varchar(10), adhaar varchar(20), address varchar(100), gender varchar(20));")      
con.commit()


def register_window():
    root=Tk()
    root.title("The Students")
    root.config(bg="LightBlue")
    
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x_dim=(screen_width-600)//2
    y_dim=(screen_height-650)//2
    
    root.geometry(f"600x600+{x_dim}+{y_dim}")
    root.minsize(600,600)
    root.maxsize(600,600)
    
    # Back Arrow
    back_arrow_image = PhotoImage(file=r"C:\Users\admin\Downloads\GitHub\Student-Database-Management\BackArrow.png")
    back_arrow_image=back_arrow_image.subsample(15,15)
    # Keep a reference of the photo image
    root.back_arrow_image = back_arrow_image

    # Create an image button with the correct reference
    button = Button(root, image=root.back_arrow_image, bg="LightBlue", borderwidth=0, relief='flat', activebackground="LightBlue", command=lambda: [destry(), app_window1()])
    button.place(x=10, y=10)

    #To destroy the window
    def destry():
        root.destroy()

    #Functions related to Register Button
    def chck_pass():
        if(e1.get()=="" or e2.get()=="" or e3.get()=="" or e4.get()=="" or e5.get()==""):
            blabel.config(text="Please enter all the required details for registeration!")
        else:
            if((e2.get())==(e3.get())):
                e3.config(fg="black")
                blabel.config(text="")
                register_DB()    
            else:
                e3.config(fg="red")
                blabel.config(text="Password does not match !")

    #Creating Funtion of Clear button
    def clr():
        e1.delete(first=0,last=300)
        e2.delete(first=0,last=300)
        e3.delete(first=0,last=300)
        e4.delete(first=0,last=300)
        e5.delete(first=0,last=300)
        blabel.config(text="")

    #Connection of Database
    def register_DB():
        try:
            query=(f"insert into students values('{e1.get()}','{e2.get()}',{e4.get()},'{e5.get()}','','','','','','')")
            con=m.connect(DATABASE_file)
            cur_db=con.cursor()
            a=cur_db.execute(query)
            con.commit()
            mb.showinfo('Successfull Execution','Student registeration successfully')
            clr()

        except Exception:
            mb.showinfo("Unsuccessfull Execution","Error occured while Registering. Please retry")
            clr()


    #Inserting a image
    image1=PhotoImage(file="Student-Database-Management\logo.png")
    image1=image1.subsample(18,18)
    image_label=Label(root,text="REGISTER",font="times 12 bold",image=image1,bg="lightblue",compound=TOP)
    image_label.pack(pady=8)

    #Controls Frame
    frame1 = Frame(root, relief="groove", borderwidth=5, bg="LightBlue", width=550, height=430)
    frame1.pack()

    #Name Label & Entry
    l1=Label(frame1, text="Enter Name :",font=("calibri",14,"bold"),bg="lightblue")
    l1.place(x=10, y=10)
    e1=Entry(frame1, width=40, font="calibri")
    e1.place(x=150, y=10)



    
    root.mainloop()



















def app_window2():
    #Creating the application window ( " The Students " )
    win1=Tk()
    win1.title("The Students")
    win1.config(bg="LightBlue")

    screen_width = win1.winfo_screenwidth()
    screen_height = win1.winfo_screenheight()
    x_dim=(screen_width-500)//2
    y_dim=(screen_height-350)//2
    
    win1.geometry(f"500x280+{x_dim}+{y_dim}")
    win1.minsize(500,280)
    win1.maxsize(500,280)
    
    # Load an image file
    back_arrow_image = PhotoImage(file=r"c:\Users\admin\Downloads\GitHub\Student-Database-Management\BackArrow.png")
    back_arrow_image=back_arrow_image.subsample(15,15)
    # Keep a reference of the photo image
    win1.back_arrow_image = back_arrow_image

    # Create an image button with the correct reference
    button = Button(win1, image=win1.back_arrow_image, bg="LightBlue", borderwidth=0, relief='flat', activebackground="LightBlue", command=lambda: [destry(), app_window1()])
    button.place(x=10, y=10)

    
    #To destroy the window
    def destry():
        win1.destroy()

    #Label for the Title
    l1=Label(win1,text=" THE STUDENTS ",font=("Times",30,"bold"),bg="LightBlue",fg="grey",relief="ridge")
    l1.pack(pady=40)

    #Register Button
    b1=Button(win1,text="Register",relief="groove",font=("arial",13,"bold"),width=15,height=1)
    b1.pack()
    b1.config(command=lambda:[destry(),register_window()])

    #Login Button
    b2=Button(win1,text="Login",relief="groove",font=("arial",13,"bold"),width=15,height=1)
    b2.pack(pady=10)
    b2.config()

    #Blank Label
    lblank1=Label(win1, bg="LightBlue")
    lblank1.pack()
    
    #Student Count
    cur_insert=con.cursor()
    query=(f"select count(*) from students")
    cur_insert.execute(query)
    a=cur_insert.fetchone()
    l3=Label(win1,text=f"Students Count: {a[0]}",font=("calibri",11,"bold"),bg="LightBlue")
    l3.pack()

    #Credit Label
    l2=Label(win1,text="designed by DATTARAM KOLTE",font=("calibri",8,"bold"),bg="LightBlue")
    l2.pack()   

    win1.mainloop()

    
def app_window1():
    #Creating the application window ( " The Students " )
    win1=Tk()
    win1.title("The Students")
    win1.config(bg="LightBlue")

    screen_width = win1.winfo_screenwidth()
    screen_height = win1.winfo_screenheight()
    x_dim=(screen_width-500)//2
    y_dim=(screen_height-350)//2
        
    win1.geometry(f"500x280+{x_dim}+{y_dim}")
    win1.minsize(500,280)
    win1.maxsize(500,280)
        
    #To destroy the window
    def destry():
        win1.destroy()

    #Label for the Title
    l1=Label(win1,text=" THE STUDENTS ",font=("Times",30,"bold"),bg="LightBlue",fg="grey",relief="ridge")
    l1.pack(pady=40)
        
    #Image for Student and Institue Login
    student_image = PhotoImage(file=r'C:\Users\admin\Downloads\GitHub\Student-Database-Management\Student.png')
    institute_image = PhotoImage(file=r'C:\Users\admin\Downloads\GitHub\Student-Database-Management\College.png')
        
    #Button for Student and Institute Login
    student_button = Button(win1, image=student_image, text="Student Login", bg="LightBlue", borderwidth=0, activebackground="LightBlue")
    student_button.configure(command=lambda:[destry(), app_window2()])
    student_button.place(x=100, y=110)
        
    student_label=Label(win1, text="Student Login", bg="LightBlue")
    student_label.place(x=110, y=205)

    institute_button = Button(win1, bg="LightBlue", image=institute_image, text="Institute Login", borderwidth=0, activebackground="LightBlue")
    institute_button.place(x=300, y=108)
        
    ins_label=Label(win1, text="Institute Login", bg="LightBlue")
    ins_label.place(x=310, y=205)




    #Credit Label
    l2=Label(win1,text="designed by DATTARAM KOLTE",font=("calibri",8,"bold"),bg="LightBlue")
    l2.pack(side=BOTTOM)
    win1.mainloop()



#MAIN EXECUTION
app_window1()