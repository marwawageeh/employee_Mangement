from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from db import Database

db=Database("Employee.db")

root = Tk()
root.title('Employ management system')
root.geometry('1240x680+0+0')
root.resizable(False,False)
root.configure(bg='gray')


name=StringVar()
age=StringVar()
job=StringVar()
gender=StringVar()
email=StringVar()
mobile=StringVar()

logo=PhotoImage(file='logo.png')
lbl_logo= Label(root,image=logo,bg='gray')
lbl_logo.place(x=10,y=490)

#==============Entries frame=================
entries_frame= Frame(root, bg='gray')
entries_frame.place(x=1,y=1,width=360,height=510)
title=Label(entries_frame,text='Employ company',font=('Calibri',18,'bold'),bg='gray',fg='white')
title.place(x=10,y=1)

lblname=Label(entries_frame,text='    Name',font=('Calibri',16),bg='gray',fg='white')
lblname.place(x=10,y=50)
txtname=Entry(entries_frame,textvariable=name,width=20,font=('Calibri',16))
txtname.place(x=120,y=50)

lbljob=Label(entries_frame,text='    Job',font=('Calibri',16),bg='gray',fg='white')
lbljob.place(x=10,y=90)
txtjob=Entry(entries_frame,textvariable=job,width=20,font=('Calibri',16))
txtjob.place(x=120,y=90)

lblgender=Label(entries_frame,text='    Gender',font=('Calibri',16),bg='gray',fg='white')
lblgender.place(x=10,y=130)
combogender= ttk.Combobox(entries_frame,textvariable=gender,state='readonly',width=18,font=('Calibri',16))
combogender['values']=('Male','Female')
combogender.place(x=120,y=130)

lblage=Label(entries_frame,text='    Age',font=('Calibri',16),bg='gray',fg='white')
lblage.place(x=10,y=170)
txtage=Entry(entries_frame,textvariable=age,width=20,font=('Calibri',16))
txtage.place(x=120,y=170)

lblemail=Label(entries_frame,text='    Email',font=('Calibri',16),bg='gray',fg='white')
lblemail.place(x=10,y=210)
txtemail=Entry(entries_frame,textvariable=email,width=20,font=('Calibri',16))
txtemail.place(x=120,y=210)

lblcontact=Label(entries_frame,text='    Mobile',font=('Calibri',16),bg='gray',fg='white')
lblcontact.place(x=10,y=250)
txtcontact=Entry(entries_frame,textvariable=mobile,width=20,font=('Calibri',16))
txtcontact.place(x=120,y=250)

lbladdress=Label(entries_frame,text='    Address : ',font=('Calibri',16),bg='gray',fg='white')
lbladdress.place(x=10,y=290)
txtaddress=Text(entries_frame,width=30,height=2,font=('Calibri',16))
txtaddress.place(x=10,y=330)

#==============Define========================
def hide():
    root.geometry('360x515+0+0')
def show():
    root.geometry('1240x680+0+0')
   
btnhide=Button(entries_frame,text='Hide',bg='white',bd=1,relief=SOLID,cursor='hand2',command=hide)
btnhide.place(x=270,y=10)

btnshow=Button(entries_frame,text='Show',bg='white',bd=1,relief=SOLID,cursor='hand2',command=show)
btnshow.place(x=310,y=10)

#دى عشان لما ندوس على النص يجبهولى فى الناحيه الشمال
def getData(event):
    selected_row=tv.focus()
    data=tv.item(selected_row)
    global row 
    row=data['values']
    name.set(row[1])
    age.set(row[2])
    job.set(row[3])
    email.set(row[4])
    gender.set(row[5])
    mobile.set(row[6])
    txtaddress.delete(1.0,END)
    txtaddress.insert(END,row[7])

def displayAll():
    tv.delete(*tv.get_children())
    for row in db.fetch():
        tv.insert("",END,values=row)

def update():
    pass

def delete():
    db.remove(row[0])
    clear()
    displayAll()


def clear():
    name.set("")
    age.set("")
    job.set("")
    gender.set("")
    email.set("")
    mobile.set("")
    txtaddress.delete(1.0,END)
        


def add_employee():
    if txtname.get()==""  or txtage.get()=="" or txtjob.get()=="" or txtemail.get()=="" or combogender.get()=="" or txtemail.get()=="" or txtaddress.get(1.0,END)=="":
        messagebox.showerror("Error","please fill")
        return
    db.insert(
        txtname.get(),
        txtage.get(),
        txtjob.get(),
        txtemail.get(),
         combogender.get(),
        txtcontact.get(),
        txtaddress.get(1.0,END))
    messagebox.showinfo("success","added new employee")
    clear()
    displayAll()

def update():
    if txtname.get()==""  or txtage.get()=="" or txtjob.get()=="" or txtemail.get()=="" or combogender.get()=="" or txtemail.get()=="" or txtaddress.get(1.0,END)=="":
        messagebox.showerror("Error","please fill")
        return
    db.update(row[0],
        txtname.get(),
        txtage.get(),
        txtjob.get(),
        txtemail.get(),
        combogender.get(),
        txtcontact.get(),
        txtaddress.get(1.0,END)
        )
    messagebox.showinfo('success','the employee data is update')
    clear()
    displayAll()

#==============Buttom frame=================
btn_fram=Frame(entries_frame,bg='gray',bd=0,relief=SOLID)
btn_fram.place(x=10,y=400,width=335,height=100)

btnadd= Button(btn_fram,
              text='Add Details',
              width=14,
              height=1,
              font=('Calibri',16),
              fg='white',
              bg='green',
              bd=0,
              command=add_employee

              ).place(x=4,y=5)

btnedit= Button(btn_fram,
              text='Update Details',
              width=14,
              height=1,
              font=('Calibri',16),
              fg='white',
              bg='blue',
              bd=0,
              command=update
              ).place(x=4,y=50)

btndelete= Button(btn_fram,
              text='Delete Details',
              width=14,
              height=1,
              font=('Calibri',16),
              fg='white',
              bg='red',
              bd=0,
              command=delete
              ).place(x=170,y=5)

btnclear= Button(btn_fram,
              text='Clear Details',
              width=14,
              height=1,
              font=('Calibri',16),
              fg='white',
              bg='orange',
              bd=0,
              command=clear

              ).place(x=170,y=50)

#==============Table frame=================
tree_fram=Frame(root,bg='white')
tree_fram.place(x=365,y=1,width=875,height=680)
style=ttk.Style()
style.configure('mystyle.Treeview',font=('Calibri',13),rowheight=50)
style.configure('mystyle.Treeview.heading',font=('Calibri',13))

tv=ttk.Treeview(tree_fram,columns=(1,2,3,4,5,6,7,8),style='mystyle.Treeview')
tv.heading('1',text='ID')
tv.column('1',width='40')

tv.heading('2',text='Name')
tv.column('2',width='140')

tv.heading('3',text='Age')
tv.column('3',width='50')

tv.heading('4',text='Job')
tv.column('4',width='120')

tv.heading('5',text='Email')
tv.column('5',width='150')

tv.heading('6',text='Gender')
tv.column('6',width='90')

tv.heading('7',text='Mobile')
tv.column('7',width='150')

tv.heading('8',text='Address')
tv.column('8',width='150')

#اعرض كلهم من غيرها مش هيعرضهم كلهم
tv['show']='headings'
tv.bind("<ButtonRelease-1>",getData)
tv.place(x=1,y=1,height=680,width=875)

displayAll()


root.mainloop()

