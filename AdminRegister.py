from tkinter import *
from tkinter import ttk, messagebox
# from tkinter.ttk import *
# import tkinter.messagebox as mb
from PIL import ImageTk, Image
import mysql.connector


class AdminRegister:

    def __init__(self, root):

        self.root = root
        self.root.title("Registration System for Admin (OSHES)")
        self.root.geometry("1280x700+200+70")
        self.root.resizable(False, False)
        # self.root.config(bg="white")

        # Adding image#

        self.image = ImageTk.PhotoImage(file="/Login/sales1.jpg")
        self.label = Label(self.root, image=self.image)
        self.label.pack()

        self.left = ImageTk.PhotoImage(file="/Login/sleek.jpg")
        left = Label(self.root, image=self.left)
        left.place(x=80, y=100, width=400, height=500)

        # Frame
        frame1 = Frame(self.root, bg="white")
        frame1.place(x=480, y=100, width=700, height=500)

        # Name, Gender, Email, Number, Address, Password and Re-enter Password
        title = Label(frame1, text="Admin Register with OSHES", font=("calibri", 20, "bold"), bg="white", fg="green")
        title.place(x=50, y=10)

        # Username
        adminID = Label(frame1, text="Username", font=("calibri", 15, "bold"), bg="white", fg="gray")
        adminID.place(x=50, y=120)

        self.adminID = Entry(frame1, font=("calibri", 15), bg="lightgray")
        self.adminID.place(x=50, y=150, width=250)

        # Name
        name = Label(frame1, text="Name", font=("calibri", 15, "bold"), bg="white", fg="gray")
        name.place(x=50, y=190)

        self.name = Entry(frame1, font=("calibri", 15), bg="lightgray")
        self.name.place(x=50, y=220, width=250)

        # Number
        number = Label(frame1, text="Phone Number", font=("calibri", 15, "bold"), bg="white", fg="gray")
        number.place(x=370, y=120)

        self.num = Entry(frame1, font=("calibri", 15), bg="lightgray")
        self.num.place(x=370, y=150, width=250)


        # Gender 1
        gender = Label(frame1, text="Gender", font=("calibri", 15, "bold"), bg="white", fg="gray")
        gender.place(x=370, y=190)

        '''
        var = StringVar()
        var.set('male')
        self.male_rb = Radiobutton(frame1, text='Male', bg="lightgray",variable=var, value="Male",font=("calibri",15))
        self.male_rb.place(x=370, y=200)
        self.female_rb = Radiobutton(frame1, text='Female', bg="lightgray",variable=var, value="Female",font=("calibri",15))
        self.female_rb.place(x=470, y=200)
        '''

        # Gender 2
        self.gender_cmb = ttk.Combobox(frame1, font=("calibri", 15), state='readonly', justify=CENTER)
        self.gender_cmb.place(x=370, y=220, width=200)
        self.gender_cmb['values'] = ("Select", "M", "F")
        self.gender_cmb.current(0)

        # Password
        password = Label(frame1, text="Password", font=("calibri", 15, "bold"), bg="white", fg="gray")
        password.place(x=50, y=330)

        self.pw = Entry(frame1, font=("calibri", 15), bg="lightgray", show="*")
        self.pw.place(x=50, y=360, width=250)

        # Confirm Password
        cpassword = Label(frame1, text="Confirm Password", font=("calibri", 15, "bold"), bg="white", fg="gray")
        cpassword.place(x=370, y=330)

        self.cpw = Entry(frame1, font=("calibri", 15), bg="lightgray", show="*")
        self.cpw.place(x=370, y=360, width=250)

        # Register Button

        reg = Button(frame1, text="Register", font=("Cambria", 15, "bold"), fg="white", bg="orange",
                     command=self.register_data)
        reg.place(x=50, y=420)

        back = Button(frame1, text="Back", font=("Cambria", 15, "bold"), fg="white", bg="orange",
                      command=self.destroyRegister)
        back.place(x=150, y=420)

    def register_data(self):
        if (self.adminID.get() == "" or self.name.get() == "" or self.num.get() == "" or self.gender_cmb.get() == "Select"
             or self.pw.get() == "" or self.cpw.get() == ""):
            messagebox.showerror("Error", "All fields are required to be filled up", parent=self.root)
        elif self.pw.get() != self.cpw.get():
            messagebox.showerror("Error", "Password does not match. Please try again.", parent=self.root)
        else:
            try:
                con = mysql.connector.connect(host="localhost", user="root", password="s63127734", database="oshes")
                cur = con.cursor()
                cur.execute(
                    "insert into Administrator (administratorID, name, gender, phoneNumber, password) values(%s,%s,%s,%s,%s)",
                    (self.adminID.get(),
                     self.name.get(),
                     self.gender_cmb.get(),
                     self.num.get(),
                     self.cpw.get()
                     )
                    )
                con.commit()
                con.close()
                messagebox.showinfo("Success", "Registration Successful", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Error due to: {str(es)}", parent=self.root)

    def destroyRegister(self):
        self.root.destroy()


if __name__ == "__main__":
    root = Tk()
    main = AdminRegister(root)
    root.mainloop()

