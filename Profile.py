from tkinter import *
# from tkinter.ttk import *
#import tkinter.messagebox as mb
from PIL import ImageTk
import mysql.connector

class Profile:

    def __init__(self, root):
        self.root = root
        self.root.title("Login System (OSHES)")
        self.root.geometry("1280x700+200+70")
        self.root.resizable(False, False)
       # self.root.config(bg="white")

        #Adding image#

        self.image=ImageTk.PhotoImage(file="/Login/bg1.jpg")
        self.label=Label(self.root, image=self.image)
        self.label.pack()

        self.left=ImageTk.PhotoImage(file="/Login/pro01.jpg")
        left=Label(self.root, image=self.left)
        left.place(x=80, y=100, width=400, height=500)

        #text variables
        self.id_var = StringVar()
        self.name_var = StringVar()
        self.num_var = StringVar()
        self.email_var = StringVar()
        self.address_var = StringVar()

        f = open("store_custID.txt", "r")
        profile_details = []
        for line in f:
            profile_details.append(line.rstrip())

        print(profile_details[0])

        self.id_var.set(profile_details[0])
        self.name_var.set(profile_details[1])
        self.num_var.set(profile_details[4])
        self.email_var.set(profile_details[3])
        self.address_var.set(profile_details[5])

        #Frame
        frame1=Frame(self.root, bg="white")
        frame1.place(x=480, y=100, width=700, height=500)

        #Name, Gender, Email, Number, Address, Password and Re-enter Password
        title = Label(frame1, text = "My Account Page", font=("calibri",20,"bold", "underline"),bg="white", fg="green")
        title.place(x=50, y=10)

        #ID
        id = Label(frame1, text = "Username", font=("calibri",15,"bold"),bg="white", fg="gray")
        id.place(x=50, y=70)
        
        txt_id = Entry(frame1, font=("calibri",15), bg="lightgray", state="readonly", textvariable=self.id_var)
        txt_id.place(x=50, y=110)

        # Name
        name = Label(frame1, text="Name", font=("calibri", 15, "bold"), bg="white", fg="gray")
        name.place(x=50, y=160)

        txt_name = Entry(frame1, font=("calibri", 15), bg="lightgray", state="readonly", textvariable=self.name_var)
        txt_name.place(x=50, y=200)

        #Number
        number = Label(frame1, text = "Number", font=("calibri",15,"bold"),bg="white", fg="gray")
        number.place(x=330,y=70)
        
        txt_num = Entry(frame1, font=("calibri",15), bg="lightgray", state="readonly", textvariable=self.num_var)
        txt_num.place(x=330, y=110)

        #Email
        email = Label(frame1, text = "Email", font=("calibri",15,"bold"),bg="white", fg="gray")
        email.place(x=330, y=160)
        
        txt_email = Entry(frame1, font=("calibri",15), bg="lightgray", state="readonly", textvariable=self.email_var)
        txt_email.place(x=330, y=200, width=250)

        #Address
        address = Label(frame1, text = "Address", font=("calibri",15,"bold"),bg="white", fg="gray")
        address.place(x=50,y=250)
        
        txt_address = Entry(frame1, font=("calibri",15), bg="lightgray", state="readonly", textvariable=self.address_var)
        txt_address.place(x=50, y=290, width=350)

        #Register Button
   #     check=Button(frame1, text="Purchase History", font=("Cambria", 15, "bold"), fg="white", bg="light blue")
     #   check.place(x=50, y=360)

    #    check1=Button(frame1, text="Request and Service History", font=("Cambria", 15, "bold"), fg="white", bg="light blue")
    #    check1.place(x=250, y=360)

        check2 = Button(frame1, text="Back", font=("Cambria", 15, "bold"), fg="white", bg="light blue", command=self.destroyProfile)
        check2.place(x=50, y=440)

    def fetch_data(self):
        con = mysql.connector.connect(host="localhost", user="root", password="s63127734", database="oshes")
        cur = con.cursor()
        cur.execute("select * from Customer where customerID = %s", self.id_var.get())
        rows = cur.fetchone()
        self.name_var.set(rows[1])
        self.num_var.set(rows[4])
        self.email_var.set(rows[3])
        self.address_var.set(rows[5])
        if rows is None:
            print("empty")
        else:
            print(rows)

    def destroyProfile(self):
        self.root.destroy()
        import NewProduct




if __name__ =="__main__":
    root=Tk()
    main = Profile(root)
    root.mainloop()
