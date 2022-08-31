from tkinter import *
from tkinter import ttk, messagebox
# from tkinter.ttk import *
#import tkinter.messagebox as mb
from PIL import ImageTk, Image
from pymongo import MongoClient
import mysql.connector
client = MongoClient('localhost', 27017)
db = client["OSHES"]
itemcol = db["items"]
procol = db["product"]



class Import:

    def __init__(self, root):

        self.root = root
        self.root.title("Data Import System")
        self.root.geometry("1350x700+0+0")
        self.root.resizable(False, False)

        title = Label(self.root, text="Data Import System", font=("calibri", 40, "bold"), bg="light blue", fg="white")
        title.pack(side=TOP, fill=X)

        # Import Frame

        self.frame1 = Frame(self.root, bg="black")
        self.frame1.place(x=375, y=140, height=420, width=480)

        self.frame = Frame(self.root, bg="light blue")
        self.frame.place(x=390, y=150, height=400, width=450)

        #Label and Boxes in Frame
        self.title = Label(self.frame, text = "Data Import System", font=("Calibri", 20, 'bold', "underline"), bg = "light blue")
        self.title.place(x=100, y=10)

        self.serverlabel = Label(self.frame, text="MySQL SERVER INFORMATION", font=("Calibri", 15, 'bold'),
                                    bg="light blue")
        self.serverlabel.place(x=80, y=50, width=260)

        self.hostlabel = Label(self.frame, text = "HOST", font=("Calibri", 15, 'bold'), bg="light blue")
        self.hostlabel.place(x=80, y=80)

        self.host = Entry(self.frame, font=("times new roman", 15, 'bold'))
        self.host.place(x=80, y=110, width=250)

        self.databaselabel = Label(self.frame, text = "DATABASE", font=("Calibri", 15, 'bold'), bg="light blue")
        self.databaselabel.place(x=80, y=140)

        self.database = Entry(self.frame, font=("times new roman", 15, 'bold'))
        self.database.place(x=80, y=170, width=250)

        self.userlabel = Label(self.frame, text="USER", font=("Calibri", 15, 'bold'), bg="light blue")
        self.userlabel.place(x=80, y=200)

        self.user = Entry(self.frame, font=("times new roman", 15, 'bold'))
        self.user.place(x=80, y=230, width=250)

        self.passwordlabel = Label(self.frame, text="PASSWORD", font=("Calibri", 15, 'bold'), bg="light blue")
        self.passwordlabel.place(x=80, y=260)

        self.password = Entry(self.frame, font=("times new roman", 15, 'bold'))
        self.password.place(x=80, y=290, width=250)

        self.importButton = Button(self.frame, text="Import", activebackground="#00B0F0",
                                  activeforeground="white", fg="white",
                                  bg="crimson", font=("Calibri", 15, 'bold'), command=self.import_data)
        self.importButton.place(x=150, y=330, width=150)

    def import_data(self):
        if (self.host.get() == "") :
            messagebox.showerror("Error", "Please enter the host of your server", parent=self.root)
        elif (self.database.get() == "") :
            messagebox.showerror("Error", "Please enter the database of your server", parent=self.root)
        elif (self.user.get() == "") :
            messagebox.showerror("Error", "Please enter the user of your server", parent=self.root)
        elif (self.password.get() == "") :
            messagebox.showerror("Error", "Please enter the password of your server", parent=self.root)
        else:
            try:
                productList = list(procol.find())
                itemList = list(itemcol.find())
                print(productList)

                connection = mysql.connector.connect(host=self.host.get(),
                                                     database=self.database.get(),
                                                     user=self.user.get(),
                                                     password=self.password.get())

                mySql_insert_query1 = """INSERT INTO Product
                                       VALUES (%s, %s, %s, %s, %s, %s) """

                records_to_insert1 = []
                for product in productList:
                    records_to_insert1.append((product['ProductID'], product['Model'], product['Category'], product['Price'],
                                              product['Cost'], product['Warranty']))

                cursor1 = connection.cursor()
                cursor1.executemany(mySql_insert_query1, records_to_insert1)
                connection.commit()
                messagebox.showinfo("Success",str(cursor1.rowcount) + " Record inserted successfully into Product table", parent=self.root)
                print(cursor1.rowcount, "Record inserted successfully into Product table")

                productDict = dict()
                for product in productList:
                    productDict[(product['Category'], product['Model'])] = product['ProductID']

                mySql_insert_query2 = """INSERT INTO Item
                                                       VALUES (%s, %s, %s, %s, %s, %s, NULL, NULL, %s, NULL, NULL) """

                records_to_insert2 = []
                for item in itemList:
                    records_to_insert2.append((item['ItemID'], item['PurchaseStatus'], item['Factory'], item['ProductionYear'],
                                              item['Color'], item['PowerSupply'], productDict[(item['Category'], item['Model'])]))


                cursor2 = connection.cursor()
                cursor2.executemany(mySql_insert_query2, records_to_insert2)
                connection.commit()
                messagebox.showinfo("Success", str(cursor2.rowcount) + " Record inserted successfully into Item table",
                                    parent=self.root)
                print(cursor2.rowcount, "record inserted successfully into Item table")

                cursor1.close()
                cursor2.close()
                connection.close()


            except mysql.connector.Error as error:
                messagebox.showerror("Error", "Failed to insert record into MySQL table {}".format(error), parent=self.root)
                print("Failed to insert record into MySQL table {}".format(error))

if __name__ =="__main__":
    root = Tk()
    main = Import(root)
    root.mainloop()