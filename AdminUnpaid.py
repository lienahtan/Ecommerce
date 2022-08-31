from tkinter import *
from tkinter import ttk, messagebox
# from tkinter.ttk import *
# import tkinter.messagebox as mb
from PIL import ImageTk, Image
import mysql.connector

class AdminSearchCustomers:

    def __init__(self, root):

        self.root = root
        self.root.title("Admin Search Customers with unpaid Service Fees")
        self.root.geometry("1350x700+0+0")
        self.root.resizable(False, False)

        title = Label(self.root, text="Customers with unpaid service fees", font=("calibri", 40, "bold"), bg="light blue", fg="white")
        title.pack(side=TOP, fill=X)

        # ======Detail Frame=======

        detail_frame = Frame(self.root, bd=4, relief=RIDGE, bg="crimson")
        detail_frame.place(x=60, y=100, width=1200, height=550)

        # ====== Table Frame ========

        table_frame = Frame(detail_frame, bd=4, relief=RIDGE, bg="crimson")
        table_frame.place(x=110, y=40, width=1000, height=450)

        scroll_x = Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(table_frame, orient=VERTICAL)
        self.search_table = ttk.Treeview(table_frame,
                                          columns=("Customer ID", "Name",
                                                   "Gender", "Email",
                                                   "Phone Number"),
                                          xscrollcommand=scroll_x.set,
                                          yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.search_table.xview)
        scroll_y.config(command=self.search_table.yview)
        self.search_table.heading("Customer ID", text="Customer ID")
        self.search_table.heading("Name", text="Name")
        self.search_table.heading("Gender", text="Gender")
        self.search_table.heading("Email", text="Email")
        self.search_table.heading("Phone Number", text="Phone Number")
        #       self.product_table.heading("inventory", text="Inventory Level")
        self.search_table['show'] = 'headings'
        self.search_table.column("Customer ID", width=100)
        self.search_table.column("Name", width=100)
        self.search_table.column("Gender", width=100)
        self.search_table.column("Email", width=100)
        self.search_table.column("Phone Number", width=100)
        #     self.product_table.column("inventory",width=100)
        self.search_table.pack(fill=BOTH, expand=1)

        self.search_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.search_data()

#how to clear the search result

    def get_cursor(self, ev):
        cursor_row = self.search_table.focus()
        contents = self.search_table.item(cursor_row)
        row = contents['values']
        self.itemID.set(row[0])
        self.requestID.set(row[1])
        self.requestStatus.set(row[2])
        self.serviceStatus.set(row[3])
        self.customerID.set(row[4])
        self.administratorID.set(row[5])

    def search_data(self):
        con=mysql.connector.connect(host="localhost", user="root", password="s63127734", database="oshes")
        cur=con.cursor()
        cur.execute("SELECT c.customerID, name, gender, email, phonenumber "
                    "FROM Customer AS c inner join request AS r "
                    "USING (customerID) WHERE requestStatus = 'Submitted and Waiting for payment'"
                    "or requestStatus = 'Canceled'")
        rows=cur.fetchall()
        if len(rows) != 0:
            self.search_table.delete(*self.search_table.get_children())
            for rows in rows:
                self.search_table.insert('',END,values=rows)
            con.commit()
        con.close()

if __name__ =="__main__":
    root=Tk()
    main = AdminSearchCustomers(root)
    root.mainloop()
