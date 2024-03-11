from tkinter import * 
from tkinter import *
import sqlite3
from tkinter import messagebox as msg
import smtplib
import random
import regex as re
import datetime as date

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
image_frame=Frame(root,bd=2,bg=back_ground,width=150,height=170,relief="ridge")
image_frame.place(x=20,y=80)

stud_image=PhotoImage(file="image.png")
stud_image_label=Label(image_frame,image=stud_image).place(x=0,y=0)



root.mainloop()