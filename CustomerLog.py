from tkinter import *
import math, random, os
from tkinter import messagebox
import tkinter.ttk
import pymongo
from tkinter import ttk, messagebox
import mysql.connector
from ReqPayment import Request_Payment
from datetime import datetime
from datetime import timedelta, date

class HISTORY_App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1320x700+0+0")
        self.root.title("History Software")
        self.root.resizable(False, False)
        bg_color = "black"
        title = Label(self.root, text="CUSTOMER PURCHASE HISTORY", bd=15, bg="black", fg="white",
                      font=("times new roman", 30, "bold"), pady=2).pack(fill=X)

        # ================Cutomers==================================

        self.customerID = StringVar()
        self.itemID = StringVar()
        self.selectedID = StringVar()

        self.purchaseDate = StringVar()
        self.itemID = StringVar()
        self.modelID = StringVar()
        self.colour = StringVar()
        self.powerSupply = StringVar()



        #======================CUSTOMER DETAILS=========================

        F1 = LabelFrame(self.root, bd=8, text="Your Details", font=("times new roman", 25, "bold"), fg="white",
                        bg=bg_color)
        F1.place(x=0, y=80, relwidth=1)

        customerID = Label(F1, text="Customer ID", bg=bg_color, fg="White", font=("times new roman", 15, "bold")).grid(
            row=0, column=0, padx=0, pady=0)
        customerID_txt = Entry(F1, width=15, textvariable=self.customerID, font="arial 12", bd=7, relief=SUNKEN).grid(row=0,
                                                                                                                 column=1,
                                                                                                                 pady=0,
                                                                                                                 padx=3)


        bill_btn = Button(F1, text="Search", command=self.search_data, width=10, bd=7, font="arial 12").grid(row=0, column=6,
                                                                                                       padx=20, pady=3)



        #==========make a request=========
        F6 = Frame(self.root, bd=8, relief=GROOVE, bg="white")
        F6.place(x=1120, y=180, width=200, height=520)
        wantToMakeReq = Label(F6, text="Press Here to\n\nMake a Request\nOR\nSearch for a Request", bg="white", fg="red",
                           font=("times new roman", 13, "bold")).place(x=0, y=0, width=175, height=100)

        reqbutton = Button(F6, text="Search\Make Rquest\nFor Item ID", command=self.moveToReq, width=10, bd=7, font="arial 13").place(x=0, y=150, width=175, height=75)
        displayID = Entry(F6, width=15, textvariable=self.itemID, font="arial 12", bd=7, relief=SUNKEN, state="readonly").place(x=0, y= 240, width=175, height=40)


        #====================search results==============
        F5 = Frame(self.root, bd=8, relief=GROOVE)
        F5.place(x=0, y=180, width=1120, height=520)


        search_results_title = Label(F5, text="Search Results",font="arial 15 bold", bd=7, relief=GROOVE).pack(fill=X)
        scroll_x = Scrollbar(F5, orient=HORIZONTAL)
        scroll_y = Scrollbar(F5, orient=VERTICAL)
        self.product_table = ttk.Treeview(F5,
                                          columns=("purchaseDate", "itemID", "productID", "colour", "powerSupply"),
                                          xscrollcommand=scroll_x.set,
                                          yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.product_table.xview)
        scroll_y.config(command=self.product_table.yview)
        self.product_table.heading("purchaseDate", text="Purchased Date")
        self.product_table.heading("itemID", text="ItemID")
        self.product_table.heading("productID", text="Model")
        self.product_table.heading("colour", text="Colour")
        self.product_table.heading("powerSupply", text="Power Supply")
        #self.product_table.heading("cost", text="Cost")
        #self.product_table.heading("warrantyDuration", text="Warranty")

        #       self.product_table.heading("inventory", text="Inventory Level")
        self.product_table['show'] = 'headings'
        self.product_table.column("purchaseDate", width=100)
        self.product_table.column("itemID", width=100)
        self.product_table.column("productID", width=100)
        self.product_table.column("colour", width=100)
        self.product_table.column("powerSupply", width=100)
        #self.product_table.column("warrantyDuration", width=100)

        #     self.product_table.column("inventory",width=100)
        self.product_table.pack(fill=BOTH, expand=1)
        ttk.Style().configure(F5, background = "#FF0FFF", rowheight = 40)

        self.product_table.bind("<ButtonRelease-1>", self.get_cursor)

        tkinter.ttk.Separator(F5, orient=VERTICAL).place(x=218, y=40, width=2, height=445)
        tkinter.ttk.Separator(F5, orient=VERTICAL).place(x=433, y=40, width=2, height=445)
        tkinter.ttk.Separator(F5, orient=VERTICAL).place(x=650, y=40, width=2, height=445)
        tkinter.ttk.Separator(F5, orient=VERTICAL).place(x=868, y=40, width=2, height=445)

        con = mysql.connector.connect(host="localhost", user="root", password="s63127734", database="oshes")
        cur = con.cursor()
        cur.execute("select creationDate from servicefee where requestID =%s", (self.itemID.get(),))
        row = cur.fetchone()

        if row == None:
            print()
        else:
            if row + timedelta(days=10) < date.today():
                cur.execute("UPDATE request SET requestStatus = 'Canceled' WHERE itemID = %s", (self.itemID.get(),))
                cur.execute("UPDATE servicefee SET paymentID = '' WHERE requestID = %s", (self.itemID.get(),))

        con.commit()
        con.close()

    def get_cursor(self, ev):
        cursor_row = self.product_table.focus()
        contents = self.product_table.item(cursor_row)
        row = contents['values']
        self.purchaseDate.set(row[0])
        self.itemID.set(row[1])
        self.modelID.set(row[2])
        self.colour.set(row[3])
        self.powerSupply.set(row[4]) #waiting for prize


    # =========== search data that correspond to Customer ID ==============
    def search_data(self):
        con = mysql.connector.connect(host="localhost", user="root", password="s63127734", database="oshes")
        cur = con.cursor()
        cur.execute("select * from oshes.item")
        rows = cur.fetchall()

        if len(rows) != 0:
            self.product_table.delete(*self.product_table.get_children())
            for row in rows:
                if row[9] == self.customerID.get():
                    holder = [row[10], row[0], row[8], row[4], row[5]]
                    if row[8] == "001":  # 1410
                        holder = [row[10], row[0], "Category: Light, Model: Light 1", row[4], row[5]]
                    if row[8] == "002":  # 1410
                        holder = [row[10], row[0], "Category: Light, Model: Light 2", row[4], row[5]]

                    if row[8] == "003":  # 1410
                        holder = [row[10], row[0], "Category: Light, Model: SmartHome1", row[4], row[5]]

                    if row[8] == "004":  # 1410
                        holder = [row[10], row[0], "Category: Safe, Model: Safe 1", row[4], row[5]]

                    if row[8] == "005":  # 1410
                        holder = [row[10], row[0], "Category: Safe, Model: Safe 2", row[4], row[5]]

                    if row[8] == "006":  # 1410
                        holder = [row[10], row[0], "Category: Safe, Model: Safe 3", row[4], row[5]]

                    if row[8] == "007":  # 1410
                        holder = [row[10], row[0], "Category: Safe, Model: SmartHome1", row[4], row[5]]
                    self.product_table.insert('', END, values=holder)
            con.commit()
        con.close()


    def moveToReq(self):
        if self.itemID.get() == "":
            messagebox.showerror("Error", "Please select an item")

        else:
            con = mysql.connector.connect(host="localhost", user="root", password="s63127734", database="oshes")
            cur = con.cursor()
            cur.execute("select * from Item where itemID =%s", (self.itemID.get(),))
            row = cur.fetchone()
            #if there is a request, SEAERCH FOR A REQUEST that corrrespeond ot

            f = open("store_itemID.txt", "w")
            for t in row:
                if t == None:
                    f.write("NULL" + "\n")
                else:
                    try:
                        f.write(''.join(str(s) for s in t.strftime("%Y-%m-%d")) + "\n")
                    except:
                        f.write(''.join(str(s) for s in t) + "\n")
            f.close()

        self.new_window = Toplevel(self.root)
        self.new_object = Request_Payment(self.new_window)




if __name__ == "__main__":
    root = Tk()
    obj = HISTORY_App(root)
    root.mainloop()