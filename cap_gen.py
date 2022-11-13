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
ent.grid(row=6,column=10)
ent_cap=Entry(root)
ent_cap.grid(row=6,column=11)
root.mainloop()