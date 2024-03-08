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
                        rootk=Tk()
                        rootk.title("Desktop Notifier")
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
                        er2.place(anchor=CENTER,x=300,y=140)

                        login_button=Button(rootk,text="Login",bg="white",fg="LightBlue",font="arial 12 bold",height=20,width=50,relief=GROOVE)
                        login_button.pack(anchor=CENTER)
                        login_button.config(command=chck_cred)
                        
                        rootk.mainloop()
                else:
                    register_DB()
            else:
                e3.config(fg="red")
                blabel.config(text="Password does not match !")