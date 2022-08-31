from tkinter import *
from tkinter import ttk, messagebox
# from tkinter.ttk import *
#import tkinter.messagebox as mb
from PIL import ImageTk, Image
import mysql.connector
from Profile import Profile
from Receipt import Bill_App
from CustomerSearchProduct import CustomerSearchProduct
from CustomerLog import HISTORY_App

class NewProduct:

    def __init__(self, root):

        self.root = root
        self.root.geometry("1800x1000+0+0")
        self.root.title("Product Catalogue")
        self.root.config(bg="azure")

        #title
        title = Label(self.root, text="Product Catalogue",
                      font=("Times New Roman", 40, "bold"), bg="#FFD1C1", fg="black",compound="center")
        title.place(x=0,y=0,relwidth=1,height=70)

        #Button Log Out
        btn_logout = Button(self.root, text="Logout", font=("Times New Roman", 15, "bold"),
                          bg="yellow", command=self.logout)
        btn_logout.place(x=1600, y=10, width=150, height=50)

        #Left Menu
        leftmenu=Frame(self.root, bd=2, relief=RIDGE,bg="white")
        leftmenu.place(x=0,y=102,width=200,height=850)

        lbl_account=Label(leftmenu, text="Account", font=("Times New Roman", 25, "bold"), bg="#009688")
        lbl_account.pack(side=TOP, fill=X)
        lbl_account.place(y=0, height=90, width=200)

        btn_profile = Button(leftmenu, text="Profile", font=("Times New Roman", 20, "bold"),
                             bg="white", bd=3, cursor="hand2", command=self.profileview)
        btn_profile.place(y=90, height=152, width=200)

        btn_product=Button(leftmenu, text="Search", font=("Times New Roman", 20, "bold"),bg="white",bd=3,cursor="hand2", command=self.searchview)
        btn_product.place(y=240, height=152, width=200)

        btn_purchase = Button(leftmenu, text="Purchase", font=("Times New Roman", 20, "bold"), bg="white", bd=3,
                             cursor="hand2", command=self.purchaseview)
        btn_purchase.place(y=390, height=152, width=200)

        btn_request = Button(leftmenu, text="Request", font=("Times New Roman", 20, "bold"), bg="white", bd=3,
                             cursor="hand2")
        btn_request.place(y=540, height=152, width=200)

        btn_service = Button(leftmenu, text="History", font=("Times New Roman", 20, "bold"), bg="white", bd=3,
                             cursor="hand2", command=self.history)
        btn_service.place(y=540, height=152, width=200)

        #Content

        #===========Text Description===========
        self.desc1 = Label(self.root, text="Products that are suitable for you. \n"
                                           "We provide lights and security for you.",
                           bg="azure", fg="black",
                           font=("goudy old style", 16, "bold")
                           )
        self.desc1.place(x=880, y=250)

        self.desc2 = Label(self.root, text="Come and browse for our products. \n"
                                           "We will ensure you that we are the best!",
                           bg="azure", fg="black",
                           font=("goudy old style", 16, "bold")
                           )
        self.desc2.place(x=880, y=780)

        #=======================Image for Products============================

        self.light1 = ImageTk.PhotoImage(file="/Login/lights1.jpg")
        self.light2 = ImageTk.PhotoImage(file="/Login/lights2.png")
        self.smarthome1 = ImageTk.PhotoImage(file="/Login/smartlight1.jpg")
        self.smarthome2 = ImageTk.PhotoImage(file="/Login/lock11.jpg")
        self.safe1 = ImageTk.PhotoImage(file="/Login/lock22.jpg")
        self.safe2 = ImageTk.PhotoImage(file="/Login/lock33.jpg")
        self.safe3 = ImageTk.PhotoImage(file="/Login/smartlock11.jpg")


        #Left
        self.img_Light1=Label(self.root, image=self.light1)
        self.img_Light1.place(x=400, y=200, height=200, width=400)

        self.lbl_Light1 = Label(self.root, text="Light1", bg="azure", fg="black",
                                font=("goudy old style", 15, "bold"))
        self.lbl_Light1.place(x=570, y=410)

        self.img_Light2 = Label(self.root, image=self.light2)
        self.img_Light2.place(x=400, y=450, height=200, width=400)

        self.lbl_Light1 = Label(self.root, text="Light2", bg="azure", fg="black",
                                font=("goudy old style", 15, "bold"))
        self.lbl_Light1.place(x=570, y=660)

        self.lbl_SmartHome1 = Label(self.root, image=self.smarthome1)
        self.lbl_SmartHome1.place(x=400, y=700, height=200, width=400)

        self.lbl_SmartHome1 = Label(self.root, text="SmartHome1", bg="azure", fg="black",
                                    font=("goudy old style", 15, "bold"))
        self.lbl_SmartHome1.place(x=540, y=910)


        #Middle
        self.img_SmartHome2 = Label(self.root, image=self.smarthome2)
        self.img_SmartHome2.place(x=850, y=450, height=200, width=400)

        self.lbl_SmartHome1 = Label(self.root, text="SmartHome1 (Locks)", bg="azure", fg="black",
                                    font=("goudy old style", 15, "bold"))
        self.lbl_SmartHome1.place(x=960, y=660)


        #Right
        self.img_Safe1 = Label(self.root, image=self.safe1)
        self.img_Safe1.place(x=1300, y=200, height=200, width=400)

        self.lbl_Safe1 = Label(self.root, text="Safe1", bg="azure", fg="black",
                                font=("goudy old style", 15, "bold"))
        self.lbl_Safe1.place(x=1470, y=410)

        self.img_Safe2 = Label(self.root, image=self.safe2)
        self.img_Safe2.place(x=1300, y=450, height=200, width=400)

        self.lbl_Safe2 = Label(self.root, text="Safe2", bg="azure", fg="black",
                                font=("goudy old style", 15, "bold"))
        self.lbl_Safe2.place(x=1470, y=660)

        self.img_Safe3 = Label(self.root, image=self.safe3)
        self.img_Safe3.place(x=1300, y=700, height=200, width=400)

        self.lbl_Safe3 = Label(self.root, text="Safe3", bg="azure", fg="black",
                                font=("goudy old style", 15, "bold"))
        self.lbl_Safe3.place(x=1470, y=910)
#=============================================================================

    def profileview(self):
        self.new_win = Toplevel(self.root)
        self.new_Obj = Profile(self.new_win)

    def purchaseview(self):
        self.new_win = Toplevel(self.root)
        self.new_Obj = Bill_App(self.new_win)

    def searchview(self):
        self.new_win = Toplevel(self.root)
        self.new_Obj = CustomerSearchProduct(self.new_win)

    def history(self):
        self.new_win = Toplevel(self.root)
        self.new_Obj = HISTORY_App(self.new_win)

    def logout(self):
        self.root.destroy()

if __name__ =="__main__":
    root=Tk()
    main = NewProduct(root)
    root.mainloop()




