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
                                    global USER_email
                                    USER_email=email
                                    msg.showinfo('Login Successfully','You have entered valid credentials')
                                    lr1.destroy()
                                    er1.destroy()
                                    lr2.destroy()
                                    er2.destroy()
                                    blank_label.config(text="     Login Successfully     ")
                                    login_button.config(text="Proceed",width=30,bg="white",fg="LightBlue",font="arial 18 bold",height=1,command=lambda:[rootk.destroy(),app_window()])
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
                            clr()
                            global USER_email
                            USER_email=user_email
                            root.destroy()

                            rootk=Tk()
                            rootk.title("The Students")
                            rootk.config(bg="LightBlue")
                            rootk.geometry("400x200")
                            rootk.minsize(400,200)
                            rootk.maxsize(400,200)

                            #Creating a blank textbox
                            blabel1=Label(rootk,bg="LightBlue")
                            blabel1.pack()

                            blabel=Label(rootk,text="Click  \"LOGIN\"  to continue...",bg="LightBlue",fg="white",font="arial 20 bold",width=28,relief=RIDGE)
                            blabel.pack()

                            blabel2=Label(rootk,bg="LightBlue")
                            blabel2.pack()

                            blabel3=Label(rootk,bg="LightBlue")
                            blabel3.pack()


                            #Creating a button to Register
                            b1=Button(rootk,text="Login",relief="groove",font=("arial",16,"bold"),height=1,command=lambda:[rootk.destroy(),app_window()])
                            b1.pack()
                            rootk.mainloop()


                        
                    except Exception as e:
                        print(e)
                        msg.showinfo("Unsuccessfull Execution","Error occured while Registering. Please retry")
                        clr()
                else:
                    msg.showinfo("Invalid OTP","Check your OTP again")
                    print("Check your OTP again")

            OTP1=str(random.randint(1000,9999))
            
            s=smtplib.SMTP_SSL("smtp.gmail.com",465)
            s.login('shubhuu5171@gmail.com',"gzstnwbzcfevtjea")
            send_to=e2.get()
            msgg=f"The OPT for Student registeration is {OTP1} \n\nThanks for choosing us."
            s.sendmail('shubhuu5171@gmail.com',send_to,msgg)

            def on_entry_click(event):
                E2.delete(0, 'end')  # Clear the default text when clicked
                E2.config(fg='black')  # Change text color to black

            def submit_on_enter(event):
                verify()

            root1 = Tk()
            root1.geometry("400x100")
            root1.title("OTP Verification")
            root1.config(background="LightBlue")

            l1 = Label(root1, text=" Notifier ", font=("Times", 15, "bold"), bg="LightBlue", fg="white", relief="ridge")
            l1.pack(pady=10)

            l2 = Label(root1, text="Enter OTP:", font=('Calibri', 10, 'bold'), bg="salmon")
            l2.place(x=30, y=60)

            E2 = Entry(root1, font=('Calibri', 10, 'bold'))
            E2.insert(0, "Enter OTP")  # Set default text
            E2.bind("<FocusIn>", on_entry_click)  # Bind focus event
            E2.place(x=120, y=60)
            E2.focus_set()  # Set focus to the entry field

            B2 = Button(root1, text='Submit', command=verify, font=('Calibri', 8, 'bold'), bg="bisque", relief=GROOVE)
            B2.place(x=280, y=60)

            # Bind the "Enter" key to the "Submit" button
            root1.bind('<Return>', submit_on_enter)

            root1.mainloop()


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
register_window()