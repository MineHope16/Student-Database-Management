from tkinter import * 
import os
from tkinter import filedialog
import sqlite3
from tkinter import messagebox as msg
import smtplib
import random
import regex as re
import datetime as date
from PIL import Image,ImageTk

DATABASE_file="student.db"
TABLE_NAME="students"
USER_TABLE=""
filename=""
img=""

#To create a table The_Student
con=sqlite3.connect(DATABASE_file)
cur_db=con.cursor()
# Create counter table
cur_db.execute("""
    CREATE TABLE IF NOT EXISTS counter (
        next_rollno INTEGER
    );
""")
# Check if the counter table has any records
cur_db.execute("SELECT COUNT(*) FROM counter")
count = cur_db.fetchone()[0]
if count == 0:
    # If no records exist, insert the initial value
    cur_db.execute("INSERT INTO counter (next_rollno) VALUES (237701)")

# Create students table
cur_db.execute("""
    CREATE TABLE IF NOT EXISTS students (
        rollno INTEGER PRIMARY KEY,
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
con.close()


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


def student_window4():
    #for Student
    def showimage():
        global filename
        global img

        filename=filedialog.askopenfilename(initialdir=os.getcwd(),title="Select Image",filetype=(("PNG File","*.png"),("JPG File","*.jpg"),("All Files","*.txt")))
        img=(Image.open(filename))
        resized_image=img.resize((150,170))
        photo2=ImageTk.PhotoImage(resized_image)
        stud_image_label.config(image=photo2)
        stud_image_label.image=photo2
        
        print("Student Images/"+str(reg_var.get())+".png")
        filename="Student Images/"+str(reg_var.get())+".png"
        img.save("Student Images/"+str(reg_var.get())+".png")


    def search_stud():
        a="" #To store the fetched data
        try:
                        
            con=sqlite3.connect(DATABASE_file)
            cur_db=con.cursor()
            cur_db.execute(f"select * from {TABLE_NAME} where email='{USER_TABLE + "@gmail.com"}'")
            a=cur_db.fetchone()            
            cur_db.close

            #Setting textvariable            
            roll_no_var.set(a[0])
            name_var.set(a[1])
            email_var.set(a[2])            
            mobile_var.set(a[4])
            batch_var.set(a[5])
            dob_var.set(a[6])            
            aadhaar_var.set(a[7])
            address_var.set(a[8])
            gender_var.set(a[9])
            reg_var.set(a[0] - 237700)
            img=(Image.open(f"Student Images/"+str(a[0] - 237700)+".png"))
            resized_image=img.resize((150,170))
            photo2=ImageTk.PhotoImage(resized_image)
            stud_image_label.config(image=photo2)
            stud_image_label.image=photo2
                    
        
        except FileNotFoundError as v:
            img=(Image.open("image.png"))
            resized_image=img.resize((150,170))
            photo2=ImageTk.PhotoImage(resized_image)
            stud_image_label.config(image=photo2)
            stud_image_label.image=photo2

        except TclError as t:
            msg.showerror("Wrong Input","Please search the valid Roll No only")
            print(t)

        
        except TypeError as t:
            msg.showerror("Invalid Roll No","You have entered the wrong Roll No")

        except Exception as e:
            msg.showerror("Error has occured","Search only the valid \"Roll No\" of the student")
            print(e)  

    back_ground="LightBlue"

    root=Tk()
    root.title("The Students")
    root.config(bg=back_ground)  # Updated background color

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x_dim = (screen_width - 900) // 2
    y_dim = ((screen_height - 600) // 2)-50

    root.geometry(f"900x700+{x_dim}+{y_dim}")
    root.minsize(900, 600)
    root.maxsize(900, 600)


    #Label for the Title
    l1=Label(root,text=" THE STUDENTS ",font=("Times",30,"bold"),bg="LightBlue",fg="Black",relief="ridge")
    l1.pack(pady=20,fill=X)
    
    back_arrow=PhotoImage(file="BackArrow.png")
    back_arrow=back_arrow.subsample(15,15)
    back_arrow_button=Button(root,image=back_arrow,bg="LightBlue",relief=FLAT,activebackground="LightBlue",command=lambda:[root.destroy(),student_window2()]).place(x=10,y=25)

    #Student Details Frame
    frame=LabelFrame(root,text="Student Details",relief="groove",width=840,height=300,bg=back_ground,fg="Black",font="cambria 15 bold",)
    frame.place(x=20,y=260)

    #TextVariable
    name_var=StringVar()
    roll_no_var=StringVar()
    email_var=StringVar()
    batch_var=StringVar()
    mobile_var=StringVar()
    dob_var=StringVar()
    gender_var=StringVar()
    aadhaar_var=StringVar()
    address_var=StringVar()
    reg_var=StringVar()

    name_label=Label(root,text="Student Name :",bg=back_ground,fg="Gray32",font="cambria 16 bold").place(x=180,y=200)
    name_label_entry=Entry(root,width=26,textvariable=name_var,font="cambria 14",bg=back_ground,relief=FLAT).place(x=335,y=203)
    reg_label=Label(root,text="Registeration No.:",bg=back_ground,fg="Gray32",font="cambria 16 bold").place(x=180,y=230)
    reg_label_entry=Entry(root,width=26,textvariable=reg_var,font="cambria 14",bg=back_ground,relief=FLAT).place(x=365,y=233)


    roll_no_label=Label(frame,text="Roll No",bg=back_ground,fg="Black",font="cambria 14").place(x=20,y=20)
    roll_no_label_entry=Entry(frame,textvariable=roll_no_var,width=26,font="cambria 12",state="readonly").place(x=135,y=22)

    email_label=Label(frame,text="Email ID",bg=back_ground,fg="Black",font="cambria 14").place(x=420,y=20)
    email_label_entry=Entry(frame,textvariable=email_var,width=28,font="cambria 12",state="readonly").place(x=560,y=22)

    batch_label=Label(frame,text="Batch",bg=back_ground,fg="Black",font="cambria 14").place(x=20,y=70)
    batch_label_entry=Entry(frame,textvariable=batch_var,width=26,font="cambria 12",state="readonly").place(x=135,y=72)

    mobile_label=Label(frame,text="Mobile Number",bg=back_ground,fg="Black",font="cambria 14").place(x=420,y=70)
    mobile_label_entry=Entry(frame,textvariable=mobile_var,width=28,font="cambria 12",state="readonly").place(x=560,y=72)

    dob_label=Label(frame,text="Date of Birth",bg=back_ground,fg="Black",font="cambria 14").place(x=20,y=120)
    dob_label_entry=Entry(frame,textvariable=dob_var,width=26,font="cambria 12",state="readonly").place(x=135,y=122)

    gender_label=Label(frame,text="Gender",bg=back_ground,fg="Black",font="cambria 14").place(x=420,y=120)
    gender_label_entry=Entry(frame,textvariable=gender_var,width=28,font="cambria 12",state="readonly").place(x=560,y=122)

    aadhaar_label=Label(frame,text="Aadhaar Number",bg=back_ground,fg="Black",font="cambria 14").place(x=20,y=170)
    aadhaar_label_entry=Entry(frame,textvariable=aadhaar_var,width=30,font="cambria 12",state="readonly").place(x=170,y=172)

    address_label=Label(frame,text="Address",bg=back_ground,fg="Black",font="cambria 14").place(x=20,y=222)
    aadhaar_label_entry=Entry(frame,textvariable=address_var,width=50,font="cambria 12",state="readonly").place(x=170,y=222)
 
    update_image=PhotoImage(file="bell.png")
    update_image=update_image.subsample(15,15)
    update_button=Button(frame,image=update_image,bg="LightBlue",relief=FLAT,activebackground="LightBlue").place(x=790,y=230)

    #Image Frame
    image_frame=Frame(root,bd=3,bg=back_ground,width=150,height=170,relief="groove")
    image_frame.place(x=20,y=80)

    img1=(Image.open("image.png"))
    resized_image=img1.resize((150,170))
    photo2=ImageTk.PhotoImage(resized_image)
    stud_image=PhotoImage(file="image.png")
    stud_image_label=Label(image_frame,image=photo2)
    stud_image_label.pack()   

    upload_button=Button(root,text="Upload Image",bg="salmon",fg="white",activebackground="white",activeforeground="salmon",font="cambria 12",width=10,relief="groove")
    upload_button.place(x=760,y=233)
    upload_button.config(command=showimage)
    search_stud()
    root.mainloop()


def student_window3():    
    #for Institute

    def ind_notify():
        def fetch_emails():
            # Connect to your SQLite database
            conn = sqlite3.connect(DATABASE_file)
            cursor = conn.cursor()

            # Fetch emails from the "notification" table
            cursor.execute(f"SELECT email FROM {TABLE_NAME}")
            emails = cursor.fetchall()

            # Close the connection
            conn.close()

            # Extract emails from the result
            emails_list = ["Select User"]  # Adding "Select User" as the default option
            emails_list.extend([email[0] for email in emails])

            return emails_list


        def send_notification():
            
            try:
                selected_email_value = selected_email.get()
                if selected_email_value=="Select User":
                    raise ValueError("Please select the email")
                notification_subject = "The Students Notification"  # Get the subject from the entry field
                notification_message = notification_text.get("1.0", "end-1c")  # Get the text from the text box
                # SMTP Configuration
                smtp_server = "smtp.gmail.com"
                smtp_port = 587  # TLS Port
                smtp_username = "shubhuu5171@gmail.com"  # Update with your email
                smtp_password = "gzstnwbzcfevtjea"  # Update with your password

                # Create SMTP connection
                with smtplib.SMTP(smtp_server, smtp_port) as server:
                    server.starttls()
                    server.login(smtp_username, smtp_password)

                    # Construct and send the email
                    email_message = f"Subject: {notification_subject}\n\n"
                    email_message += f"Dear Employee,\n\n{notification_message}\n\nBest Regards,\nShubham Navale\n(CEO)"
                    server.sendmail(smtp_username, selected_email_value, email_message)

                
                                    
                
                connection = sqlite3.connect(DATABASE_file)
                cur_db = connection.cursor()
                
                notification_msg = f"{notification_message} - Shubham Navale (CEO)"  # Appending additional information
                
                # Using parameterized queries to prevent SQL injection attacks
                cur_db.execute(f"UPDATE {TABLE_NAME} SET notifi=? WHERE email=?", (notification_msg, selected_email_value))
                
                
                connection.commit()
                msg.showinfo("Email sent successfully",f"The email has sent to {selected_email_value} successfully.")

            except Exception as e:
                msg.showerror("Error has occured !",e)
                print(e)

            finally:
                connection.close()

                
        win1 = Tk()
        win1.title("Notifier")
        win1.config(bg="MediumPurple1")

        screen_width = win1.winfo_screenwidth()
        screen_height = win1.winfo_screenheight()
        x_dim = (screen_width - 500) // 2
        y_dim = (screen_height - 400) // 2

        win1.geometry(f"500x400+{x_dim}+{y_dim}")
        win1.minsize(500, 400)
        win1.maxsize(500, 400)

        # Label for the Title
        l1 = Label(win1, text=" Notifier ", font=("Times", 30, "bold"), bg="MediumPurple1", fg="white", relief="ridge")
        l1.pack(pady=20)

        # Dropdown list for emails
        emails = fetch_emails()
        selected_email = StringVar(win1)
        selected_email.set(emails[0])  # Set default value
        email_dropdown = OptionMenu(win1, selected_email, *emails)
        email_dropdown.pack(pady=10)

        info_label=Label(win1,text="Type the message you want to send",font="arial 10 bold",fg="Black",bg="MediumPurple1")
        info_label.pack(pady=10)

        def on_click(event):
            notification_text.delete("1.0", "end-1c")
            notification_text.config(fg="Black")         

        # Text box for notification message
        notification_text = Text(win1, height=8, width=60, fg="Grey",wrap="word")
        notification_text.insert("1.0", "Type Here...")
        notification_text.bind("<FocusIn>", on_click)
        notification_text.pack(pady=10)

        # Send Notification Button
        b2 = Button(win1, text="Send Notification", relief="groove", font=("arial", 10, "bold"), bg="Salmon", width=30, command=send_notification)
        b2.pack(pady=10)

        # Blank Label
        lblank1 = Label(win1, bg="MediumPurple1")
        lblank1.pack()

        win1.mainloop()


    def mass_notify():
        pass


    def notifi():
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
        l1.pack(pady=5)
        #Blank Label
        lblank1=Label(win1, bg="LightBlue")
        lblank1.pack()

        # Load an image file
        back_arrow_image = PhotoImage(file="BackArrow.png")
        back_arrow_image=back_arrow_image.subsample(15,15)
        # Keep a reference of the photo image
        win1.back_arrow_image = back_arrow_image
        # Create an image button with the correct reference
        button = Button(win1, image=win1.back_arrow_image, bg="LightBlue", borderwidth=0, relief='flat', activebackground="LightBlue", command=lambda: [destry(), student_window3()])
        button.place(x=8, y=8)

        update_image1=PhotoImage(file="bell.png")
        update_image1=update_image1.subsample(3,3)
        update_button=Button(win1,image=update_image1,bg="LightBlue",relief=FLAT,activebackground="LightBlue").place(x=300,y=80)

        update_image11=PhotoImage(file="bell.png")
        update_image11=update_image11.subsample(3,3)
        update_button=Button(win1,image=update_image11,bg="LightBlue",relief=FLAT,activebackground="LightBlue").place(x=30,y=80)

        #Register Button
        b1=Button(win1,text="Individual Notify",relief="groove",font=("arial",13,"bold"),width=20,height=2,bg="DarkOliveGreen1")
        b1.pack(pady=10)
        b1.config(command=lambda:[destry(),ind_notify()])

        #Login Button
        b2=Button(win1,text="Mass Notify",relief="groove",font=("arial",13,"bold"),width=20,height=2,bg="Maroon1")
        b2.pack(pady=10)
        b2.config(command=lambda:[destry(),mass_notify()])

        #Blank Label
        lblank1=Label(win1, bg="LightBlue")
        lblank1.pack()

        win1.mainloop()

    def logO():
        a=msg.askyesno("Logout","Do you want to logout ?")
        if a==True:
            root.destroy()
            app_window1()

    def clear():
        name_var.set(" ")
        roll_no_var.set(" ")
        email_var.set(" ")
        batch_var.set(" ")
        mobile_var.set(" ")
        dob_var.set(" ")
        gender_var.set(" ")
        aadhaar_var.set(" ")
        address_var.set(" ")
        reg_var.set(" ")
        search.set("")
        img1=(Image.open("image.png"))
        resized_image=img1.resize((150,170))
        photo2=ImageTk.PhotoImage(resized_image)
        stud_image_label.config(image=photo2)
        stud_image_label.image=photo2

        img=""

    def search_stud():
        a="" #To store the fetched data
        try:
            search_text=search.get()

            #Establishing the Database Connection
            con=sqlite3.connect(DATABASE_file)
            cur_db=con.cursor()
            cur_db.execute(f"select * from {TABLE_NAME} where rollno='{search_text}'")
            a=cur_db.fetchone()            
            cur_db.close

            #Setting textvariable            
            roll_no_var.set(a[0])
            name_var.set(a[1])
            email_var.set(a[2])            
            mobile_var.set(a[4])
            batch_var.set(a[5])
            dob_var.set(a[6])            
            aadhaar_var.set(a[7])
            address_var.set(a[8])
            gender_var.set(a[9])
            reg_var.set(a[0] - 237700)
            img=(Image.open(f"Student Images/"+str(a[0] - 237700)+".png"))
            resized_image=img.resize((150,170))
            photo2=ImageTk.PhotoImage(resized_image)
            stud_image_label.config(image=photo2)
            stud_image_label.image=photo2
                    
        
        except FileNotFoundError as v:
            img=(Image.open("image.png"))
            resized_image=img.resize((150,170))
            photo2=ImageTk.PhotoImage(resized_image)
            stud_image_label.config(image=photo2)
            stud_image_label.image=photo2

        except TclError as t:
            msg.showerror("Wrong Input","Please search the valid Roll No only")
            print(t)

        
        except TypeError as t:
            msg.showerror("Invalid Roll No","You have entered the wrong Roll No")

        except Exception as e:
            msg.showerror("Error has occured","Search only the valid \"Roll No\" of the student")
            print(e)  

    
    back_ground="LightBlue"

    root=Tk()
    root.title("The Students")
    root.config(bg=back_ground)  # Updated background color

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x_dim = (screen_width - 900) // 2
    y_dim = ((screen_height - 600) // 2)-50

    root.geometry(f"900x700+{x_dim}+{y_dim}")
    root.minsize(900, 600)
    root.maxsize(900, 600)


    #Label for the Title
    l1=Label(root,text=" THE STUDENTS ",font=("Times",30,"bold"),bg="LightBlue",fg="Black",relief="ridge")
    l1.pack(pady=20,fill=X)

    #Search Box to Fetch
    search=IntVar()
    search_entry=Entry(root,textvariable=search,width=20,bd=2,font="cambria 12").place(x=680,y=70)
    search_icon=PhotoImage(file="search.png")
    search_icon_resized=search_icon.subsample(30,30)
    # Keep a reference of the photo image
    root.search_icon_resized = search_icon_resized
    search_button=Button(root,text="Search",compound=LEFT,image=search_icon_resized,width=70,font="cambria 10",command=search_stud).place(x=830,y=70)

    logout=PhotoImage(file="logout.png")
    logout=logout.subsample(15,15)
    logout_button=Button(root,image=logout,bg="LightBlue",relief=FLAT,activebackground="LightBlue",command=logO).place(x=10,y=25)

    #Student Details Frame
    frame=LabelFrame(root,text="Student Details",relief="groove",width=840,height=300,bg=back_ground,fg="Black",font="cambria 15 bold",)
    frame.place(x=20,y=260)

    #TextVariable
    name_var=StringVar()
    roll_no_var=StringVar()
    email_var=StringVar()
    batch_var=StringVar()
    mobile_var=StringVar()
    dob_var=StringVar()
    gender_var=StringVar()
    aadhaar_var=StringVar()
    address_var=StringVar()
    reg_var=StringVar()

    name_label=Label(root,text="Student Name :",bg=back_ground,fg="Gray32",font="cambria 16 bold").place(x=180,y=200)
    name_label_entry=Entry(root,width=26,textvariable=name_var,font="cambria 14",bg=back_ground,relief=FLAT).place(x=335,y=203)
    reg_label=Label(root,text="Registeration No.:",bg=back_ground,fg="Gray32",font="cambria 16 bold").place(x=180,y=230)
    reg_label_entry=Entry(root,width=26,textvariable=reg_var,font="cambria 14",bg=back_ground,relief=FLAT).place(x=365,y=233)


    roll_no_label=Label(frame,text="Roll No",bg=back_ground,fg="Black",font="cambria 14").place(x=20,y=20)
    roll_no_label_entry=Entry(frame,textvariable=roll_no_var,width=26,font="cambria 12",state="readonly").place(x=135,y=22)

    email_label=Label(frame,text="Email ID",bg=back_ground,fg="Black",font="cambria 14").place(x=420,y=20)
    email_label_entry=Entry(frame,textvariable=email_var,width=28,font="cambria 12",state="readonly").place(x=560,y=22)

    batch_label=Label(frame,text="Batch",bg=back_ground,fg="Black",font="cambria 14").place(x=20,y=70)
    batch_label_entry=Entry(frame,textvariable=batch_var,width=26,font="cambria 12",state="readonly").place(x=135,y=72)

    mobile_label=Label(frame,text="Mobile Number",bg=back_ground,fg="Black",font="cambria 14").place(x=420,y=70)
    mobile_label_entry=Entry(frame,textvariable=mobile_var,width=28,font="cambria 12",state="readonly").place(x=560,y=72)

    dob_label=Label(frame,text="Date of Birth",bg=back_ground,fg="Black",font="cambria 14").place(x=20,y=120)
    dob_label_entry=Entry(frame,textvariable=dob_var,width=26,font="cambria 12",state="readonly").place(x=135,y=122)

    gender_label=Label(frame,text="Gender",bg=back_ground,fg="Black",font="cambria 14").place(x=420,y=120)
    gender_label_entry=Entry(frame,textvariable=gender_var,width=28,font="cambria 12",state="readonly").place(x=560,y=122)

    aadhaar_label=Label(frame,text="Aadhaar Number",bg=back_ground,fg="Black",font="cambria 14").place(x=20,y=170)
    aadhaar_label_entry=Entry(frame,textvariable=aadhaar_var,width=30,font="cambria 12",state="readonly").place(x=170,y=172)

    address_label=Label(frame,text="Address",bg=back_ground,fg="Black",font="cambria 14").place(x=20,y=222)
    aadhaar_label_entry=Entry(frame,textvariable=address_var,width=50,font="cambria 12",state="readonly").place(x=170,y=222)

    update_image=PhotoImage(file="bell.png")
    update_image=update_image.subsample(15,15)
    update_button=Button(frame,image=update_image,bg="LightBlue",relief=FLAT,activebackground="LightBlue",command=lambda:[root.destroy(),notifi()]).place(x=790,y=230)


    #Image Frame
    image_frame=Frame(root,bd=3,bg=back_ground,width=150,height=170,relief="groove")
    image_frame.place(x=20,y=80)

    img1=(Image.open("image.png"))
    resized_image=img1.resize((150,170))
    photo2=ImageTk.PhotoImage(resized_image)
    stud_image=PhotoImage(file="image.png")
    stud_image_label=Label(image_frame,image=photo2)
    stud_image_label.pack()

    upload_button=Button(root,text="Clear",bg="gold",fg="white",activebackground="gold",activeforeground="white",font="cambria 12",width=10,relief="groove")
    upload_button.place(x=760,y=233)
    upload_button.config(command=clear)

    
    root.mainloop() 


def student_window2():

    #Logout Funtion
    def logO():
        a=msg.askyesno("Logout","Do you want to logout ?")
        if a==True:
            win1.destroy()
            app_window2()

    #Delete Function
    def stud_delete():
        con=sqlite3.connect(DATABASE_file)
        cur_db=con.cursor()                    
        cur_db.execute(f"select rollno from students where email='{USER_TABLE + "@gmail.com"}'")
        r=cur_db.fetchone()                        
        con.close()
        file_name="Student Images/"+str(r[0] - 237700)+".png"
        print(file_name)
        a=msg.askquestion("Delete Student","Are you sure to delete this student permanently ?")
        print(a)
        
        if a=='yes':
            con=sqlite3.connect(DATABASE_file)
            cur_db=con.cursor()                    
            cur_db.execute(f"delete from students where email='{USER_TABLE + "@gmail.com"}'")                        
            con.commit()
            cur_db.execute(f"drop table {USER_TABLE}")
            con.commit()
            con.close()
            os.remove(file_name)
            a=msg.askquestion("The Students","Student deleted successfully")
            win1.destroy()
            app_window2()
        

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
    l1.pack(pady=10,fill=X)
    l1=Label(win1,text=" DASHBOARD ",font=("Times",24,"bold"),bg="LightBlue",fg="grey",relief="ridge")
    l1.pack(pady=5)
    
    # Load an image file
    logout_image1 = PhotoImage(file="logout.png")
    logout_image1=logout_image1.subsample(15,15)
    # Keep a reference of the photo image
    win1.logout_image1 = logout_image1
    # Create an image button with the correct reference
    button = Button(win1, image=win1.logout_image1, bg="LightBlue", borderwidth=1, relief="groove", activebackground="LightBlue", command=logO)
    button.place(x=5, y=65)

    # Load an image file
    logout_image2 = PhotoImage(file="delete_user.png")
    logout_image2=logout_image2.subsample(14,14)
    # Keep a reference of the photo image
    win1.logout_image2 = logout_image2
    # Create an image button with the correct reference
    button = Button(win1, image=win1.logout_image2, bg="LightBlue", borderwidth=1, relief='groove', activebackground="LightBlue", command=stud_delete)
    button.place(x=460, y=65)

    #Image for Student and Institue Login    
    student_image=(Image.open("student_info.png"))
    resized_image=student_image.resize((80,80))
    photo1=ImageTk.PhotoImage(resized_image)    
    
    edit_image=(Image.open("edit.png"))
    resized_image=edit_image.resize((80,80))
    photo3=ImageTk.PhotoImage(resized_image)

    notification_image=(Image.open("notification.png"))
    resized_image=notification_image.resize((80,80))
    photo2=ImageTk.PhotoImage(resized_image) 
    
        
    #Button for Student and Institute Login
    student_button = Button(win1, image=photo1, text="My Info", compound=TOP,bg="LightBlue", borderwidth=0, activebackground="LightBlue",font="cambria 12")
    student_button.configure(command=lambda:[destry(), student_window4()])
    student_button.place(x=210, y=150)     
   

    My_notification = Button(win1, bg="LightBlue", image=photo2, text="My Notification", compound=TOP ,borderwidth=0, activebackground="LightBlue",font="cambria 12")
    My_notification.place(x=320, y=150)

    profile_edit = Button(win1, bg="LightBlue", image=photo3, text="Edit Profile", compound=TOP ,borderwidth=0, activebackground="LightBlue",font="cambria 12")
    profile_edit.place(x=80, y=150)
    profile_edit.config(command=lambda:[win1.destroy(),student_window1()])
        
    
    #Credit Label
    l2=Label(win1,text="designed by DATTARAM KOLTE",font=("calibri",8,"bold"),bg="LightBlue")
    l2.pack(side=BOTTOM)
    win1.mainloop()


def student_window1():
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
        query=(f"update students set mobile='{mob}',rollno='{roll}',batch='{batch}',dob='{dob}',adhaar='{adh}',address='{addr}',gender='{gen}' where email='{USER_TABLE + "@gmail.com"}'")
        cur_db.execute(query)
        con.commit()
        con.close()
        msg.showinfo("The Students","Information updated successfully")

                
    def update_info():
        con=sqlite3.connect(DATABASE_file)
        cur_db=con.cursor()
        print(USER_TABLE)    
        query=(f"select * from students where email='{USER_TABLE + "@gmail.com"}'")
        print(f"select * from students where email='{USER_TABLE + "@gmail.com"}'")
        cur_db.execute(query)
        a=cur_db.fetchone()
        print(a)
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

    # Creating Profile Window
    root = Tk()
    root.title("The Students")
    root.config(bg="LightBlue")  # Updated background color

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x_dim = (screen_width - 500) // 2
    y_dim = ((screen_height - 700) // 2)-50

    root.geometry(f"500x700+{x_dim}+{y_dim}")
    root.minsize(600, 700)
    root.maxsize(600, 700)

    # Back Arrow
    back_arrow_image = PhotoImage(file="BackArrow.png")
    back_arrow_image=back_arrow_image.subsample(15,15)
    # Keep a reference of the photo image
    root.back_arrow_image = back_arrow_image

    # Create an image button with the correct reference
    button = Button(root, image=root.back_arrow_image, bg="LightBlue", borderwidth=0, relief='flat', activebackground="LightBlue", command=lambda: [root.destroy(), student_window2()])
    button.place(x=10, y=10)

    # Frame to organize labels and entries
    frame = Frame(root, bg="LightBlue", pady=10,relief="groove", borderwidth=5, width=200, height=350)
    frame.place(anchor=NW, x=50, y=100)

    # Inserting an image
    image1 = PhotoImage(file="logopp.png")
    image1 = image1.subsample(18, 18)
    image_label = Label(root, text="Student Info", font="times 14 bold", image=image1, bg="LightBlue", fg="Gray30", compound=TOP)
    image_label.pack(pady=8)

    # Stylish font for labels and entries
    font_style = ("Arial", 14, "bold")

    # Creating Name Label
    l1 = Label(frame, text=" Student Name ", font=font_style, bg="LightBlue", fg="Gray30",relief="groove")  # Updated text and foreground color
    l1.grid(row=0, column=0, pady=10, padx=10, sticky=W)
    # Creating Textbox of Name Label
    e1 = Entry(frame, width=26, font="cambria")
    e1.grid(row=0, column=1, pady=10, padx=10, sticky=W)


    # Creating RollNo Label
    l2 = Label(frame, text=" Roll No ", font=font_style, bg="LightBlue", fg="Gray30",relief="groove")
    l2.grid(row=1, column=0, pady=10, padx=10, sticky=W)
    # Creating RollNo textbox
    e2 = Entry(frame, width=26, font="cambria")
    e2.grid(row=1, column=1, pady=10, padx=10, sticky=W)

    # Creating Batch Label
    l3 = Label(frame, text=" Batch ", font=font_style, bg="LightBlue", fg="Gray30",relief="groove")
    l3.grid(row=2, column=0, pady=10, padx=10, sticky=W)
    # Creating Batch textbox
    e3 = Entry(frame, width=26, font="cambria")
    e3.grid(row=2, column=1, pady=10, padx=10, sticky=W)


    # Creating DOB Label
    l4 = Label(frame, text=" Date of Birth ", font=font_style, bg="LightBlue", fg="Gray30",relief="groove")
    l4.grid(row=3, column=0, pady=10, padx=10, sticky=W)
    # Creating DOB textbox
    e4 = Entry(frame, width=26, font="cambria")
    e4.grid(row=3, column=1, pady=10, padx=10, sticky=W)
    

    # Creating Label and Textbox of Gender
    l5 = Label(frame, font=font_style, bg="LightBlue", fg="Gray30")
    l5.grid(row=4, column=0, pady=10, padx=10, sticky=W)
    l5 = Label(frame, font=font_style, bg="LightBlue", fg="Gray30")
    l5.grid(row=4, column=0, pady=10, padx=10, sticky=W)
    l5 = Label(frame, font=font_style, bg="LightBlue", fg="Gray30")
    l5.grid(row=4, column=0, pady=10, padx=10, sticky=W)

    var1=StringVar()
    var1.set(" ")
    l5=Label(frame,text=" Gender ",font=font_style,bg="LightBlue",fg="Gray30",relief="groove")
    l5.place(anchor=CENTER,x=52,y=215)
    r1=Radiobutton(frame,text="Male",font="cambria 12",activebackground="LightBlue",variable=var1,value="Male",bg="LightBlue")
    r1.place(anchor=CENTER,x=218,y=215)
    r2=Radiobutton(frame,text="Female",font="cambria 12",activebackground="LightBlue",variable=var1,value="Female",bg="LightBlue")
    r2.place(anchor=CENTER,x=418,y=215)

    # Creating Adhaar Number Label
    l6 = Label(frame, text=" Adhaar Number ", font=font_style, bg="LightBlue", fg="Gray30",relief="groove")
    l6.grid(row=5, column=0, pady=10, padx=10, sticky=W)
    # Creating AdhaarNumber textbox
    e6 = Entry(frame, width=26, font="cambria")
    e6.grid(row=5, column=1, pady=10, padx=10, sticky=W)

    # Creating Mobile No Label
    l7 = Label(frame, text=" Mobile Number ", font=font_style, bg="LightBlue", fg="Gray30",relief="groove")
    l7.grid(row=6, column=0, pady=10, padx=10, sticky=W)
    # Creating Textbox of Mobile No Label
    e7 = Entry(frame, width=26, font="cambria")
    e7.grid(row=6, column=1, pady=10, padx=10, sticky=W)


    # Creating Email Label
    l8 = Label(frame, text=" E-mail ID ", font=font_style, bg="LightBlue", fg="Gray30",relief="groove")
    l8.grid(row=7, column=0, pady=10, padx=10, sticky=W)
    # Creating Textbox of Email Label
    e8 = Entry(frame, width=26, font="cambria")
    e8.grid(row=7, column=1, pady=10, padx=10, sticky=W)


    # Creating Address Label
    l9 = Label(frame, text=" Address ", font=font_style, bg="LightBlue", fg="Gray30",relief="groove")
    l9.grid(row=8, column=0, pady=10, padx=10, sticky=W)

    # Creating Textbox of Address Label
    e9 = Text(frame, width=32, height=3, font="cambria 12", wrap=WORD)
    e9.grid(row=8, column=1, pady=10, padx=10, sticky=W)


    # Creating a button to Update
    b1 = Button(root, text="Update", relief="groove", font=font_style, height=1, width=10, bg="#4CAF50", fg="white")  # Updated colors and width
    b1.place(anchor=CENTER, x=310, y=620)
    b1.config(command=stud_update)

    # # Creating a button to Delete
    # b2 = Button(root, text="Delete", relief="groove", font=font_style, height=1, width=10, bg="#FF4C4C", fg="white")  # Updated colors and width
    # b2.place(anchor=CENTER, x=170, y=670)
    # b2.config(command=stud_delete)

    # # Creating a button to back
    # b3 = Button(root, text="Logout", relief="groove", font=font_style, width=10, height=1, bg="#FFD700", fg="black")  # Updated colors and width
    # b3.place(anchor=CENTER, x=310, y=670)
    # b3.config(command=logO)

    # Creating a button to Feedback
    b4 = Button(root, text="Feedback", relief="groove", font=font_style, width=10, height=1, bg="#1E90FF", fg="white")  # Updated colors and width
    b4.place(anchor=CENTER, x=310, y=670)
    b4.config(command=feedback)


    # Colon's
    colon_label=Label(frame,text=":",font=font_style,fg="Black",bg="LightBlue")
    colon_label.place(x=175,y=10)
    colon_label=Label(frame,text=":",font=font_style,fg="Black",bg="LightBlue")
    colon_label.place(x=175,y=58)
    colon_label=Label(frame,text=":",font=font_style,fg="Black",bg="LightBlue")
    colon_label.place(x=175,y=103)
    colon_label=Label(frame,text=":",font=font_style,fg="Black",bg="LightBlue")
    colon_label.place(x=175,y=152)
    colon_label=Label(frame,text=":",font=font_style,fg="Black",bg="LightBlue")
    colon_label.place(x=175,y=248)
    colon_label=Label(frame,text=":",font=font_style,fg="Black",bg="LightBlue")
    colon_label.place(x=175,y=296)
    colon_label=Label(frame,text=":",font=font_style,fg="Black",bg="LightBlue")
    colon_label.place(x=175,y=344)
    colon_label=Label(frame,text=":",font=font_style,fg="Black",bg="LightBlue")
    colon_label.place(x=175,y=415)  


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
                USER_TABLE=email.split('@')[0]
                msg.showinfo('Login Successfully','You have entered valid credentials')
                lr1.destroy()
                er1.destroy()
                lr2.destroy()
                er2.destroy()
                blank_label.config(text="     Login Successfully     ")
                login_button.config(text="Proceed",width=30,bg="white",fg="LightBlue",font="arial 18 bold",height=1,command=lambda:[rootk.destroy(),student_window2()])
                login_button.place(x=18,y=110)

            else:
                msg.showwarning("Invalid Password","You have entered the wrong password.\nTry Again")
                er2.delete(0,"end")
        
        else:
            msg.showerror("Invalid Email ID", "The entered Email ID in not registered.\nKindly register yourself first.")

        

    rootk=Tk()
    rootk.title("The Students")
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

    

    #Creating a blank textbox       
    blank_label=Label(rootk,text="Student Login",bg="LightBlue",fg="white",font="arial 20 bold",width=28,relief=RIDGE)
    blank_label.pack(pady=5,fill=X)
    blabel2=Label(rootk,bg="LightBlue")
    blabel2.pack()
    blabel3=Label(rootk,bg="LightBlue")
    blabel3.pack()
    blabel3=Label(rootk,bg="LightBlue")
    blabel3.pack()
    blabel3=Label(rootk,bg="LightBlue")
    blabel3.pack()
    blabel3=Label(rootk,bg="LightBlue")
    blabel3.pack(pady=15)

    # Back Arrow
    back_arrow_image = PhotoImage(file="BackArrow.png")
    back_arrow_image=back_arrow_image.subsample(18,18)
    # Keep a reference of the photo image
    rootk.back_arrow_image = back_arrow_image
    # Create an image button with the correct reference
    button = Button(rootk, image=rootk.back_arrow_image, bg="LightBlue", borderwidth=0, relief='flat', activebackground="LightBlue", command=lambda: [rootk.destroy(), app_window2()])
    button.place(x=8, y=8)

    #Creating Lable of Email
    lr1=Label(rootk,text="Enter Email ",relief=GROOVE,font=("arial",14,"bold"),bg="LightBlue")
    lr1.place(anchor=CENTER,x=85,y=100)
    #Creating Textbox of Email
    er1=Entry(rootk,width=26,font="calibri")
    er1.place(anchor=CENTER,x=328,y=100)

    #Creating Password Label
    lr2=Label(rootk,text="Enter Password ",relief=GROOVE,font=("arial",14,"bold"),bg="LightBlue")
    lr2.place(anchor=CENTER,x=105,y=145)
    #Creating Password textbox
    er2=Entry(rootk,width=24,show="*",font="calbri")
    er2.place(anchor=CENTER,x=328,y=145)

    def submit_on_enter(event):
        chck_pass()

    login_button=Button(rootk,text="Login",bg="white",fg="LightBlue",height=10,font="arial 12 bold",width=50,relief=GROOVE)
    login_button.pack(anchor=CENTER)
    login_button.config(command=chck_pass)
    # Bind the "Enter" key to the "Submit" button
    login_button.bind('<Return>', submit_on_enter)
    
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
    button = Button(root, image=root.back_arrow_image, bg="LightBlue", borderwidth=0, relief='flat', activebackground="LightBlue", command=lambda: [destry(), app_window2()])
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
                                    USER_TABLE=email.split('@')[0]
                                    msg.showinfo('Login Successfully','You have entered valid credentials')
                                    lr1.destroy()
                                    er1.destroy()
                                    lr2.destroy()
                                    er2.destroy()
                                    blank_label.config(text="     Login Successfully     ")
                                    login_button.config(text="Proceed",width=30,bg="white",fg="LightBlue",font="arial 18 bold",height=1,command=lambda:[rootk.destroy(),student_window2()])
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

                            screen_width = rootk.winfo_screenwidth()
                            screen_height = rootk.winfo_screenheight()
                            x_dim=(screen_width-500)//2
                            y_dim=(screen_height-220)//2
                            
                            rootk.geometry(f"500x220+{x_dim}+{y_dim}")
                            rootk.minsize(500,220)
                            rootk.maxsize(500,220)

                            #Creating a blank textbox                            
                            blank_label=Label(rootk,text="Student Login",bg="LightBlue",fg="white",font="arial 20 bold",width=28,relief=RIDGE)
                            blank_label.pack(pady=5,fill=X)
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
                            blabel3.pack(pady=5)

                            # Back Arrow
                            back_arrow_image = PhotoImage(file="BackArrow.png")
                            back_arrow_image=back_arrow_image.subsample(18,18)
                            # Keep a reference of the photo image
                            rootk.back_arrow_image = back_arrow_image
                            # Create an image button with the correct reference
                            button = Button(rootk, image=rootk.back_arrow_image, bg="LightBlue", borderwidth=0, relief='flat', activebackground="LightBlue", command=lambda: [rootk.destroy(), app_window2()])
                            button.place(x=8, y=8)

                            #Creating Lable of Email
                            lr1=Label(rootk,text="Email ",relief=GROOVE,font=("arial",14,"bold"),bg="LightBlue")
                            lr1.place(anchor=CENTER,x=57,y=100)
                            #Creating Textbox of Email
                            er1=Label(rootk,width=25,text=email,font="calibri",fg="white",bg="LightBlue",justify=LEFT,anchor=W,relief="groove")
                            er1.place(anchor=CENTER,x=320,y=100)

                            #Creating Password Label
                            lr2=Label(rootk,text="Enter Password ",relief=GROOVE,font=("arial",14,"bold"),bg="LightBlue")
                            lr2.place(anchor=CENTER,x=105,y=140)
                            #Creating Password textbox
                            er2=Entry(rootk,width=23,show="*",font="calbri")
                            er2.place(anchor=CENTER,x=320,y=140)

                            def submit_on_enter(event):
                                chck_cred()

                            login_button=Button(rootk,text="Login",bg="white",fg="LightBlue",font="arial 12 bold",height=20,width=50,relief=GROOVE)
                            login_button.pack(anchor=CENTER)
                            login_button.config(command=chck_cred)
                            # Bind the "Enter" key to the "Submit" button
                            login_button.bind('<Return>', submit_on_enter)
                            
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
                        print("HERE1")
                        # Get the next available rollno from the counter table
                        cur_db.execute("SELECT next_rollno FROM counter")
                        next_rollno = cur_db.fetchone()[0]
                        query = f"INSERT INTO {TABLE_NAME} (rollno, name, email, passwd) VALUES ({next_rollno},'{e1.get()}','{e2.get()}','{e4.get()}');"
                        print(query)
                        cur_db.execute(query)
                        # Update the counter table to increment the next_rollno
                        cur_db.execute("UPDATE counter SET next_rollno = next_rollno + 1")
                        con1.commit()
                        print("HERE2")
                        query=f"CREATE TABLE IF NOT EXISTS {USER_TABLE} (id INTEGER PRIMARY KEY AUTOINCREMENT, date VARCHAR(20), title VARCHAR(200),notifi VARCHAR(400));"
                        print(query)
                        cur_db.execute(query)
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
                            b1=Button(rootk,text="Click here to proceed",activebackground="LightBlue",activeforeground="Blue",relief="flat",font=("arial",16,"bold"),bg="LightBlue",fg="White",height=1,command=lambda:[rootk.destroy(),student_window2()])
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


def ins_login():
    def chck_pass():
        # Set focus to a different widget to hide the cursor
        blank_label.focus_set()
        if(er1.get()=="" or er2.get()==""):
            msg.showerror("Error has occured","Pleas enter all the required details")
        else:
            if er1.get()=="admin" and er2.get()=="admin123":
                rootk.destroy()
                student_window3()
            else:
                msg.showerror("Invalid Credentials","You have entered the wrong username or password")
                er1.delete(0,'end')
                er2.delete(0,'end')
        

    rootk=Tk()
    rootk.title("The Students")
    rootk.config(bg="RoyalBlue1")
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
    

    #Creating a blank textbox        
    blank_label=Label(rootk,text="Institute Login",bg="RoyalBlue1",fg="white",font="arial 20 bold",width=28,relief=RIDGE)
    blank_label.pack(pady=5,fill=X)
    blabel2=Label(rootk,bg="RoyalBlue1")
    blabel2.pack()
    blabel3=Label(rootk,bg="RoyalBlue1")
    blabel3.pack()
    blabel3=Label(rootk,bg="RoyalBlue1")
    blabel3.pack()
    blabel3=Label(rootk,bg="RoyalBlue1")
    blabel3.pack()
    blabel3=Label(rootk,bg="RoyalBlue1")
    blabel3.pack()
    blabel3=Label(rootk,bg="RoyalBlue1")
    blabel3.pack(pady=8)
    
   


    # Back Arrow
    back_arrow_image = PhotoImage(file="BackArrow.png")
    back_arrow_image=back_arrow_image.subsample(18,18)
    # Keep a reference of the photo image
    rootk.back_arrow_image = back_arrow_image
    # Create an image button with the correct reference
    button = Button(rootk, image=rootk.back_arrow_image, bg="RoyalBlue1", borderwidth=0, relief='flat', activebackground="RoyalBlue1", command=lambda: [rootk.destroy(), app_window1()])
    button.place(x=8, y=8)

    #Creating Lable of Username
    lr1=Label(rootk,text="Username ",relief=GROOVE,font=("arial",14,"bold"),bg="RoyalBlue1")
    lr1.place(anchor=CENTER,x=105,y=85)
    #Creating Textbox of Username
    er1=Entry(rootk,width=26,font="cambria")
    er1.place(anchor=CENTER,x=328,y=85)

    #Creating Password Label
    lr2=Label(rootk,text="Password ",relief=GROOVE,font=("arial",14,"bold"),bg="RoyalBlue1")
    lr2.place(anchor=CENTER,x=105,y=125)
    #Creating Password textbox
    er2=Entry(rootk,width=26,show="*",font="cambria")
    er2.place(anchor=CENTER,x=328,y=125)

    def submit_on_enter(event):
        chck_pass()

    login_button=Button(rootk,text="Login",bg="white",fg="RoyalBlue1",height=3,font="arial 12 bold",width=50,relief=GROOVE)
    login_button.pack(anchor=CENTER)
    login_button.config(command=chck_pass)
    # Bind the "Enter" key to the "Submit" button
    login_button.bind('<Return>', submit_on_enter)
    
    rootk.mainloop()


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
    con=sqlite3.connect(DATABASE_file)
    cur_insert=con.cursor()
    query=(f"select count(*) from students")
    cur_insert.execute(query)
    a=cur_insert.fetchone()
    l3=Label(win1,text=f"Students Count: {a[0]}",font=("calibri",11,"bold"),bg="LightBlue")
    l3.pack()
    con.close()

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
    institute_button.config(command=lambda:[destry(),ins_login()])
        
    ins_label=Label(win1, text="Institute Login", bg="LightBlue")
    ins_label.place(x=310, y=205)




    #Credit Label
    l2=Label(win1,text="designed by DATTARAM KOLTE",font=("calibri",8,"bold"),bg="LightBlue")
    l2.pack(side=BOTTOM)
    win1.mainloop()

#MAIN EXECUTION
student_window3()