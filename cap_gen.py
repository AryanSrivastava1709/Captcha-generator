from tkinter import*
# defining the geometry of parent window
root=Tk()
root.geometry('450x220')
root.title("Login")
# designing the registration box
Reg_no=Label(root,text='Registration Number: ',font='calibri 15 bold')
Reg_no.grid(row=1,column=10,sticky=E)
Regno_ent=Entry(root)
Regno_ent.grid(row=1,column=11)
# adding field for captcha writing.
ent=Label(root,text='Enter the Captcha: ',font='calibri 15 bold')
ent.grid(row=4,column=10)
ent_cap=Entry(root)
ent_cap.grid(row=4,column=11)
# adding buttons and images
sub_btn=Button(root,text='Login',relief=RIDGE,height=2,width=10,bg='white',fg='black',activebackground='lightblue',activeforeground='red',font='Times 10 bold')
#to set the co ordinates
sub_btn.place(x=180, y=160)
img=PhotoImage(file="Refresh.png")
refresh=Button(root,text="Refresh",relief=RIDGE,height=30,width=40,bg='white',image=img,activebackground='lightblue')
refresh.grid(row=3,column=11)
# adding canvas for captcha 
c=Canvas(root,height=80,width=240)
c.create_text(160,40,text="6dasd",font='calibri 28 bold')
c.grid(row=3,column=10)
root.mainloop()