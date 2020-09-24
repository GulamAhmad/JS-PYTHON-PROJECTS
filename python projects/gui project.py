 #libraries....
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector as mysql
import re 
import smtplib
import os


EMAIL_ADD = os.environ.get('EMAIL_USER')
EMAIL_PASS = os.environ.get('EMAIL_PASS')
def sendmail(to):
    with smtplib.SMTP('smtp.gmail.com',587) as ser:
            ser.starttls()
            ser.login(EMAIL_ADD,EMAIL_PASS)
            ser.sendmail(EMAIL_ADD,to,"your data submited succesfully")
            ser.close()


#msql connection & functions.........
#inserting values in databases...
def get():
    regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    if n_ent.get() == '':
        messagebox.showerror("error","please enter name")
        
    elif (re.search(regex,e_ent.get()) == None) and e_ent.get()==None:
        messagebox.showerror("error","please enter valid email")
        e_ent.delete(0,'end')
        
    elif c_ent.get() == '':
        messagebox.showerror("error","please enter contact number")

    elif t_ent.get()=='':
        messagebox.showerror("error","please enter address")

    elif com_b.get() =='':
        messagebox.showerror("error","please enter gender")

    else:
        messagebox.showinfo("succesfull","your data has been sumited ")
        myConnection = mysql.connect( host='localhost', user='root', passwd='root123', db='students' )
        cur = myConnection.cursor()
        cur.execute("insert into info values('"+n_ent.get()+"','"+e_ent.get()+"',"+c_ent.get()+",'"+com_b.get()+"','"+t_ent.get()+"',null)")
        myConnection.commit()
        cur.execute("select * from info")
        myConnection.close()
        tree.insert('','end',text=n_ent.get(),values=(e_ent.get(),c_ent.get(),gen.get(),t_ent.get()))
        sendmail(e_ent.get())

#deleting values from database and treeview.....
def del_():
    msgbox = messagebox.askquestion("Delete","selected item will be deleted from database also",icon='warning')
    if msgbox == 'yes':
        myConnection = mysql.connect( host='localhost', user='root', passwd='root123', db='students' )
        cur = myConnection.cursor()
        select = tree.selection()
        for i in select:
            dic = tree.item(select[0])
        dic_arr = dic['text']
        name = dic_arr
        cur.execute("delete from info where name='"+name+"'")
        myConnection.commit()
        cur.execute("select * from info")
        myConnection.close()
        select = tree.selection()
        for i in select:
            tree.delete(i)
    else:
        messagebox.showinfo("return","you cancelled this operation")
#retrieving full data from database...... 
def see():
    myConnection = mysql.connect( host='localhost', user='root', passwd='root123', db='students' )
    cur = myConnection.cursor()
    cur.execute("SELECT * FROM info where name='"+seL.get()+"'")
    fetch = cur.fetchall()
    for data in fetch: 
        tree.insert('', 'end',text=data[0] ,values=(data[1], data[2], data[3], data[4]))
    myConnection.commit()
    myConnection.close()

def data():
    myConnection = mysql.connect( host='localhost', user='root', passwd='root123', db='students' )
    cur = myConnection.cursor()
    cur.execute("SELECT * FROM info")
    fetch = cur.fetchall()
    for data in fetch:
        tree.insert('', 'end',text=data[0] ,values=(data[1], data[2], data[3], data[4]))
    myConnection.commit()
    myConnection.close()
    but_2.config(state=DISABLED)
    
def clear():
    for i in tree.get_children():
        tree.delete(i)   
    seL.delete(0, 'end')
    but_2.config(state=ACTIVE)

def clr():
    n_ent.delete(0, 'end')
    e_ent.delete(0, 'end')
    c_ent.delete(0, 'end')
    t_ent.delete(0, 'end')
    com_b.set('')
    

 #geomtry of gui
root = Tk()
root.geometry("1350x700+0+0")
main_label=Label(root,text="Student Detail",bg="red",fg="white",font=("",40,"bold"))
main_label.pack(side=TOP,fill=X)

#setting frame
fr=Frame(root,bd=3,relief=RIDGE,bg="dodgerblue")
fr.place(x=10,y=70,width=500,height=600)

fr_de=Frame(root,bd=3,relief=RIDGE,bg="dodgerblue")
fr_de.place(x=550,y=70,width=750,height=600)

fr_tb=Frame(root)
fr_tb.place(x=575,y=200,width=700,height=450)

fr_bt=Frame(root,bd=3,relief=RIDGE,bg="dodgerblue")
fr_bt.place(x=30,y=550,width=450,height=70)


def update():
    update = Tk()
    update.geometry("450x250+20+100")
    update.config(bg="dodgerblue")
    update.title("update")
    up_label = Label(update,text="Update: ",bg="dodgerblue",font=("",20,"bold"))
    up_label.grid(row=0,column=0)
    ch_label = Label(update,text="Change: ",bg="dodgerblue",font=("",20,"bold"))
    ch_label.grid(row=1,column=0)
    up_ent = Entry(update,font=("",20,"bold"))
    up_ent.grid(row=1,column=1)
    info = StringVar()
    com_info=ttk.Combobox(update,font=("",19,"bold"),state="readonly",textvariable=info)
    com_info['value']=("name","email","phone","gender","addres")
    com_info.grid(row=0,column=1,padx=20,pady=10,sticky="w")
    def updatedb():
        msgbox = messagebox.askquestion("warning","do you want to update changes",icon='warning')
        if msgbox == 'yes':
            myConnection = mysql.connect( host='localhost', user='root', passwd='root123', db='students' )
            cur = myConnection.cursor()
            select = tree.selection()
            for i in select:
                dic = tree.item(select[0])
            dic_arr = dic['text']
            name = dic_arr
            cur.execute("update info set "+com_info.get()+"='"+up_ent.get()+"' where name='"+name+"'")
            myConnection.commit()
            myConnection.close()
            messagebox.showinfo("successful","data has been updated successfully")
        else:
            messagebox.showinfo("Declined","data not submited")
        update.destroy()
        
    bt_fr =Frame(update,bg="dodgerblue")
    bt_fr.place(x=40,y=100,width=400,height=100)
    up_bt = Button(bt_fr,text="Update",width=10,height=2,bg="yellow",command=updatedb)
    up_bt.pack(side=LEFT,expand=YES)
    cl_bt = Button(bt_fr,text="Cancel",width=10,height=2,bg="yellow",command=update.destroy)
    cl_bt.pack(side=LEFT,expand=YES)


#treeview table
tree  = ttk.Treeview(fr_tb,selectmode="browse")
sbr = Scrollbar(fr_tb)
sbr.pack(side=RIGHT,fill="y")
sbr.config(command=tree.yview)
tree.config(yscrollcommand=sbr.set)

tree.config(height=22)

tree["column"] = ("1","2","3","4")
tree.column("#0", width=150, stretch=NO)
tree.column("1", width=150, stretch=NO)
tree.column("2", width=150,stretch=NO)
tree.column("3", width=150,stretch=NO)
tree.column("4", width=150,stretch=NO)

tree.heading("#0",text="Name",anchor=W)
tree.heading("1",text="email",anchor=W)
tree.heading("2",text="phone",anchor=W)
tree.heading("3",text="gender",anchor=W)
tree.heading("4",text="address",anchor=W)

tree.pack(side=TOP,fill=X)


def callback(event):
    print(tree.selection())

tree.bind('<<TreeviewSelect>>',callback)
#labels and entry

title_l = Label(fr,text="Student",bg="dodgerblue",fg="white",font=("",40,"bold"))
title_l.grid(row=0,columnspan=2,pady=20)

name_l = Label(fr,text="Name",bg="dodgerblue",fg="white",font=("",20,"bold"))
name_l.grid(row=1,column=0,padx=20,pady=10,sticky="w")

n_ent = Entry(fr,font=("",20,"bold"),bd=3,relief=RIDGE)
n_ent.grid(row=1,column=1,padx=20,sticky="w")

email_l = Label(fr,text="Email",bg="dodgerblue",fg="white",font=("",20,"bold"))
email_l.grid(row=2,column=0,padx=20,pady=10,sticky="w")

e_ent = Entry(fr,font=("",20,"bold"),bd=3,relief=RIDGE)
e_ent.grid(row=2,column=1,padx=20,sticky="w")

cont_l = Label(fr,text="Phone",bg="dodgerblue",fg="white",font=("",20,"bold"))
cont_l.grid(row=3,column=0,padx=20,pady=10,sticky="w")

c_ent = Entry(fr,font=("",20,"bold"),bd=3,relief=RIDGE)
c_ent.grid(row=3,column=1,padx=20,sticky="w")

com_l = Label(fr,text="Gender",bg="dodgerblue",fg="white",font=("",20,"bold"))
com_l.grid(row=4,column=0,padx=20,pady=10,sticky="w")

gen = StringVar()
com_b=ttk.Combobox(fr,font=("",19,"bold"),state="readonly",textvariable=gen)
com_b['value']=("Male","Female","Other")
com_b.grid(row=4,column=1,padx=20,pady=10,sticky="w")

add_l = Label(fr,text="City",bg="dodgerblue",fg="white",font=("",20,"bold"))
add_l.grid(row=5,column=0,padx=20,pady=10,sticky="w")

t_ent = Entry(fr,font=("",20,"bold"),bd=3,relief=RIDGE)
t_ent.grid(row=5,column=1,padx=20,pady=10,sticky="w")

sub_l = Button(fr_bt,text="submit",width=15,height=2,command=get)
sub_l.pack(side=LEFT,expand=YES)

upd_l = Button(fr_bt,text="update",width=15,height=2,command=update)
upd_l.pack(side=LEFT,expand=YES)

del_l = Button(fr_bt,text="delete",width=15,height=2,command=del_)
del_l.pack(side=LEFT,expand=YES)

but_4 = Button(fr_bt,text="CLEAR",width=10,height=2,command=clr)
but_4.pack(side=LEFT,expand=YES)



#frame setting and data

title_l = Label(fr_de,text="Search",bg="dodgerblue",fg="white",font=("",20,"bold"))
title_l.grid(row=0,column=0,pady=20,padx=20)

sphoto = PhotoImage(file="search.png")
ssize = sphoto.subsample(45,45)

ephoto = PhotoImage(file="eye.png")
esize = ephoto.subsample(17,17)

seL= Entry(fr_de,font=("",15,"bold"),bd=3,relief=RIDGE)
seL.grid(row=0,column=1,padx=20)

but_l = Button(fr_de,text="SEARCH",command=see,image=ssize,compound = RIGHT)
but_l.grid(row=0,column=2,padx=10)

but_2 = Button(fr_de,text="SEE ALL",command=data,image=esize,compound = RIGHT)
but_2.grid(row=0,column=3,padx=10)

but_3 = Button(fr_de,text="CLEAR",width=10,height=2,command=clear)
but_3.grid(row=0,column=4,padx=10)

root.mainloop()
