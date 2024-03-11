from tkinter import *
import sqlite3
from tkinter import messagebox as msg
import smtplib
import random
import regex as re

DATABASE_file="student.db"
TABLE_NAME="students"
USER_TABLE=""
#To create a table The_Student
con=sqlite3.connect(DATABASE_file)
cur_db=con.cursor()
cur_db.execute("""
    CREATE TABLE IF NOT EXISTS students (
        rollno INTEGER PRIMARY KEY AUTOINCREMENT DEFAULT 237701,
        name VARCHAR(50),
        email VARCHAR(50),
        passwd VARCHAR(50),
        mobile VARCHAR(10),
        batch VARCHAR(20),
        dob VARCHAR(10),
        adhaar VARCHAR(20),
        address VARCHAR(100),
        gender VARCHAR(20)
    );
""")
con.commit()


# Function to find the table is exist or not
def is_table_exists(table_name):
    # Connect to the SQLite database
    conn = sqlite3.connect(DATABASE_file)
    
    # Create a cursor object to execute SQL queries
    cursor = conn.cursor()
    
    # Execute a query to check if the table exists
    cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}';")
    
    # Fetch the result
    result = cursor.fetchone()
    
    # Close the connection
    conn.close()
    
    # If the result is not None, the table exists
    return result is not None


def student_window():
       
    #Logout Button Function
    def logO():
        a=msg.askyesno("Logout","Do you want to logout ?")
        if a==True:
            root.destroy()
            login_window()

    #Feedback Button Funtion
    def feedback():
        a=msg.askquestion("Feedback","Do you like this Project ?")
        if a=="Yes":
            msg.showinfo("Feedback","Thanks For your Feedback")

        else:
            msg.showinfo("Feedback","We appreciate your kind Feedback")
    
    #Update Button Function
    def stud_update():
        
        name=e1.get()
        print(name)
        mob=e7.get()
        print(mob)
        roll=e2.get()
        print(roll)
        batch=e3.get()
        print(batch)
        dob=e4.get()
        print(dob)
        gen=var1.get()
        print(gen)
        adh=e6.get()
        print(adh)
        addr=e9.get("1.0",END)
        print(addr)

        con=sqlite3.connect(DATABASE_file)
        cur_db=con.cursor()
        query=(f"update students set mobile='{mob}',rollno='{roll}',batch='{batch}',dob='{dob}',adhaar='{adh}',address='{addr}',gender='{gen}' where email='{USER_TABLE}'")
        cur_db.execute(query)
        con.commit()
        con.close()
        msg.showinfo("The Students","Information updated successfully")

    #Delete Button Function
    def stud_delete():
        a=msg.askquestion("Delete Student","Are you sure to delete this student permanently ?")
        print(a)
        print(e1.get())
        if a=='yes':
            con=sqlite3.connect(DATABASE_file)
            cur_db=con.cursor()                    
            cur_db.execute(f"delete from students where email='{USER_TABLE + "@gmail.com"}'")            
            con.commit()
            cur_db.execute(f"drop table {USER_TABLE}")
            con.commit()
            con.close()
            a=msg.askquestion("The Students","Student deleted successfully")
            root.destroy()
            login_window()
            
    def update_info():

        con=sqlite3.connect(DATABASE_file)
        cur_db=con.cursor()
        print(USER_TABLE)    
        query=(f"select * from students where email='{USER_TABLE + "@gmail.com"}'")
        cur_db.execute(query)
        a=cur_db.fetchone()
        #Update Info
        e1.insert(0,a[1])
        e1.config(state=DISABLED)
        e2.insert(0,a[0])
        e2.config(state=DISABLED)
        e8.insert(0,a[2])
        e8.config(state=DISABLED)
        e3.insert(0,a[5])
        e4.insert(0,a[6])
        if a[9]=='':
            var1.set(" ")
        else:
            var1.set(a[9])
        e6.insert(0,a[7])
        e7.insert(0,a[4])    
        e9.insert(INSERT,a[8])   


    #Creating Profile Window    
    root=Tk()
    root.title("The Students")
    root.config(bg="LightBlue")    

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x_dim=(screen_width-500)//2
    y_dim=(screen_height-650)//2
    
    root.geometry(f"500x650+{x_dim}+{y_dim}")
    root.minsize(600,650)
    root.maxsize(600,650) 

    #Creating Name Label
    l1=Label(root,text="Student Name",font=("arial",14,"bold"),bg="lightblue")
    l1.place(anchor=CENTER,x=150,y=130)
    #Creating Textbox of Name Label
    e1=Entry(root,width=26,font="calibri")
    e1.place(anchor=CENTER,x=350,y=130)
    

    #Creating RollNo Label
    l2=Label(root,text="Roll No",font=("arial",14,"bold"),bg="lightblue")
    l2.place(anchor=CENTER,x=155,y=170)
    #Creating RollNo textbox
    e2=Entry(root,width=23,font="calbri")
    e2.place(anchor=CENTER,x=350,y=170)
    
    #Creating Batch Label
    l3=Label(root,text="Batch",font=("arial",14,"bold"),bg="lightblue")
    l3.place(anchor=CENTER,x=155,y=210)
    #Creating Batch textbox
    e3=Entry(root,width=23,font="calbri")
    e3.place(anchor=CENTER,x=350,y=210)

    #Creating DOB Label
    l4=Label(root,text="Date of Birth",font=("arial",14,"bold"),bg="lightblue")
    l4.place(anchor=CENTER,x=155,y=250)
    #Creating DOB textbox
    e4=Entry(root,width=23,font="calbri")
    e4.place(anchor=CENTER,x=350,y=250)

    #Creating Label and Textbox of Gender
    var1=StringVar()
    var1.set(" ")
    l5=Label(root,text="Gender",font=("arial",14,"bold"),bg="lightblue")
    l5.place(anchor=CENTER,x=140,y=290)
    r1=Radiobutton(root,text="Male",font="airal 10 bold",activebackground="lightblue",variable=var1,value="Male",bg="lightblue")
    r1.place(anchor=CENTER,x=270,y=290)
    r2=Radiobutton(root,text="Female",font="arial 10 bold",activebackground="lightblue",variable=var1,value="Female",bg="lightblue")
    r2.place(anchor=CENTER,x=350,y=290)


    #Creating Adhaar Number Label
    l6=Label(root,text="Adhaar Number",font=("arial",14,"bold"),bg="lightblue")
    l6.place(anchor=CENTER,x=150,y=330)
    #Creating AdhaarNumber textbox
    e6=Entry(root,width=22,font="calbri")
    e6.place(anchor=CENTER,x=350,y=330)

    
    #Creating Mobile No Label
    l7=Label(root,text="Mobile Number",font=("arial",14,"bold"),bg="lightblue")
    l7.place(anchor=CENTER,x=150,y=370)
    #Creating Textbox of Mobile No Label
    e7=Entry(root,width=25,font="calibri")
    e7.place(anchor=CENTER,x=350,y=370)

    #Creating Email Label
    l8=Label(root,text="E-mail ID",font=("arial",14,"bold"),bg="lightblue")
    l8.place(anchor=CENTER,x=150,y=410)
    #Creating Textbox of Email Label
    e8=Entry(root,width=25,font="calibri")
    e8.place(anchor=CENTER,x=350,y=410)

    #Creating Address Label
    l9=Label(root,text="Address",font=("arial",14,"bold"),bg="lightblue")
    l9.place(anchor=CENTER,x=150,y=450)
    #Creating Textbox of Address Label
    e9=Text(root,width=25,height=3,font="calibri",wrap=WORD)
    e9.place(anchor=CENTER,x=350,y=470)

    #Creating a button to Update
    b1=Button(root,text="Update",relief="groove",font=("arial",13,"bold"),height=1)
    b1.place(anchor=CENTER,x=260.5,y=570)
    b1.config(command=stud_update)

    #Creating a button to Delete
    b1=Button(root,text="Delete",relief="groove",font=("arial",13,"bold"),height=1)
    b1.place(anchor=CENTER,x=260.5,y=620)
    b1.config(command=stud_delete)
    
    #Creating a button to back
    b2=Button(root,text="Logout",relief="groove",font=("arial",13,"bold"),width=6,height=1)
    b2.place(anchor=CENTER,x=167,y=570)
    b2.config(command=logO)

    #Inserting a image
    image1=PhotoImage(file="logopp.png")
    image1=image1.subsample(18,18)
    image_label=Label(root,text="Student Info",font="times 12 bold",image=image1,bg="lightblue",compound=TOP)
    image_label.pack(pady=8)

    #Creating a button to Feedback    
    b3=Button(root,text="Feedback",relief="groove",font=("arial",13,"bold"),width=8,height=1)
    b3.place(anchor=CENTER,x=360,y=570)
    b3.config(command=feedback)  


    update_info()
    
    root.mainloop()


def login_window():

    def chck_pass():
        # Set focus to a different widget to hide the cursor
        blank_label.focus_set()
        if(er1.get()=="" or er2.get()==""):
            msg.showerror("Error has occured","Pleas enter all the required details")
        else:
            email_pattern = re.compile(r'^[a-zA-Z0-9_.+-]+@gmail\.com$')

            # Check if the e2 matches the pattern
            if email_pattern.match(er1.get()):
                chck_cred()
                
            else:
                er1.delete(0,"end")
                er2.delete(0,"end")
                msg.showinfo("Error has occured","PLease enter the valid Email ID !")



    def chck_cred():
        email=er1.get()
        if is_table_exists(email.split("@")[0]):
            con1=sqlite3.connect(DATABASE_file)
            cur_db=con1.cursor()
            cur_db.execute(f'select passwd from {TABLE_NAME} where email="{email}"')
            a=cur_db.fetchone()
            con1.commit()

            print(a[0])

            if a[0]==er2.get():
                global USER_TABLE
                USER_TABLE=email
                msg.showinfo('Login Successfully','You have entered valid credentials')
                lr1.destroy()
                er1.destroy()
                lr2.destroy()
                er2.destroy()
                blank_label.config(text="     Login Successfully     ")
                login_button.config(text="Proceed",width=30,bg="white",fg="LightBlue",font="arial 18 bold",height=1,command=lambda:[rootk.destroy(),student_window()])
                login_button.place(x=18,y=110)

            else:
                msg.showwarning("Invalid Password","You have entered the wrong password.\nTry Again")
                er2.delete(0,"end")
        
        else:
            msg.showerror("Invalid Email ID", "The entered Email ID in not registered.\nKindly register yourself first.")

        

    rootk=Tk()
    rootk.title("Desktop Notifier")
    rootk.config(bg="LightBlue")
    rootk.geometry("500x220")
    rootk.minsize(500,220)
    rootk.maxsize(500,220)
    
    screen_width = rootk.winfo_screenwidth()
    screen_height = rootk.winfo_screenheight()
    x_dim=(screen_width-500)//2
    y_dim=(screen_height-220)//2
    
    rootk.geometry(f"500x220+{x_dim}+{y_dim}")
    rootk.minsize(500,220)
    rootk.maxsize(500,220)

    # Back Arrow
    back_arrow_image = PhotoImage(file="BackArrow.png")
    back_arrow_image=back_arrow_image.subsample(18,18)
    # Keep a reference of the photo image
    rootk.back_arrow_image = back_arrow_image

    # Create an image button with the correct reference
    button = Button(rootk, image=rootk.back_arrow_image, bg="LightBlue", borderwidth=0, relief='flat', activebackground="LightBlue", command=lambda: [rootk.destroy(), app_window2()])
    button.place(x=10, y=2)

    #Creating a blank textbox
    blabel1=Label(rootk,bg="LightBlue")
    blabel1.pack(pady=10)    
    blank_label=Label(rootk,text="Please enter your Login Credentials",bg="LightBlue",fg="white",font="arial 20 bold",width=28,relief=RIDGE)
    blank_label.pack()
    blabel2=Label(rootk,bg="LightBlue")
    blabel2.pack()
    blabel3=Label(rootk,bg="LightBlue")
    blabel3.pack()
    blabel3=Label(rootk,bg="LightBlue")
    blabel3.pack()
    blabel3=Label(rootk,bg="LightBlue")
    blabel3.pack()
    blabel3=Label(rootk,bg="LightBlue")
    blabel3.pack()

    #Creating Lable of Email
    lr1=Label(rootk,text="Enter Email ",relief=GROOVE,font=("arial",14,"bold"),bg="LightBlue")
    lr1.place(anchor=CENTER,x=85,y=115)
    #Creating Textbox of Email
    er1=Entry(rootk,width=26,font="calibri")
    er1.place(anchor=CENTER,x=328,y=115)

    #Creating Password Label
    lr2=Label(rootk,text="Enter Password ",relief=GROOVE,font=("arial",14,"bold"),bg="LightBlue")
    lr2.place(anchor=CENTER,x=105,y=155)
    #Creating Password textbox
    er2=Entry(rootk,width=24,show="*",font="calbri")
    er2.place(anchor=CENTER,x=328,y=155)

    login_button=Button(rootk,text="Login",bg="white",fg="LightBlue",height=10,font="arial 12 bold",width=50,relief=GROOVE)
    login_button.pack(anchor=CENTER)
    login_button.config(command=chck_pass)
    
    rootk.mainloop()


def register_window():
    root=Tk()
    root.title("The Students")
    root.config(bg="LightBlue")
    
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x_dim=(screen_width-600)//2
    y_dim=(screen_height-650)//2
    
    root.geometry(f"600x460+{x_dim}+{y_dim}")
    root.minsize(600,460)
    root.maxsize(600,600)
    
    # Back Arrow
    back_arrow_image = PhotoImage(file="BackArrow.png")
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
        # Set focus to a different widget to hide the cursor
        l1.focus_set()
        if(e1.get()=="" or e2.get()=="" or e3.get()=="" or e4.get()==""):
            blabel.config(text="Please enter all the required details for registeration!")
        else:
            email_pattern = re.compile(r'^[a-zA-Z0-9_.+-]+@gmail\.com$')

            # Check if the e2 matches the pattern
            if email_pattern.match(e2.get()):
                if((e3.get())==(e4.get())):
                    e3.config(fg="black")
                    blabel.config(text="")
                    email=e2.get()

                    if is_table_exists(email.split('@')[0]):
                        clr()
                        a=msg.askyesno("Email ID already exist","If you wish to Login to the entered email\nClick \"OK\"")
                        print(a)

                        if a==True:
                            print(email)
                            root.destroy()

                            #TO check the entered password is right or wrong
                            def chck_cred():
                                con1=sqlite3.connect(DATABASE_file)
                                cur_db=con1.cursor()
                                cur_db.execute(f'select passwd from {TABLE_NAME} where email="{email}"')
                                a=cur_db.fetchone()
                                con1.commit()

                                print(a[0])

                                if a[0]==er2.get():
                                    global USER_TABLE
                                    USER_TABLE=email
                                    msg.showinfo('Login Successfully','You have entered valid credentials')
                                    lr1.destroy()
                                    er1.destroy()
                                    lr2.destroy()
                                    er2.destroy()
                                    blank_label.config(text="     Login Successfully     ")
                                    login_button.config(text="Proceed",width=30,bg="white",fg="LightBlue",font="arial 18 bold",height=1,command=lambda:[rootk.destroy(),student_window()])
                                    login_button.place(x=18,y=110)

                                else:
                                    
                                    msg.showwarning("Invalid Password","You have entered the wrong password.\nTry Again")
                                    er2.delete(0,"end")
                            rootk=Tk()
                            rootk.title("The Students")
                            rootk.config(bg="LightBlue")
                            rootk.geometry("500x220")
                            rootk.minsize(500,220)
                            rootk.maxsize(500,220)

                            #Creating a blank textbox
                            blabel1=Label(rootk,bg="LightBlue")
                            blabel1.pack()
                            blank_label=Label(rootk,text="Please enter your Login Credentials",bg="LightBlue",fg="white",font="arial 20 bold",width=28,relief=RIDGE)
                            blank_label.pack()
                            blabel2=Label(rootk,bg="LightBlue")
                            blabel2.pack()
                            blabel3=Label(rootk,bg="LightBlue")
                            blabel3.pack()
                            blabel3=Label(rootk,bg="LightBlue")
                            blabel3.pack()
                            blabel3=Label(rootk,bg="LightBlue")
                            blabel3.pack()
                            blabel3=Label(rootk,bg="LightBlue")
                            blabel3.pack()
                            blabel3=Label(rootk,bg="LightBlue")
                            blabel3.pack()

                            #Creating Lable of Email
                            lr1=Label(rootk,text="Email ",relief=GROOVE,font=("arial",14,"bold"),bg="LightBlue")
                            lr1.place(anchor=CENTER,x=57,y=100)
                            #Creating Textbox of Email
                            er1=Label(rootk,width=25,text=email,font="calibri",fg="white",bg="LightBlue",justify=LEFT,anchor=W,relief="groove")
                            er1.place(anchor=CENTER,x=300,y=100)

                            #Creating Password Label
                            lr2=Label(rootk,text="Enter Password ",relief=GROOVE,font=("arial",14,"bold"),bg="LightBlue")
                            lr2.place(anchor=CENTER,x=105,y=140)
                            #Creating Password textbox
                            er2=Entry(rootk,width=23,show="*",font="calbri")
                            er2.place(anchor=CENTER,x=320,y=140)

                            login_button=Button(rootk,text="Login",bg="white",fg="LightBlue",font="arial 12 bold",height=20,width=50,relief=GROOVE)
                            login_button.pack(anchor=CENTER)
                            login_button.config(command=chck_cred)
                            
                            rootk.mainloop()
                    else:
                        register_DB()
                else:
                    e4.config(fg="red")
                    blabel.config(text="Password does not match !")
            else:
                e2.config(fg="red")
                blabel.config(text="PLease enter the valid Email ID !")


                
    #Creating Funtion of Clear button
    def clr():
        e1.delete(first=0,last=300)
        e2.delete(first=0,last=300)
        e3.delete(first=0,last=300)
        e4.delete(first=0,last=300)
        blabel.config(text="")


    #Connection of Database
    def register_DB():
            def verify():
                if(OTP1 == E2.get()):
                    try:
                        root1.destroy()
                        con1=sqlite3.connect(DATABASE_file)
                        cur_db=con1.cursor()
                        user_email=e2.get()
                        user_email=user_email.split('@')[0]
                        global USER_TABLE
                        USER_TABLE=user_email
                        query = f"INSERT INTO {TABLE_NAME} (name, email, passwd) VALUES ('{e1.get()}', '{e2.get()}', '{e4.get()}')"
                        cur_db.execute(query)
                        cur_db.execute(f"""
                            CREATE TABLE IF NOT EXISTS {USER_TABLE} (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                name VARCHAR(50),
                                notifi VARCHAR(200)
                            );
                        """)
                        con1.commit()
                        con1.close()
                        a=msg.showinfo('Successfull Execution','User registeration successfully')
                        print(a)
                        if a=="ok":                            
                            root.destroy()                            
                            rootk=Tk()
                            rootk.title("The Students")
                            rootk.config(bg="LightBlue")
                            screen_width = rootk.winfo_screenwidth()
                            screen_height = rootk.winfo_screenheight()
                            x_dim=(screen_width-500)//2
                            y_dim=(screen_height-150)//2
                            
                            rootk.geometry(f"500x300+{x_dim}+{y_dim}")
                            rootk.minsize(500,150)
                            rootk.maxsize(500,150)

                            #Creating a blank textbox
                            blabel1=Label(rootk,bg="LightBlue")
                            blabel1.pack()

                            blabel=Label(rootk,text="You have successfully registered now...",bg="LightBlue",fg="white",font="cambria 18 bold",width=35,relief=FLAT)
                            blabel.pack()

                            blabel2=Label(rootk,bg="LightBlue")
                            blabel2.pack()                        


                            #Creating a button to Register
                            b1=Button(rootk,text="Click here to proceed",activebackground="LightBlue",activeforeground="Blue",relief="flat",font=("arial",16,"bold"),bg="LightBlue",fg="White",height=1,command=lambda:[rootk.destroy(),student_window()])
                            b1.pack()
                            rootk.mainloop()


                        
                    except Exception as e:
                        print(e)
                        msg.showinfo("Unsuccessfull Execution","Error occured while Registering. Please retry")
                        clr()
                else:
                    msg.showinfo("Invalid OTP","Check your OTP again")
                    print("Check your OTP again")
            
            
            ####### Resgiter DB #########
            OTP1=str(random.randint(1000,9999))
            try:                
                email = e2.get()                
                notification_subject = "One Time Password (OTP) for Student Database Management"  # Get the subject from the entry field                
                # SMTP Configuration
                smtp_server = "smtp.gmail.com"
                smtp_port = 587  # TLS Port
                smtp_username = "minehope16@gmail.com"  # Update with your email
                smtp_password = "lhtjdviuanqumahw"  # Update with your password

                # Create SMTP connection
                with smtplib.SMTP(smtp_server, smtp_port) as server:
                    server.starttls()
                    server.login(smtp_username, smtp_password)

                    # Construct and send the email
                    email_message = f"Subject: {notification_subject}\n\n"
                    email_message += f"Dear Student,\n\nThe one time password for your registeration is {OTP1}.\nThank you for using our services. \n\nBest Regards,\nDattaram Kolte"
                    server.sendmail(smtp_username, email, email_message)


            except Exception as e:
                msg.showerror("Error has occured !",e)
                print(e)
                        

            def on_entry_click(event):
                E2.delete(0, 'end')  # Clear the default text when clicked
                E2.config(fg='black')  # Change text color to black

            def submit_on_enter(event):
                verify()

            root1 = Tk()
            root1.geometry("400x100")
            root1.title("OTP Verification")
            root1.config(background="LightBlue")

            screen_width = root1.winfo_screenwidth()
            screen_height = root1.winfo_screenheight()
            x_dim=((screen_width-400)//2)+300
            y_dim=((screen_height-100)//2)-200
            
            root1.geometry(f"400x100+{x_dim}+{y_dim}")
            root1.minsize(400,100)
            root1.maxsize(400,100)

            l1 = Label(root1, text=" The Students ", font=("Times", 15, "bold"), bg="LightBlue", fg="white", relief="ridge")
            l1.pack(pady=10)

            l2 = Label(root1, text="Enter OTP:", font=('Calibri', 10, 'bold'), bg="salmon")
            l2.place(x=30, y=60)

            E2 = Entry(root1, font=('Calibri', 10, 'bold'),fg="Grey")
            E2.insert(0, "Enter OTP")  # Set default text
            E2.bind("<FocusIn>", on_entry_click)  # Bind focus event
            E2.place(x=120, y=60)
            E2.focus_set()  # Set focus to the entry field

            B2 = Button(root1, text='Submit', command=verify, font=('Calibri', 8, 'bold'), bg="bisque", relief=GROOVE)
            B2.place(x=280, y=60)

            # Bind the "Enter" key to the "Submit" button
            root1.bind('<Return>', submit_on_enter)

            root1.mainloop()

    ########## Register Controlls #########
    # Inserting an image
    image1 = PhotoImage(file="logo.png")
    image1 = image1.subsample(18, 18)
    image_label = Label(root, text="REGISTER", font="times 12 bold", image=image1, bg="lightblue", compound=TOP)
    image_label.pack(pady=8)

    # Controls Frame
    frame1 = Frame(root, relief="groove", borderwidth=5, bg="LightBlue", width=550, height=200)
    frame1.pack()

    # Name Label & Entry
    l1 = Label(frame1, text="Enter Name:", font=("calibri", 14, "bold"), bg="lightblue")
    l1.place(x=10, y=10)
    e1 = Entry(frame1, width=35, font="calibri")
    e1.place(x=175, y=10)

    # Bind function for the Email entry and Passworsd Entry
    def on_entry_click(event):
        e2.config(fg="black")
        e4.config(fg="black")
        blabel.config(text="")
    # Email Label & Entry
    l2 = Label(frame1, text="Enter Email:", font=("calibri", 14, "bold"), bg="lightblue")
    l2.place(x=10, y=50)
    e2 = Entry(frame1, width=35, font="calibri")
    e2.bind("<FocusIn>", on_entry_click)
    e2.place(x=175, y=50)

    # Password Label & Entry
    l3 = Label(frame1, text="Enter Password:", font=("calibri", 14, "bold"), bg="lightblue")
    l3.place(x=10, y=90)
    e3 = Entry(frame1, width=35, font="calibri",show="*")
    e3.place(x=175, y=90)

    # Re-Enter Password Label & Entry
    l4 = Label(frame1, text="Re-Enter Password:", font=("calibri", 14, "bold"), bg="lightblue")
    l4.place(x=10, y=130)
    e4 = Entry(frame1, width=35, font="calibri")
    e4.bind("<FocusIn>", on_entry_click)
    e4.place(x=175, y=130)

    # Creating a blank textbox
    blabel = Label(root, text="", bg="LightBlue", fg="red", font="arial 12 bold", width=40, anchor="center", justify="center")
    blabel.place(x=100, y=307)

    # Creating a button to Register
    register_button = Button(root, text="Register", relief="groove", font=("arial", 13, "bold"), height=1, command=chck_pass, padx=20, pady=5, bg="green", fg="white")
    register_button.place(anchor=CENTER, x=290.5, y=375)

    # Creating a button to clear
    clear_button = Button(root, text="Clear", relief="groove", font=("arial", 13, "bold"), width=6, height=1, command=clr, padx=20, pady=5, bg="orange", fg="white")
    clear_button.place(anchor=CENTER, x=192, y=428)

    # Creating a button to back
    back_button = Button(root, text="Back", relief="groove", font=("arial", 13, "bold"), width=6, height=1, command=lambda: [destry(), app_window1()], padx=20, pady=5, bg="blue", fg="white")
    back_button.place(anchor=CENTER, x=390, y=428)

    # Start the Tkinter main loop
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
    back_arrow_image = PhotoImage(file="BackArrow.png")
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
    b2.config(command=lambda:[destry(),login_window()])

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
    student_image = PhotoImage(file='Student.png')
    institute_image = PhotoImage(file='College.png')
        
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