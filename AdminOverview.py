from tkinter import *
from tkinter import ttk, messagebox
# from tkinter.ttk import *
#import tkinter.messagebox as mb
from PIL import ImageTk, Image
import mysql.connector
from AdminSearchProduct import AdminSearchProduct
from AdminSearchItem import AdminSearchItem
from RequestManagement import RequestManagement
from ServiceManagement import ServiceManagement
from AdminUnpaid import AdminSearchCustomers
from AdminRegister import AdminRegister
from ProductTable import DisplayProduct
from Import import Import

class AdminOverview:

    def __init__(self, root):

        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Admin Dashboard Overview")
        self.root.config(bg="white")
        self.root.resizable(False, False)

        #title
        title = Label(self.root, text="Admin Dashboard Overview",
                      font=("Times New Roman", 40, "bold"), bg="#010c48", fg="white",
                      anchor="w", compound="left",padx=20)
        title.place(x=0,y=0,relwidth=1,height=70)

        #Button Log Out
        btn_logout = Button(self.root, text="Logout", font=("Times New Roman", 15, "bold"),
                          bg="yellow", command=self.logout)
        btn_logout.place(x=1100, y=10, width=150, height=50)

        #Left Menu
        leftmenu=Frame(self.root, bd=2, relief=RIDGE,bg="white")
        leftmenu.place(x=0,y=102,width=200,height=565)

        lbl_menu=Label(leftmenu, text="Menu", font=("Times New Roman", 15, "bold"), bg="#009688")
        lbl_menu.pack(side=TOP, fill=X)

        btn_product=Button(leftmenu, text="Product", command=self.product, font=("Times New Roman", 20, "bold"),bg="white",bd=3,cursor="hand2")
        btn_product.pack(side=TOP,fill=X)

        btn_item = Button(leftmenu, text="Item", command=self.item, font=("Times New Roman", 20, "bold"), bg="white", bd=3,
                             cursor="hand2")
        btn_item.pack(side=TOP, fill=X)

        btn_request = Button(leftmenu, text="Request", font=("Times New Roman", 20, "bold"), bg="white", bd=3,
                             cursor="hand2", command=self.request)
        btn_request.pack(side=TOP, fill=X)

        btn_customer = Button(leftmenu, text="Customer", font=("Times New Roman", 20, "bold"), bg="white", bd=3,
                             cursor="hand2", command=self.unpaid)
        btn_customer.pack(side=TOP, fill=X)

        btn_Service= Button(leftmenu, text="Service", font=("Times New Roman", 20, "bold"), bg="white", bd=3,
                              cursor="hand2", command=self.service)
        btn_Service.pack(side=TOP, fill=X)

        btn_Register = Button(leftmenu, text="Register", font=("Times New Roman", 20, "bold"), bg="white", bd=3,
                             cursor="hand2", command=self.register)
        btn_Register.pack(side=TOP, fill=X)

        btn_Sales = Button(leftmenu, text="Sales", font=("Times New Roman", 20, "bold"), bg="white", bd=3,
                             cursor="hand2", command=self.sales)
        btn_Sales.pack(side=TOP, fill=X)

        btn_Import = Button(leftmenu, text="Import", font=("Times New Roman", 20, "bold"), bg="white", bd=3,
                           cursor="hand2", command=self.importData)
        btn_Import.pack(side=TOP, fill=X)

        btn_Initialisation = Button(leftmenu, text="Initialisation", font=("Times New Roman", 20, "bold"), bg="white", bd=3,
                           cursor="hand2", command=self.initialisation)
        btn_Initialisation.pack(side=TOP, fill=X)


        #Content

        self.lbl_product=Label(self.root,text="Total Product\n[ 7 ]", bg="#607d8b", fg="white",
                               font=("goudy old style", 20, "bold"), bd=5)
        self.lbl_product.place(x=400,y=200, height=150,width=300)

        self.lbl_item = Label(self.root, text="Total Item\n[ 1001 ]", bg="#ff5722", fg="white",
                                 font=("goudy old style", 20, "bold"), bd=5)
        self.lbl_item.place(x=850, y=200, height=150, width=300)

        self.lbl_request = Label(self.root, text="Total Request\n[ 0 ]", bg="#009688", fg="white",
                                 font=("goudy old style", 20, "bold"), bd=5)
        self.lbl_request.place(x=400, y=400, height=150, width=300)

        self.lbl_customer = Label(self.root, text="Total Customer\n[ 0 ]", bg="#ffc107", fg="white",
                                 font=("goudy old style", 20, "bold"), bd=5)
        self.lbl_customer.place(x=850, y=400, height=150, width=300)

        self.update_details()

    def update_details(self):
        con = mysql.connector.connect(host="localhost", user="root", password="s63127734", database="oshes")
        cur = con.cursor()
        try:
            # cur.execute("select * from Request")
            # cr = cur.fetchall()
            # self.lbl_request.config(text=f"Total Request\n[{str(len(cr))}]")
            #self.lbl_request.after(200, self.update_details)
            cur.execute("select * from Customer")
            cr = cur.fetchall()
            self.lbl_customer.config(text=f"Total Customer\n[{str(len(cr))}]")
            #self.lbl_customer.after(200, self.update_details)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")


    def product(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=AdminSearchProduct(self.new_win)

    def request(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=RequestManagement(self.new_win)
        con = mysql.connector.connect(host="localhost", user="root", password="s63127734", database="oshes")
        cur = con.cursor()
        cur.execute("select * from Request")
        cr = cur.fetchall()
        cur.execute("update Request as r left join ServiceFee as s on r.requestID = s.requestID "
                    "left join Payment as p on s.paymentID = p.paymentID set r.requestStatus = 'Canceled' "
                    "where p.paymentID is null and timestampdiff(day, requestDate, curdate()) > 10")
        con.commit()
        con.close()
        self.lbl_request.config(text=f"Total Request\n[{str(len(cr))}]")

    def service(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=ServiceManagement(self.new_win)

    def item(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=AdminSearchItem(self.new_win)

    def unpaid(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=AdminSearchCustomers(self.new_win)

    def register(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = AdminRegister(self.new_win)

    def sales(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = DisplayProduct(self.new_win)

    def importData(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = Import(self.new_win)


    def initialisation(self):
        import MySQLInitialization

    def logout(self):
        self.root.destroy()

if __name__ =="__main__":
    root=Tk()
    main = AdminOverview(root)
    root.mainloop()




