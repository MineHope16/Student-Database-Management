from tkinter import *

def stud_update():
    # Add your update logic here
    pass

def stud_delete():
    # Add your delete logic here
    pass

def logO():
    # Add your logout logic here
    pass

def feedback():
    # Add your feedback logic here
    pass

def update_info():
    pass

# Creating Profile Window
root = Tk()
root.title("The Students")
root.config(bg="#4DA6FF")  # Updated background color

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_dim = (screen_width - 500) // 2
y_dim = ((screen_height - 700) // 2)-50

root.geometry(f"500x700+{x_dim}+{y_dim}")
root.minsize(600, 700)
root.maxsize(600, 700)

# Frame to organize labels and entries
frame = Frame(root, bg="#4DA6FF", padx=20, pady=10,relief="groove", borderwidth=5, width=200, height=350)
frame.place(anchor=NW, x=50, y=100)

# Inserting an image
image1 = PhotoImage(file="logopp.png")
image1 = image1.subsample(18, 18)
image_label = Label(root, text="Student Info", font="times 12 bold", image=image1, bg="#4DA6FF", fg="white", compound=TOP)
image_label.pack(pady=8)

# Stylish font for labels and entries
font_style = ("Arial", 14, "bold")

# Creating Name Label
l1 = Label(frame, text=" Student Name ", font=font_style, bg="#4DA6FF", fg="white",relief="groove")  # Updated text and foreground color
l1.grid(row=0, column=0, pady=10, padx=10, sticky=W)
# Creating Textbox of Name Label
e1 = Entry(frame, width=26, font="calibri")
e1.grid(row=0, column=1, pady=10, padx=10, sticky=W)

# Creating RollNo Label
l2 = Label(frame, text=" Roll No       ", font=font_style, bg="#4DA6FF", fg="white",relief="groove")
l2.grid(row=1, column=0, pady=10, padx=10, sticky=W)
# Creating RollNo textbox
e2 = Entry(frame, width=26, font="calibri")
e2.grid(row=1, column=1, pady=10, padx=10, sticky=W)

# Creating Batch Label
l3 = Label(frame, text=" Batch ", font=font_style, bg="#4DA6FF", fg="white",relief="groove")
l3.grid(row=2, column=0, pady=10, padx=10, sticky=W)
# Creating Batch textbox
e3 = Entry(frame, width=26, font="calibri")
e3.grid(row=2, column=1, pady=10, padx=10, sticky=W)


# Creating DOB Label
l4 = Label(frame, text=" Date of Birth ", font=font_style, bg="#4DA6FF", fg="white",relief="groove")
l4.grid(row=3, column=0, pady=10, padx=10, sticky=W)
# Creating DOB textbox
e4 = Entry(frame, width=26, font="calibri")
e4.grid(row=3, column=1, pady=10, padx=10, sticky=W)
 

# Creating Label and Textbox of Gender
l5 = Label(frame, font=font_style, bg="#4DA6FF", fg="white")
l5.grid(row=4, column=0, pady=10, padx=10, sticky=W)
l5 = Label(frame, font=font_style, bg="#4DA6FF", fg="white")
l5.grid(row=4, column=0, pady=10, padx=10, sticky=W)
l5 = Label(frame, font=font_style, bg="#4DA6FF", fg="white")
l5.grid(row=4, column=0, pady=10, padx=10, sticky=W)

var1=StringVar()
var1.set(" ")
l5=Label(frame,text=" Gender ",font=font_style,bg="#4DA6FF",fg="White",relief="groove")
l5.place(anchor=CENTER,x=52,y=215)
r1=Radiobutton(frame,text="Male",font="arial 10 bold",activebackground="#4DA6FF",variable=var1,value="Male",bg="#4DA6FF")
r1.place(anchor=CENTER,x=205,y=215)
r2=Radiobutton(frame,text="Female",font="arial 10 bold",activebackground="#4DA6FF",variable=var1,value="Female",bg="#4DA6FF")
r2.place(anchor=CENTER,x=320,y=215)

# Creating Adhaar Number Label
l6 = Label(frame, text=" Adhaar Number ", font=font_style, bg="#4DA6FF", fg="white",relief="groove")
l6.grid(row=5, column=0, pady=10, padx=10, sticky=W)
# Creating AdhaarNumber textbox
e6 = Entry(frame, width=26, font="calibri")
e6.grid(row=5, column=1, pady=10, padx=10, sticky=W)

# Creating Mobile No Label
l7 = Label(frame, text=" Mobile Number ", font=font_style, bg="#4DA6FF", fg="white",relief="groove")
l7.grid(row=6, column=0, pady=10, padx=10, sticky=W)
# Creating Textbox of Mobile No Label
e7 = Entry(frame, width=26, font="calibri")
e7.grid(row=6, column=1, pady=10, padx=10, sticky=W)


# Creating Email Label
l8 = Label(frame, text=" E-mail ID ", font=font_style, bg="#4DA6FF", fg="white",relief="groove")
l8.grid(row=7, column=0, pady=10, padx=10, sticky=W)
# Creating Textbox of Email Label
e8 = Entry(frame, width=26, font="calibri")
e8.grid(row=7, column=1, pady=10, padx=10, sticky=W)


# Creating Address Label
l9 = Label(frame, text=" Address ", font=font_style, bg="#4DA6FF", fg="white",relief="groove")
l9.grid(row=8, column=0, pady=10, padx=10, sticky=W)

# Creating Textbox of Address Label
e9 = Text(frame, width=26, height=3, font="calibri", wrap=WORD)
e9.grid(row=8, column=1, pady=10, padx=10, sticky=W)


# Creating a button to Update
b1 = Button(root, text="Update", relief="groove", font=font_style, height=1, width=10, bg="#4CAF50", fg="white")  # Updated colors and width
b1.place(anchor=CENTER, x=340, y=640)
b1.config(command=stud_update)

# Creating a button to Delete
b2 = Button(root, text="Delete", relief="groove", font=font_style, height=1, width=10, bg="#FF4C4C", fg="white")  # Updated colors and width
b2.place(anchor=CENTER, x=200, y=680)
b2.config(command=stud_delete)

# Creating a button to back
b3 = Button(root, text="Logout", relief="groove", font=font_style, width=10, height=1, bg="#FFD700", fg="black")  # Updated colors and width
b3.place(anchor=CENTER, x=340, y=680)
b3.config(command=logO)

# Creating a button to Feedback
b4 = Button(root, text="Feedback", relief="groove", font=font_style, width=10, height=1, bg="#1E90FF", fg="white")  # Updated colors and width
b4.place(anchor=CENTER, x=480, y=680)
b4.config(command=feedback)

update_info()

root.mainloop()
