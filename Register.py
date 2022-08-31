from tkinter import *
# from tkinter.ttk import *
#import tkinter.messagebox as mb
from PIL import ImageTk, Image

root=Tk()

def backtoLogin():
    root.destroy()
    import Login
    
class Register:

    def __init__(self, root):
        
        self.root = root
        self.root.title("Login System (OSHES)")
        self.root.geometry("1280x700+200+70")
        self.root.resizable(False, False)
       # self.root.config(bg="white")

        #Adding image#

        self.image=ImageTk.PhotoImage(file="/Login/light5.jpg")
        self.label=Label(self.root, image=self.image)
        self.label.pack()

        self.left=ImageTk.PhotoImage(file="/Login/light4.jpg")
        left=Label(self.root, image=self.left)
        left.place(x=80, y=100, width=400, height=500)
        

        #Frame
        frame1=Frame(self.root, bg="white")
        frame1.place(x=480, y=100, width=700, height=500)

        #Name, Gender, Email, Number, Address, Password and Re-enter Password
        title = Label(frame1, text = "Register with OSHES", font=("calibri",20,"bold"),bg="white", fg="green")
        title.place(x=50, y=30)

        #Name
        name = Label(frame1, text = "Name", font=("calibri",15,"bold"),bg="white", fg="gray")
        name.place(x=50,y=100)
        
        txt_name = Entry(frame1, font=("calibri",15), bg="lightgray")
        txt_name.place(x=50, y=130, width=250)

        #Number
        number = Label(frame1, text = "Number", font=("calibri",15,"bold"),bg="white", fg="gray")
        number.place(x=370,y=100)
        
        txt_num = Entry(frame1, font=("calibri",15), bg="lightgray")
        txt_num.place(x=370, y=130, width=250)

        #Email
        email = Label(frame1, text = "Email", font=("calibri",15,"bold"),bg="white", fg="gray")
        email.place(x=50,y=170)
        
        txt_email = Entry(frame1, font=("calibri",15), bg="lightgray")
        txt_email.place(x=50, y=200, width=250)

        #Gender
        gender = Label(frame1, text = "Gender", font=("calibri",15,"bold"),bg="white", fg="gray")
        gender.place(x=370,y=170)

        var = StringVar()
        var.set('male')
        male_rb = Radiobutton(frame1, text='Male', bg="lightgray",variable=var, value="Male",font=("calibri",15))
        male_rb.place(x=370, y=200)
        female_rb = Radiobutton(frame1, text='Female', bg="lightgray",variable=var, value="Female",font=("calibri",15))
        female_rb.place(x=470, y=200)

        #Address
        address = Label(frame1, text = "Address", font=("calibri",15,"bold"),bg="white", fg="gray")
        address.place(x=50,y=240)
        
        txt_address = Entry(frame1, font=("calibri",15), bg="lightgray")
        txt_address.place(x=50, y=270, width=350)

        #Password
        password = Label(frame1, text = "Password", font=("calibri",15,"bold"),bg="white", fg="gray")
        password.place(x=50,y=310)
        
        txt_pw = Entry(frame1, font=("calibri",15), bg="lightgray")
        txt_pw.place(x=50, y=340, width=250)
        
        #Confirm Password
        cpassword = Label(frame1, text = "Confirm Password", font=("calibri",15,"bold"),bg="white", fg="gray")
        cpassword.place(x=370,y=310)
        
        txt_cpw = Entry(frame1, font=("calibri",15), bg="lightgray")
        txt_cpw.place(x=370, y=340, width=250)

        #Register Button

        reg=Button(frame1, text="Register", font=("Cambria", 15, "bold"), fg="white", bg="orange")
        reg.place(x=50, y=420)

        back=Button(frame1, text="Back", font=("Cambria", 15, "bold"), fg="white", bg="orange", command=backtoLogin)
        back.place(x=150, y=420)

main = Register(root)
root.mainloop()
        
