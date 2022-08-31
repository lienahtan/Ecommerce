from tkinter import *
from tkinter import ttk, messagebox
# from tkinter.ttk import *
# import tkinter.messagebox as mb
from PIL import ImageTk, Image
import mysql.connector
from datetime import date

#root = Tk()


class RequestManagement:

    def __init__(self, root):

        self.root = root
        self.root.title("Admin Request Management Dashboard")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="ghost white")
        self.root.resizable(False, False)

        title = Label(self.root, text="Request Management", font=("calibri", 40, "bold"), bg="coral", fg="white")
        title.pack(side=TOP, fill=X)

        # =====All Variables=======
        f = open("store_adminID.txt", "r")
        profile_details = []
        for line in f:
            profile_details.append(line.rstrip())

        self.requestID = StringVar()
        self.requestStatus = StringVar()
        self.requestDate = StringVar()
        self.customerID = StringVar()
        self.administratorID = StringVar()
        self.administratorID.set(profile_details[0])
        self.itemID = StringVar()

        self.search_by=StringVar()
        self.search_txt=StringVar()

        # ======Manage Frame=======

        db_frame = Frame(self.root, bd=4, relief=RIDGE, bg="skyblue2")
        db_frame.place(x=20, y=100, width=450, height=560)

        db_title = Label(db_frame, text="Manage request", bg="skyblue2", fg="white", font=("calibri", 25, "bold"))
        db_title.grid(row=0, columnspan=2, pady=20)

        # ======Manage request=========

        requestID = Label(db_frame, text="Request ID", bg="skyblue2", fg="white", font=("calibri", 12, "bold"))
        requestID.grid(row=1, column=0, pady=10, padx=10, sticky="w")

        txt_id = Entry(db_frame, bd=5, textvariable=self.requestID, relief=GROOVE, bg="white", fg="black",
                       font=("calibri", 12, "bold"))
        txt_id.grid(row=1, column=1, pady=10, padx=10, sticky="w")

        iteID = Label(db_frame, text="Item ID", bg="skyblue2", fg="white", font=("calibri", 12, "bold"))
        iteID.grid(row=2, column=0, pady=10, padx=10, sticky="w")

        txt_item = Entry(db_frame, bd=5, textvariable=self.itemID, relief=GROOVE, bg="white", fg="black",
                       font=("calibri", 12, "bold"))
        txt_item.grid(row=2, column=1, pady=10, padx=10, sticky="w")

        adminID = Label(db_frame, text="Administrator ID", bg="skyblue2", fg="white", font=("calibri", 12, "bold"))
        adminID.grid(row=3, column=0, pady=10, padx=10, sticky="w")

        txt_admin = Entry(db_frame, bd=5, textvariable=self.administratorID, state="readonly", relief=GROOVE,
                          bg="white", fg="black",
                          font=("calibri", 12, "bold"))
        txt_admin.grid(row=3, column=1, pady=10, padx=10, sticky="w")

        # ======Button Frame for Request=========
        reqbutton = Frame(db_frame, bd=4, relief=RIDGE, bg="skyblue2")
        reqbutton.place(x=15, y=500, width=420)

        approveBtn = Button(reqbutton, text="Approve", width=20, command=self.ApproveRequest).grid(row=0, column=1, padx=20, pady=10)
        #serviceBtn = Button(reqbutton, text="Go to Service", width=20, command=self.GoToService).grid(row=0, column=2, padx=20, pady=10)

        # ======Detail Frame=======

        detail_frame = Frame(self.root, bd=4, relief=RIDGE, bg="skyblue2")
        detail_frame.place(x=500, y=100, width=800, height=560)

        lbl_search = Label(detail_frame, text="Search By", bg="skyblue2", fg="white", font=("calibri", 20, "bold"))
        lbl_search.grid(row=0, column=0, pady=20, padx=7, sticky="w")

        combo_search = ttk.Combobox(detail_frame, textvariable=self.search_by, font=("calibri", 12, "bold"),
                                    state="readonly")
        combo_search['values'] = ("requestID", "requestStatus")
        combo_search.grid(row=0, column=1, padx=6, pady=10)

        txt_Search = Entry(detail_frame, textvariable=self.search_txt, font=("calibri", 12, "bold"), bd=5,
                           relief=GROOVE)
        txt_Search.grid(row=0, column=2, pady=10, padx=6, sticky="w")

        searchBtn = Button(detail_frame, text="Search", width=10, command=self.search_data).grid(row=0, column=3,
                                                                                                 padx=6, pady=10)
        showallBtn = Button(detail_frame, text="Show All", width=10, command=self.fetch_data).grid(row=0, column=4,
                                                                                                   padx=6, pady=10)
        # ====== Table Frame ========

        table_frame = Frame(detail_frame, bd=4, relief=RIDGE, bg="skyblue2")
        table_frame.place(x=10, y=70, width=760, height=480)

        scroll_x = Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(table_frame, orient=VERTICAL)
        self.request_table = ttk.Treeview(table_frame,
                                          columns=("Request ID", "Request Status",
                                                   "Request Date", "Customer ID",
                                                   "Item ID"),
                                          xscrollcommand=scroll_x.set,
                                          yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.request_table.xview)
        scroll_y.config(command=self.request_table.yview)
        self.request_table.heading("Request ID", text="Request ID")
        self.request_table.heading("Request Status", text="Request Status")
        self.request_table.heading("Request Date", text="Request Date")
        self.request_table.heading("Customer ID", text="Customer ID")
        self.request_table.heading("Item ID", text="Item ID")
        #       self.product_table.heading("inventory", text="Inventory Level")
        self.request_table['show'] = 'headings'
        self.request_table.column("Request ID", width=100)
        self.request_table.column("Request Status", width=100)
        self.request_table.column("Request Date", width=100)
        self.request_table.column("Customer ID", width=100)
        self.request_table.column("Item ID", width=100)
        #     self.product_table.column("inventory",width=100)
        self.request_table.pack(fill=BOTH, expand=1)

        self.request_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()


    def get_cursor(self, ev):
        cursor_row = self.request_table.focus()
        contents = self.request_table.item(cursor_row)
        row = contents['values']
        self.requestID.set(row[0])
        self.requestStatus.set(row[1])
        self.requestDate.set(row[2])
        self.customerID.set(row[3])
        self.itemID.set(row[4])

    def fetch_data(self):
        con=mysql.connector.connect(host="localhost", user="root", password="s63127734", database="oshes")
        cur=con.cursor()
        cur.execute("select requestID, requestStatus, requestDate, customerID, itemID from Request")
        rows=cur.fetchall()
        if len(rows) != 0:
            self.request_table.delete(*self.request_table.get_children())
            for rows in rows:
                self.request_table.insert('', END, values=rows)
            con.commit()
        con.close()

#some problems with update the status in approval
    def ApproveRequest(self):
        if ((self.requestStatus.get() == 'Submitted') | (self.requestStatus.get() == 'In progress')):
            con = mysql.connector.connect(host="localhost", user="root", password="s63127734", database="oshes")
            cur = con.cursor()
            cur.execute("update Request set requestStatus= 'Approved' where requestID = %s ", (
                self.requestID.get(),
                ))
            cur.execute("update Item set serviceStatus='In progress' where itemID = %s ", (
                self.itemID.get(),
                ))
            cur.execute("update Request set administratorID = %s where requestID = %s ", (
                self.administratorID.get(),
                self.requestID.get()
                ))
            #GET TODAYS DATE AFTER APPROVAL
            cur.execute("update Request SET requestDate = %s where requestID = %s ",
                         str(date.today()), self.requestID.get())
            con.commit()
            self.fetch_data()
            self.clear()
            con.close()
        else:
            messagebox.showerror("Error", "Cannot approve this request!", parent=self.root)

    def clear(self):
        self.requestID.set("")
        self.requestStatus.set("")
        self.requestDate.set("")
        self.customerID.set("")
       # self.administratorID.set("")
        self.itemID.set("")

#how to clear the search result

    def search_data(self):
        con=mysql.connector.connect(host="localhost", user="root", password="s63127734", database="oshes")
        cur=con.cursor()
        cur.execute("select requestID, requestStatus, requestDate, customerID, itemID from Request where "
                    +str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%'")
        rows=cur.fetchall()
        if len(rows) != 0:
            self.request_table.delete(*self.request_table.get_children())
            for rows in rows:
                self.request_table.insert('',END,values=rows)
            con.commit()
        con.close()

if __name__ =="__main__":
    root=Tk()
    main = RequestManagement(root)
    root.mainloop()

