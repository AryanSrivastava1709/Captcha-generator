from tkinter import*
top=Tk()
top.geometry('450x220')
top.title("Login")
Reg=Label(top,text='Registration Number: ',font='Times 13')
Reg.grid(row=1,column=10,sticky=E)
Reg_ent=Entry(top)
Reg_ent.grid(row=1,column=11)
top.mainloop()