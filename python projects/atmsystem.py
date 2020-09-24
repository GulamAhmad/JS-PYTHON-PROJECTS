# importing library
from tkinter import *
from tkinter import ttk
import mysql.connector as mysql
from tkinter import messagebox
import random
import string
import secrets
import smtplib
import os


def forgot():
    global pin_acc

    top = Toplevel()
    email = Label(top, text="ENTER MAIL")
    email.grid(row=0, column=0)
    email_e = Entry(top,)
    email_e.grid(row=0, column=1)

    u_name = Label(top, text="ENTER ACCNAME")
    u_name.grid(row=1, column=0)
    u_e = Entry(top)
    u_e.grid(row=1, column=1)

    def get():
        for i in pin_acc:
            if i[1] == u_e.get():
                sendmail(email_e.get(), i[0])

    btn = Button(top, text="SEND", command=get)
    btn.grid(row=2, columnspan=2, column=1)


# smtp server setup....
EMAIL_ADD = #your email
EMAIL_PASS = #password


def sendmail(to, content):
    with smtplib.SMTP('smtp.gmail.com', 587) as ser:
        ser.ehlo()
        ser.starttls()
        ser.ehlo()
        ser.login(EMAIL_ADD, EMAIL_PASS)
        ser.sendmail(EMAIL_ADD, to, content)
        ser.close()


# main window.....
root = Tk()
root.geometry("1350x700+0+0")
main_label = Label(root, text="ATM", bg="red",
                   fg="white", font=("", 60, "bold"))
main_label.pack(side=TOP, fill=X)
root.title("ATM")

# defing globals
global n_ent
global p_ent
global master2
global pin_acc
global fe
global d
global dep_l
global wit_l

# fetching data......


def data():
    global fe
    myConnection = mysql.connect(
        host='localhost', user='root', passwd='root123', db='atm_system')
    cur = myConnection.cursor()
    cur.execute("SELECT * FROM details")
    fe = cur.fetchall()
    myConnection.commit()
    myConnection.close()


data()

# fetching data for validation........


def validate():
    global pin_acc
    myConnection = mysql.connect(
        host='localhost', user='root', passwd='root123', db='atm_system')
    cur = myConnection.cursor()
    cur.execute("SELECT pincode,accname FROM details")
    pin_acc = cur.fetchall()
    myConnection.commit()
    myConnection.close()


validate()

# login window.........


def login():
    master5 = Tk()
    master5.geometry("1350x720+0+0")
    master5.title("Login")

    global n_ent
    global p_ent
    fr_0 = Frame(master5, bg="blue")
    fr_0.place(x=450, y=200, width=500, height=275)

    fr_1 = Frame(fr_0, bg="silver")
    fr_1.place(width=500, height=25)

    fr_2 = Frame(fr_0, bg="blue")
    fr_2.place(y=25, width=500, height=150)

    fr_3 = Frame(fr_0, bg="blue")
    fr_3.place(y=175, width=500, height=100)

    li = Label(fr_1, text="Log in", fg="black", bg="silver", font=("", 15))
    li.pack(side=LEFT, expand=YES)

    name_l = Label(fr_2, text="Name", fg="white", bg="blue", font=("", 19))
    name_l.grid(row=0, column=0, padx=35, pady=35)

    n_ent = Entry(fr_2, font=("", 18), bd=2, relief=FLAT)
    n_ent.grid(row=0, column=1)

    pin_l = Label(fr_2, text="Pin", fg="white", bg="blue", font=("", 19))
    pin_l.grid(row=1, column=0, padx=35)

    p_ent = Entry(fr_2, font=("", 18), bd=2, relief=FLAT)
    p_ent.grid(row=1, column=1)

    but_l = Button(fr_3, text="Enter", width=15, height=1, command=check)
    but_l.pack(side=LEFT, expand='yes')

    but_3 = Button(fr_3, text="Forgot Password",
                   width=15, height=1, command=forgot)
    but_3.pack(side=LEFT, expand='yes')

    but_2 = Button(fr_1, text="X", width=2, relief=FLAT, height=1,
                   bg="red", fg="white", command=master5.destroy)
    but_2.pack(anchor="e")

# checking password.....


def check():
    global pin_acc
    global n_ent
    global p_ent
    global d

    d = (p_ent.get(), n_ent.get())
    for i in pin_acc:
        if d == i:
            command()
            break
    else:
        messagebox.showerror("Error", "Invalid name")

# getting details of logged in user.....


def details():
    global pin_acc
    global d
    global fe

    myConnection = mysql.connect(
        host='localhost', user='root', passwd='root123', db='atm_system')
    cur = myConnection.cursor()
    cur.execute(f"SELECT * FROM details where pincode={d[0]}")
    show = cur.fetchall()
    myConnection.commit()
    myConnection.close()

    tp = Toplevel()
    tp.geometry("300x150+570+150")
    label1 = Label(tp, text="Name: ", font=("", 24, ""))
    label1.grid(row=0, column=0)

    label2 = Label(tp, text="", font=("", 24, ""))
    label2.grid(row=0, column=1)

    label3 = Label(tp, text="Acc no: ", font=("", 24, ""))
    label3.grid(row=1, column=0)

    label4 = Label(tp, text="", font=("", 24, ""))
    label4.grid(row=1, column=1)

    label5 = Label(tp, text="Balance: ", font=("", 24, ""))
    label5.grid(row=2, column=0)

    label6 = Label(tp, text="", font=("", 24, ""))
    label6.grid(row=2, column=1)

    for j in pin_acc:
        if d == j:
            for i in show:
                label2.config(text=i[1])
                label4.config(text=i[2])
                label6.config(text=i[3])

# working window........


def command():
    global master2
    global dep_l
    global wit_l

    master2 = Tk()
    master2.geometry("1350x700+0+0")
    master2.title("New Window")
    master2.config(bg="white")

    fr_d = Frame(master2, bd=3, relief=FLAT, bg="blue")
    fr_d.place(x=400, y=100, width=600, height=500)

    det_l1 = Button(fr_d, text="Details", width=20, height=2,
                    bg="silver", fg="black", command=details)
    det_l1.place(x=225, y=100)

    fr_bt = Frame(fr_d, bg="blue")
    fr_bt.place(x=50, y=250, width=500, height=200)

    dep_l = Button(fr_bt, text="Deposite", width=20, height=2,
                   bg="red", fg="white", command=deposite)
    dep_l.pack(side=TOP, expand=YES)

    wit_l = Button(fr_bt, text="Withdraw", width=20, height=2,
                   bg="green", fg="white", command=withdraw)
    wit_l.pack(side=TOP, expand=YES)

    can_l = Button(fr_bt, text="Cancel", width=20, height=2,
                   bg="yellow", fg="blue", command=master2.destroy)
    can_l.pack(side=TOP, expand=YES)
    master2.mainloop()

# deposite window.....


def deposite():
    global dep_l
    global d

    def _quit():
        master3.destroy()
        dep_l.config(state=ACTIVE)

    dep_l.config(state=DISABLED)

    master3 = Toplevel()
    master3.title("Deposite")
    master3.geometry("500x500+400+100")
    amount = Label(master3, text="Enter Amount", font=("", "20", ""))
    amount.grid(pady=60, row=0, column=0)
    ent = Entry(master3, font=("", "20", ""))
    ent.grid(pady=60, row=0, column=1)

    def dep():
        msg = messagebox.askquestion(
            "update", "Are you sure you want to deposit the amount?")
        if msg == 'yes':
            myConnection = mysql.connect(
                host='localhost', user='root', passwd='root123', db='atm_system')
            cur = myConnection.cursor()
            cur.execute("update details set balance = balance + " +
                        ent.get()+" where accname = '"+d[1]+"'")
            myConnection.commit()
            myConnection.close()
            dep_l.config(state=ACTIVE)

    bt = Frame(master3)
    bt.place(x=10, y=250, width=400, height=100)
    con_l = Button(bt, text="Confirm", width=20, height=2,
                   bg="blue", fg="white", command=dep)
    con_l.pack(side=TOP, expand=YES)
    can_l = Button(bt, text="Cancel", width=20, height=2,
                   bg="blue", fg="white", command=_quit)
    can_l.pack(side=TOP, expand=YES)


# withdraw window.............
def withdraw():
    global d
    global wit_l

    def q():
        master4.destroy()
        wit_l.config(state=ACTIVE)

    wit_l.config(state=DISABLED)

    master4 = Tk()
    master4.title("Withdraw")
    master4.geometry("500x500+400+100")
    amount = Label(master4, text="Enter Amount", font=("", "20", ""))
    amount.grid(pady=60, row=0, column=0)
    ent = Entry(master4, font=("", "20", ""))
    ent.grid(pady=60, row=0, column=1)

    def wit():
        msg = messagebox.askquestion(
            "update", "Are you sure you want to withdraw the amount?")
        if msg == 'yes':
            myConnection = mysql.connect(
                host='localhost', user='root', passwd='root123', db='atm_system')
            cur = myConnection.cursor()
            cur.execute("update details set balance = balance - " +
                        ent.get()+" where accname = '"+d[1]+"'")
            myConnection.commit()
            myConnection.close()
            wit_l.config(state=ACTIVE)

    bt = Frame(master4)
    bt.place(x=10, y=250, width=400, height=100)
    con_l = Button(bt, text="Confirm", width=20, height=2,
                   bg="blue", fg="white", command=wit)
    con_l.pack(side=TOP, expand=YES)
    can_l = Button(bt, text="Cancel", width=20, height=2,
                   bg="blue", fg="white", command=q)
    can_l.pack(side=TOP, expand=YES)

# new user sign up window.......


def signup():
    master6 = Tk()
    master6.geometry("1350x720+0+0")
    master6.title("Sign up")

    fr_0 = Frame(master6, bg="blue")
    fr_0.place(x=450, y=70, width=400, height=550)

    fr_1 = Frame(fr_0, bg="silver")
    fr_1.place(width=400, height=25)

    fr_2 = Frame(fr_0, bg="blue")
    fr_2.place(y=25, width=400, height=400)

    fr_3 = Frame(fr_0, bg="blue")
    fr_3.place(y=425, width=400, height=125)

    su = Label(fr_1, text="Sign up", fg="black", bg="silver", font=("", 15))
    su.pack(side=LEFT, expand=YES)

    fn = Label(fr_2, text="First name:", fg="white", bg="blue", font=("", 16))
    fn.grid(row=2, column=1, padx=15, pady=25)

    f_ent = Entry(fr_2, font=("", 15), bd=2, relief=FLAT)
    f_ent.grid(row=2, column=2)

    def msg():
        if f_ent.get == "" or l_ent.get() == "" or p_ent.get() == "" or a_ent.get() == "" or i_ent.get() == "" or ad_ent.get() == "" or pan_ent.get() == "":
            messagebox.showerror(
                "error", "Please fill all the required details")
        else:
            msg = messagebox.askquestion("Submit", "Are you sure?")
            if msg == "yes":
                password = ''.join(secrets.choice(string.digits)
                                   for i in range(4))
                messagebox.showinfo(
                    "data", f"username {f_ent.get()} password {password}")
                messagebox.showinfo(
                    "Congratulation", "Your account has been created succesfully")

                # mysql connection..........

                myConnection = mysql.connect(
                    host='localhost', user='root', passwd='root123', db='atm_system')
                cur = myConnection.cursor()
                cur.execute(
                    f"insert into details values({password},'{f_ent.get()}',{a_ent.get()},0)")
                cur.execute(
                    f"insert into newuser values('{f_ent.get()}','{l_ent.get()}',{p_ent.get()},{a_ent.get()},'{i_ent.get()}',{ad_ent.get()},{pan_ent.get()})")
                myConnection.commit()
                myConnection.close()
                root.destroy()
                master6.destroy()

    ln = Label(fr_2, text="Last name:", fg="white", bg="blue", font=("", 16))
    ln.grid(row=3, column=1)

    l_ent = Entry(fr_2, font=("", 15), bd=2, relief=FLAT)
    l_ent.grid(row=3, column=2)

    phn = Label(fr_2, text="Phone no:", fg="white", bg="blue", font=("", 16))
    phn.grid(row=4, column=1, pady=25)

    p_ent = Entry(fr_2, font=("", 15), bd=2, relief=FLAT)
    p_ent.grid(row=4, column=2)

    accn = Label(fr_2, text="Acc no:", fg="white", bg="blue", font=("", 16))
    accn.grid(row=5, column=1)

    a_ent = Entry(fr_2, font=("", 15), bd=2, relief=FLAT)
    a_ent.grid(row=5, column=2)

    ifsc = Label(fr_2, text="IFSC no:", fg="white", bg="blue", font=("", 16))
    ifsc.grid(row=6, column=1, pady=25)

    i_ent = Entry(fr_2, font=("", 15), bd=2, relief=FLAT)
    i_ent.grid(row=6, column=2)

    adn = Label(fr_2, text="Adhaar no:", fg="white", bg="blue", font=("", 16))
    adn.grid(row=7, column=1)

    ad_ent = Entry(fr_2, font=("", 15), bd=2, relief=FLAT)
    ad_ent.grid(row=7, column=2)

    pan = Label(fr_2, text="Pan no:", fg="white", bg="blue", font=("", 16))
    pan.grid(row=8, column=1, pady=25)

    pan_ent = Entry(fr_2, font=("", 15), bd=2, relief=FLAT)
    pan_ent.grid(row=8, column=2)

    but_l = Button(fr_3, text="Submit", width=13, height=1, command=msg)
    but_l.pack(pady=30)

    but_2 = Button(fr_1, text="X", width=2, relief=FLAT, height=1,
                   bg="red", fg="white", command=master6.destroy)
    but_2.pack(anchor="e")


# startwindow....
fr = Frame(root, bd=10, highlightbackground="silver",
           highlightcolor="silver", highlightthickness=10, bg="blue")
fr.place(x=450, y=200, width=500, height=300)
fr.config()

wlc = Label(fr, text="Welcome to the ATM system",
            fg="white", bg="blue", font=("", 20))
wlc.grid(row=1, column=1, padx=60, pady=20)

choose = Label(fr, text="What would you like to do?",
               fg="white", bg="blue", font=("", 20))
choose.grid(row=2, column=1, pady=20)

but_l = Button(fr, text="Sign up", command=signup, width=15, height=1)
but_l.grid(row=3, column=1)

op = Label(fr, text="or", fg="white", bg="blue", font=("", 15))
op.grid(row=4, column=1)

but_2 = Button(fr, text="Log in", command=login, width=15, height=1)
but_2.grid(row=5, column=1)
