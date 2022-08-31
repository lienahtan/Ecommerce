from tkinter import *
from tkinter import ttk, messagebox
# from tkinter.ttk import *
# import tkinter.messagebox as mb
from PIL import ImageTk, Image
import mysql.connector


class AdminDB:

    def __init__(self, root):

        self.root = root
        self.root.title("Admin OSHES Dashboard")
        self.root.geometry("1350x700+0+0")
        self.root.resizable(False, False)

        title = Label(self.root, text="OSHES Dashboard", font=("calibri", 40, "bold"), bg="light blue", fg="white")
        title.pack(side=TOP, fill=X)

        # =====All Variables=======

        self.id_var = StringVar()
        self.cost_var = StringVar()
        self.price_var = StringVar()
        self.model_var = StringVar()
        self.category_var = StringVar()
        self.warranty_var = StringVar()
        self.inventory_var = StringVar()

        self.search_by = StringVar()
        self.search_txt = StringVar()

        # ======Manage Frame=======

        db_frame = Frame(self.root, bd=4, relief=RIDGE, bg="crimson")
        db_frame.place(x=20, y=100, width=450, height=560)

        db_title = Label(db_frame, text="Manage Inventory", bg="crimson", fg="white", font=("calibri", 25, "bold"))
        db_title.grid(row=0, columnspan=2, pady=20)

        # ======Manage Product=========

        productID = Label(db_frame, text="Product ID", bg="crimson", fg="white", font=("calibri", 12, "bold"))
        productID.grid(row=1, column=0, pady=10, padx=10, sticky="w")

        txt_id = Entry(db_frame, bd=5, textvariable=self.id_var, relief=GROOVE, bg="white", fg="black",
                       font=("calibri", 12, "bold"))
        txt_id.grid(row=1, column=1, pady=10, padx=10, sticky="w")

        model = Label(db_frame, text="Model", bg="crimson", fg="white", font=("calibri", 12, "bold"))
        model.grid(row=2, column=0, pady=10, padx=10, sticky="w")

        txt_model = Entry(db_frame, bd=5, textvariable=self.model_var, relief=GROOVE, bg="white", fg="black",
                          font=("calibri", 12, "bold"))
        txt_model.grid(row=2, column=1, pady=10, padx=10, sticky="w")

        category = Label(db_frame, text="Category", bg="crimson", fg="white", font=("calibri", 12, "bold"))
        category.grid(row=3, column=0, pady=10, padx=10, sticky="w")

        txt_category = Entry(db_frame, bd=5, textvariable=self.category_var, relief=GROOVE, bg="white", fg="black",
                             font=("calibri", 12, "bold"))
        txt_category.grid(row=3, column=1, pady=10, padx=10, sticky="w")

        price = Label(db_frame, text="Price", bg="crimson", fg="white", font=("calibri", 12, "bold"))
        price.grid(row=4, column=0, pady=10, padx=10, sticky="w")

        txt_price = Entry(db_frame, bd=5, textvariable=self.price_var, relief=GROOVE, bg="white", fg="black",
                          font=("calibri", 12, "bold"))
        txt_price.grid(row=4, column=1, pady=10, padx=10, sticky="w")

        cost = Label(db_frame, text="Cost", bg="crimson", fg="white", font=("calibri", 12, "bold"))
        cost.grid(row=5, column=0, pady=10, padx=10, sticky="w")

        txt_cost = Entry(db_frame, bd=5, textvariable=self.cost_var, relief=GROOVE, bg="white", fg="black",
                         font=("calibri", 12, "bold"))
        txt_cost.grid(row=5, column=1, pady=10, padx=10, sticky="w")

        warranty = Label(db_frame, text="Warranty", bg="crimson", fg="white", font=("calibri", 12, "bold"))
        warranty.grid(row=6, column=0, pady=10, padx=10, sticky="w")

        txt_warranty = Entry(db_frame, bd=5, textvariable=self.warranty_var, relief=GROOVE, bg="white", fg="black",
                             font=("calibri", 12, "bold"))
        txt_warranty.grid(row=6, column=1, pady=10, padx=10, sticky="w")

        inventory = Label(db_frame, text="Inventory", bg="crimson", fg="white", font=("calibri", 12, "bold"))
        inventory.grid(row=7, column=0, pady=10, padx=10, sticky="w")

        txt_inventory = Entry(db_frame, bd=5, textvariable=self.inventory_var, relief=GROOVE, bg="white", fg="black",
                              font=("calibri", 12, "bold"))
        txt_inventory.grid(row=7, column=1, pady=10, padx=10, sticky="w")

        # ======Button Frame for Product=========
        prodbutton = Frame(db_frame, bd=4, relief=RIDGE, bg="crimson")
        prodbutton.place(x=15, y=500, width=420)

        addBtn = Button(prodbutton, text="Add", width=10, command=self.add_products).grid(row=0, column=0, padx=10,
                                                                                          pady=10)
        updateBtn = Button(prodbutton, text="Update", width=10, command=self.update_data).grid(row=0, column=1, padx=10,
                                                                                               pady=10)
        deleteBtn = Button(prodbutton, text="Delete", width=10, command=self.delete_data).grid(row=0, column=2, padx=10,
                                                                                               pady=10)
        clearBtn = Button(prodbutton, text="Clear", width=10, command=self.clear).grid(row=0, column=3, padx=10,
                                                                                       pady=10)

        # ======Detail Frame=======

        detail_frame = Frame(self.root, bd=4, relief=RIDGE, bg="crimson")
        detail_frame.place(x=500, y=100, width=800, height=560)

        lbl_search = Label(detail_frame, text="Search By", bg="crimson", fg="white", font=("calibri", 20, "bold"))
        lbl_search.grid(row=0, column=0, pady=10, padx=20, sticky="w")

        combo_search = ttk.Combobox(detail_frame, textvariable=self.search_by, font=("calibri", 12, "bold"),
                                    state="readonly")
        combo_search['values'] = ("productID", "productModel", "category")
        combo_search.grid(row=0, column=1, padx=20, pady=10)

        txt_Search = Entry(detail_frame, textvariable=self.search_txt, font=("calibri", 12, "bold"), bd=5,
                           relief=GROOVE)
        txt_Search.grid(row=0, column=2, pady=10, padx=20, sticky="w")

        searchBtn = Button(detail_frame, text="Search", width=10, command=self.search_data).grid(row=0, column=3,
                                                                                                 padx=10, pady=10)
        showallBtn = Button(detail_frame, text="Show All", width=10, command=self.fetch_data).grid(row=0, column=4,
                                                                                                   padx=10, pady=10)

        # ====== Table Frame ========

        table_frame = Frame(detail_frame, bd=4, relief=RIDGE, bg="crimson")
        table_frame.place(x=10, y=70, width=760, height=480)

        scroll_x = Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(table_frame, orient=VERTICAL)
        self.product_table = ttk.Treeview(table_frame,
                                          columns=("productID", "Unsold",
                                                   "Sold"),
                                          xscrollcommand=scroll_x.set,
                                          yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.product_table.xview)
        scroll_y.config(command=self.product_table.yview)
        self.product_table.heading("productID", text="ProductID")
        self.product_table.heading("Unsold", text="Unsold")
        self.product_table.heading("Sold", text="Sold")
        self.product_table['show'] = 'headings'
        self.product_table.column("productID", width=200)
        self.product_table.column("Unsold", width=200)
        self.product_table.column("Sold", width=200)
        self.product_table.pack(fill=BOTH, expand=1)

        self.product_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    def add_products(self):
        con = mysql.connector.connect(host="localhost", user="root", password="s63127734", database="oshes")
        cur = con.cursor()
        cur.execute("insert into Product values(%s,%s,%s,%s,%s,%s)",
                    (self.id_var.get(),
                     self.model_var.get(),
                     self.category_var.get(),
                     self.price_var.get(),
                     self.cost_var.get(),
                     self.warranty_var.get()))
        #  self.inventory_var.get()
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()

    def fetch_data(self):
        con = mysql.connector.connect(host="localhost", user="root", password="s63127734", database="oshes")
        cur = con.cursor()
        cur.execute("select * from Product")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.product_table.delete(*self.product_table.get_children())
            for rows in rows:
                self.product_table.insert('', END, values=rows)
            con.commit()
        con.close()

    def clear(self):
        self.id_var.set("")
        self.cost_var.set("")
        self.price_var.set("")
        self.model_var.set("")
        self.category_var.set("")
        self.warranty_var.set("")

    def get_cursor(self, ev):
        cursor_row = self.product_table.focus()
        contents = self.product_table.item(cursor_row)
        row = contents['values']
        self.id_var.set(row[0])
        self.model_var.set(row[1])
        self.category_var.set(row[2])
        self.price_var.set(row[3])
        self.cost_var.set(row[4])
        self.warranty_var.set(row[5])

    def update_data(self):
        con = mysql.connector.connect(host="localhost", user="root", password="s63127734", database="oshes")
        cur = con.cursor()
        ##        cur.execute("update Product set productModel=%s, category=%s, price=%s, cost=%s, warrantyDuration=%s where productID = %s ",(
        ##            self.model_var.get(),
        ##            self.category_var.get(),
        ##            self.price_var.get(),
        ##            self.cost_var.get(),
        ##            self.warranty_var.get(),
        ##            self.id_var.get()
        ##            ))
        # ====== Can change all except Model as it is the reference ======, if change to ID cannot work. need to figure out why
        cur.execute("update Product set productID=%s, category=%s, price=%s, cost=%s, "
                    "warrantyDuration=%s where productModel = %s ", (
                        self.id_var.get(),
                        self.category_var.get(),
                        self.price_var.get(),
                        self.cost_var.get(),
                        self.warranty_var.get(),
                        self.model_var.get()
                    ))
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()

    def delete_data(self):
        con = mysql.connector.connect(host="localhost", user="root", password="s63127734", database="oshes")
        cur = con.cursor()
        cur.execute("delete from Product where productModel= %s ", (self.model_var.get(),))
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()

    def search_data(self):
        con = mysql.connector.connect(host="localhost", user="root", password="s63127734", database="oshes")
        cur = con.cursor()
        cur.execute(
            "select * from Product where " + str(self.search_by.get()) + " LIKE '%" + str(self.search_txt.get()) + "%'")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.product_table.delete(*self.product_table.get_children())
            for rows in rows:
                self.product_table.insert('', END, values=rows)
            con.commit()
        con.close()


if __name__ == "__main__":
    root = Tk()
    main = AdminDB(root)
    root.mainloop()
