#This is the script that i have used to test the GUI My Porject

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
    img.save("Student Images/"+str(reg_var.get())+".png")

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
    
    img1=(Image.open("image.png"))
    resized_image=img1.resize((150,170))
    photo2=ImageTk.PhotoImage(resized_image)
    stud_image_label.config(image=photo2)
    stud_image_label.image=photo2

    img=""


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

#Search Box to Update
search=StringVar()
search_entry=Entry(root,textvariable=search,width=20,bd=2,font="cambria 10").place(x=680,y=70)
search_icon=PhotoImage(file="search.png")
search_icon_resized=search_icon.subsample(30,30)
# Keep a reference of the photo image
root.search_icon_resized = search_icon_resized
search_button=Button(root,text="Search",compound=LEFT,image=search_icon_resized,width=70,font="cambria 10").place(x=830,y=70)

back_arrow=PhotoImage(file="BackArrow.png")
back_arrow=back_arrow.subsample(15,15)
back_arrow_button=Button(root,image=back_arrow,bg="LightBlue",relief=FLAT,activebackground="LightBlue").place(x=10,y=25)

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
roll_no_label_entry=Entry(frame,textvariable=roll_no_var,width=26,font="cambria 12").place(x=135,y=22)

email_label=Label(frame,text="Email ID",bg=back_ground,fg="Black",font="cambria 14").place(x=420,y=20)
email_label_entry=Entry(frame,textvariable=email_var,width=28,font="cambria 12").place(x=560,y=22)

batch_label=Label(frame,text="Batch",bg=back_ground,fg="Black",font="cambria 14").place(x=20,y=70)
batch_label_entry=Entry(frame,textvariable=batch_var,width=26,font="cambria 12").place(x=135,y=72)

mobile_label=Label(frame,text="Mobile Number",bg=back_ground,fg="Black",font="cambria 14").place(x=420,y=70)
mobile_label_entry=Entry(frame,textvariable=mobile_var,width=28,font="cambria 12").place(x=560,y=72)

dob_label=Label(frame,text="Date of Birth",bg=back_ground,fg="Black",font="cambria 14").place(x=20,y=120)
dob_label_entry=Entry(frame,textvariable=dob_var,width=26,font="cambria 12").place(x=135,y=122)

gender_label=Label(frame,text="Gender",bg=back_ground,fg="Black",font="cambria 14").place(x=420,y=120)
gender_label_entry=Entry(frame,textvariable=gender_var,width=28,font="cambria 12").place(x=560,y=122)

aadhaar_label=Label(frame,text="Aadhaar Number",bg=back_ground,fg="Black",font="cambria 14").place(x=20,y=170)
aadhaar_label_entry=Entry(frame,textvariable=aadhaar_var,width=30,font="cambria 12").place(x=170,y=172)

address_label=Label(frame,text="Address",bg=back_ground,fg="Black",font="cambria 14").place(x=20,y=222)
aadhaar_label_entry=Entry(frame,textvariable=address_var,width=50,font="cambria 12").place(x=170,y=222)

update_image=PhotoImage(file="bell.png")
update_image=update_image.subsample(15,15)
update_button=Button(frame,image=update_image,bg="LightBlue",relief=FLAT,activebackground="LightBlue").place(x=790,y=230)


#Image Frame
image_frame=Frame(root,bd=2,bg=back_ground,width=150,height=170,relief="groove")
image_frame.place(x=20,y=80)

img1=(Image.open("image.png"))
resized_image=img1.resize((150,170))
photo2=ImageTk.PhotoImage(resized_image)
stud_image=PhotoImage(file="image.png")
stud_image_label=Label(image_frame,image=photo2)
stud_image_label.place(x=0,y=0)

upload_button=Button(root,text="Clear",bg="gold",fg="white",activebackground="gold",activeforeground="white",font="cambria 12",width=10,relief="groove")
upload_button.place(x=760,y=233)
upload_button.config(command=clear)

upload_button=Button(root,text="Upload Image",bg="salmon",fg="white",activebackground="white",activeforeground="salmon",font="cambria 12",width=10,relief="groove")
upload_button.place(x=650,y=233)
upload_button.config(command=showimage)
root.mainloop() 