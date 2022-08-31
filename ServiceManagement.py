from tkinter import *
from tkinter import ttk, messagebox
# from tkinter.ttk import *
# import tkinter.messagebox as mb
from PIL import ImageTk, Image
import mysql.connector

#root=Tk()
class ServiceManagement:

    def __init__(self, root):

        self.root = root
        self.root.title("Admin Service Management Dashboard")
        self.root.geometry("1350x700+0+0")
        self.root.resizable(False, False)

        title = Label(self.root, text="Service Management", font=("calibri", 40, "bold"), bg="salmon", fg="white")
        title.pack(side=TOP, fill=X)

        # =====All Variables=======

        f = open("store_adminID.txt", "r")
        profile_details = []
        for line in f:
            profile_details.append(line.rstrip())

        self.itemID = StringVar()
        self.requestID = StringVar()
        self.requestStatus = StringVar()
        self.serviceStatus = StringVar()
        self.customerID = StringVar()
        self.administratorID = StringVar()
        self.administratorID.set(profile_details[0])

        self.search_by = StringVar()
        self.search_txt = StringVar()

        # ======Manage Frame=======

        db_frame = Frame(self.root, bd=4, relief=RIDGE, bg="peachpuff2")
        db_frame.place(x=20, y=100, width=450, height=560)

        db_title = Label(db_frame, text="Manage Service", bg="peachpuff2", fg="white", font=("calibri", 25, "bold"))
        db_title.grid(row=0, columnspan=2, pady=20)

        # ======Manage request=========

        iteID = Label(db_frame, text="Item ID", bg="peachpuff2", fg="white", font=("calibri", 12, "bold"))
        iteID.grid(row=1, column=0, pady=10, padx=10, sticky="w")
        txt_id = Entry(db_frame, bd=5, textvariable=self.itemID, relief=GROOVE, bg="white", fg="black",
                       font=("calibri", 12, "bold"))
        txt_id.grid(row=1, column=1, pady=10, padx=10, sticky="w")

        reqID = Label(db_frame, text="Request ID", bg="peachpuff2", fg="white", font=("calibri", 12, "bold"))
        reqID.grid(row=2, column=0, pady=10, padx=10, sticky="w")
        txt_id = Entry(db_frame, bd=5, textvariable=self.requestID, relief=GROOVE, bg="white", fg="black",
                       font=("calibri", 12, "bold"))
        txt_id.grid(row=2, column=1, pady=10, padx=10, sticky="w")

        adminID = Label(db_frame, text="Administrator ID", bg="peachpuff2", fg="white", font=("calibri", 12, "bold"))
        adminID.grid(row=3, column=0, pady=10, padx=10, sticky="w")
        txt_admin = Entry(db_frame, bd=5, textvariable=self.administratorID, state="readonly", relief=GROOVE,
                          bg="white", fg="black",
                          font=("calibri", 12, "bold"))
        txt_admin.grid(row=3, column=1, pady=10, padx=10, sticky="w")

        # ======Button Frame for Service=========
        reqbutton = Frame(db_frame, bd=4, relief=RIDGE, bg="peachpuff2")
        reqbutton.place(x=15, y=500, width=420)

        serveBtn = Button(reqbutton, text="Serve", width=10, command=self.Serve).grid(row=0, column=1, padx=30, pady=10)
        completeBtn = Button(reqbutton, text="Complete", width=10, command=self.Complete).grid(row=0, column=2, padx=30, pady=10)
        exitBtn = Button(reqbutton, text="Exit", width=10, command=self.Exit).grid(row=0, column=3, padx=30, pady=10)

        # ======Detail Frame=======

        detail_frame = Frame(self.root, bd=4, relief=RIDGE, bg="peachpuff2")
        detail_frame.place(x=500, y=100, width=800, height=560)

        lbl_search = Label(detail_frame, text="Search By", bg="peachpuff2", fg="white", font=("calibri", 20, "bold"))
        lbl_search.grid(row=0, column=0, pady=20, padx=7, sticky="w")

        combo_search = ttk.Combobox(detail_frame, textvariable=self.search_by, font=("calibri", 12, "bold"),
                                    state="readonly")
        combo_search['values'] = ("itemID", "requestID", "serviceStatus")
        combo_search.grid(row=0, column=1, padx=6, pady=10)

        txt_Search = Entry(detail_frame, textvariable=self.search_txt, font=("calibri", 12, "bold"), bd=5,
                           relief=GROOVE)
        txt_Search.grid(row=0, column=2, pady=10, padx=6, sticky="w")

        searchBtn = Button(detail_frame, text="Search", width=10, command=self.search_data).grid(row=0, column=3,
                                                                                                 padx=6, pady=10)
        showallBtn = Button(detail_frame, text="Show All", width=10, command=self.fetch_data).grid(row=0, column=4,
                                                                                                   padx=6, pady=10)
        # ====== Table Frame ========

        table_frame = Frame(detail_frame, bd=4, relief=RIDGE, bg="peachpuff2")
        table_frame.place(x=10, y=70, width=760, height=480)

        scroll_x = Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(table_frame, orient=VERTICAL)
        self.service_table = ttk.Treeview(table_frame,
                                          columns=("Item ID", "Request ID", "Request Status", "Service Status",
                                                   "Customer ID", "Administrator ID",),
                                          xscrollcommand=scroll_x.set,
                                          yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.service_table.xview)
        scroll_y.config(command=self.service_table.yview)
        self.service_table.heading("Item ID", text="Item ID")
        self.service_table.heading("Request ID", text="Request ID")
        self.service_table.heading("Request Status", text="Request Status")
        self.service_table.heading("Service Status", text="Service Status")
        self.service_table.heading("Customer ID", text="Customer ID")
        self.service_table.heading("Administrator ID", text="Administrator ID")
        #       self.product_table.heading("inventory", text="Inventory Level")
        self.service_table['show'] = 'headings'
        self.service_table.column("Item ID", width=100)
        self.service_table.column("Request ID", width=100)
        self.service_table.column("Request Status", width=100)
        self.service_table.column("Service Status", width=100)
        self.service_table.column("Customer ID", width=100)
        self.service_table.column("Administrator ID", width=100)
        #     self.product_table.column("inventory",width=100)
        self.service_table.pack(fill=BOTH, expand=1)

        self.service_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()


    def get_cursor(self, ev):
        cursor_row = self.service_table.focus()
        contents = self.service_table.item(cursor_row)
        row = contents['values']
        self.itemID.set(row[0])
        self.requestID.set(row[1])
        self.requestStatus.set(row[2])
        self.serviceStatus.set(row[3])
        self.customerID.set(row[4])
      #  self.administratorID.set(row[5])

    def fetch_data(self):
        con=mysql.connector.connect(host="localhost", user="root", password="s63127734", database="oshes")
        cur=con.cursor()
        cur.execute("select itemID, r.requestID, r.requestStatus, serviceStatus, i.customerID, i.administratorID from request AS r left join Item AS i using(itemID);")
        rows=cur.fetchall()
        if len(rows) != 0:
            self.service_table.delete(*self.service_table.get_children())
            for rows in rows:
                self.service_table.insert('', END, values=rows)
            con.commit()
        con.close()

#some problems with update the status in approval
    def Serve(self):
        con = mysql.connector.connect(host="localhost", user="root", password="s63127734", database="oshes")
        cur = con.cursor()
        cur.execute("update Item set administratorID = %s where itemID = %s ", (
            self.administratorID.get(),
            self.itemID.get(),
            ))
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()

    def Complete(self):
        con = mysql.connector.connect(host="localhost", user="root", password="s63127734", database="oshes")
        cur = con.cursor()
        cur.execute("update Item set serviceStatus = 'Completed' where itemID = %s ", (
            self.itemID.get(),
            ))
        cur.execute("update Request set requestStatus = 'Completed' where requestID = %s ", (
            self.requestID.get(),
            ))
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()

    def clear(self):
        self.itemID.set("")
        self.serviceStatus.set("")
        self.customerID.set("")
        #self.administratorID.set("")


#how to clear the search result

    def search_data(self):
        con=mysql.connector.connect(host="localhost", user="root", password="s63127734", database="oshes")
        cur=con.cursor()
        cur.execute("select itemID, r.requestID, r.requestStatus, serviceStatus, i.customerID, i.administratorID from request AS r left join Item AS i using(itemID) where "
                    +str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%'")
        rows=cur.fetchall()
        if len(rows) != 0:
            self.service_table.delete(*self.service_table.get_children())
            for rows in rows:
                self.service_table.insert('',END,values=rows)
            con.commit()
        con.close()

    def Exit(self):
        root.destroy()

if __name__ =="__main__":
    root=Tk()
    main = ServiceManagement(root)
    root.mainloop()
