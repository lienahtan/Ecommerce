from tkinter import *
from tkinter import ttk, messagebox
# from tkinter.ttk import *
# import tkinter.messagebox as mb
from pymongo import MongoClient
#client = MongoClient()
client = MongoClient('localhost', 27017)
db = client["OSHES"]
itemcol = db["items"]
procol = db["product"]
collection_filter1 = db["filter1"]
collection_filter2 = db["filter2"]
collection_filter3 = db["filter3"]
collection_filter4 = db["filter4"]
collection_filter5 = db["filter5"]
collection_filter6 = db["filter6"]
collection_filter1.delete_many({})
collection_filter2.delete_many({})
collection_filter3.delete_many({})
collection_filter4.delete_many({})
collection_filter5.delete_many({})
collection_filter6.delete_many({})

#root = Tk()


class CustomerSearchProduct:

    def __init__(self, root):

        self.root = root
        self.root.title("Customer Search Product System")
        self.root.geometry("1350x700+0+0")
        self.root.resizable(False, False)
        self.root.config(bg="light blue")

        title = Label(self.root, text="Product Search System", font=("calibri", 40, "bold"), bg="light green", fg="black")
        title.pack(side=TOP, fill=X)

        # =====All Variables=======

        self.category = StringVar()
        self.productModel = StringVar()
        self.price = StringVar()
        self.color = StringVar()
        self.factory = StringVar()
        self.productionYear = StringVar()
        self.powerSupply = StringVar()

        self.search_by = StringVar()
        self.search_value = StringVar()
        self.warranty = StringVar()
        self.inventory = StringVar()

        # ======Manage Frame=======

        db_frame = Frame(self.root, bd=4, relief=RIDGE, bg="pale violet red")
        db_frame.place(x=20, y=100, width=450, height=560)

        db_title = Label(db_frame, text="Customer Search product", bg="pale violet red", fg="white", font=("Cambria", 25, "bold", "underline"))
        db_title.grid(row=0, columnspan=1, pady=20)

        # ======Manage request=========

        label_search_by = Label(db_frame, text="Search by", bg="pale violet red", fg="white", font=("calibri", 12, "bold"))
        label_search_by.grid(row=1, column=0, pady=10, padx=10, sticky="w")

        combo_search_by = ttk.Combobox(db_frame, textvariable=self.search_by, font=("calibre", 12, "bold"),
                                    state="readonly")
        combo_search_by['values'] = ("Model", "Category")
        combo_search_by.place(x=150, y=100)

        label_search_value = Label(db_frame, text="Search Value", bg="pale violet red", fg="white", font=("calibri", 12, "bold"))
        label_search_value.grid(row=2, column=0, pady=10, padx=10, sticky="w")

        txt_search_value = Entry(db_frame, bd=5, textvariable=self.search_value, relief=GROOVE, bg="white", fg="black",
                         font=("calibri", 12, "bold"))
        txt_search_value.place(x=150, y=140)

        label_filter = Label(db_frame, text="Filter (optional, default as everything)", bg="pale violet red", fg="white", font=("calibri", 16, "bold"))
        label_filter.grid(row=3, column=0, pady=10, padx=10, sticky="w")

        label_price = Label(db_frame, text="Price", bg="pale violet red", fg="white", font=("calibri", 12, "bold"))
        label_price.grid(row=4, column=0, pady=10, padx=10, sticky="w")

        combo_price = ttk.Combobox(db_frame, textvariable=self.price, font=("calibri", 12, "bold"),
                                    state="readonly")
        combo_price['values'] = ("", "50", "60", "70", "100", "120", "125", "200")
        combo_price.place(x=150, y=240)

        label_color = Label(db_frame, text="Color", bg="pale violet red", fg="white", font=("calibri", 12, "bold"))
        label_color.grid(row=5, column=0, pady=10, padx=10, sticky="w")

        combo_color = ttk.Combobox(db_frame, textvariable=self.color, font=("calibri", 12, "bold"),
                                   state="readonly")
        combo_color['values'] = ("", "White", "Black", "Blue", "Yellow", "Green")
        combo_color.place(x=150, y=280)

        label_factory = Label(db_frame, text="Factory", bg="pale violet red", fg="white", font=("calibri", 12, "bold"))
        label_factory.grid(row=6, column=0, pady=10, padx=10, sticky="w")

        combo_factory = ttk.Combobox(db_frame, textvariable=self.factory, font=("calibri", 12, "bold"),
                                   state="readonly")
        combo_factory['values'] = ("", "China", "Malaysia", "Philippines")
        combo_factory.place(x=150, y=320)

        label_productionYear = Label(db_frame, text="Production Year", bg="pale violet red", fg="white", font=("calibri", 12, "bold"))
        label_productionYear.grid(row=7, column=0, pady=10, padx=10, sticky="w")

        combo_productionYear = ttk.Combobox(db_frame, textvariable=self.productionYear, font=("calibri", 12, "bold"),
                                     state="readonly")
        combo_productionYear['values'] = ("", "2014", "2015", "2016", "2017", "2018", "2019", "2020")
        combo_productionYear.place(x=150, y=370)

        label_powerSupply = Label(db_frame, text="Power Supply", bg="pale violet red", fg="white",
                                     font=("calibri", 12, "bold"))
        label_powerSupply.grid(row=8, column=0, pady=10, padx=10, sticky="w")

        combo_powerSupply = ttk.Combobox(db_frame, textvariable=self.powerSupply,
                                            font=("calibri", 12, "bold"),
                                            state="readonly")
        combo_powerSupply['values'] = ("", "Battery", "USB")
        combo_powerSupply.place(x=150, y=420)



        # ======Button Frame for Search=========
        reqbutton = Frame(db_frame, bd=4, relief=RIDGE, bg="pale violet red")
        reqbutton.place(x=15, y=500, width=420)

        button_search = Button(reqbutton, text="Search", width=20, command=self.customer_search_product)
        button_search.grid(row=0, column=1, padx=130, pady=10)

        # ======Detail Frame=======

        self.detail_frame = Frame(self.root, bd=4, relief=RIDGE, bg="pale violet red")
        self.detail_frame.place(x=500, y=100, width=800, height=560)

        lable_productResult = Label(self.detail_frame, text="Product Search Result", bg="pale violet red", fg="white", font=("calibri", 20, "bold"))
        lable_productResult.grid(row=0, column=0, pady=20, padx=7, sticky="w")

        # ====== Table Frame ========

        table_frame = Frame(self.detail_frame, bd=4, relief=RIDGE, bg="pale violet red")
        table_frame.place(x=10, y=70, width=760, height=480)

        scroll_x = Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(table_frame, orient=VERTICAL)
        self.product_table = ttk.Treeview(table_frame,
                                          columns=("Category", "Product Model",
                                                   "Price ($)", "Warranty (months)", "Inventory"),
                                          xscrollcommand=scroll_x.set,
                                          yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.product_table.xview)
        scroll_y.config(command=self.product_table.yview)
        self.product_table.heading("Category", text="Category")
        self.product_table.heading("Product Model", text="Product Model")
        self.product_table.heading("Price ($)", text="Price ($)")
        self.product_table.heading("Warranty (months)", text="Warranty (months)")
        self.product_table.heading("Inventory", text="Inventory")


        self.product_table['show'] = 'headings'
        self.product_table.column("Category", width=100)
        self.product_table.column("Product Model", width=100)
        self.product_table.column("Price ($)", width=100)
        self.product_table.column("Warranty (months)", width=100)
        self.product_table.column("Inventory", width=100)
        self.product_table.pack(fill=BOTH, expand=1)

    def customer_search_product(self):

        attribute = str(self.search_by.get())
        value = str(self.search_value.get())
        price = str(self.price.get())
        color = str(self.color.get())
        factory = str(self.factory.get())
        productionYear = str(self.productionYear.get())
        powerSupply = str(self.powerSupply.get())

        self.product_table.delete(*self.product_table.get_children())

        if attribute == "":
            messagebox.showerror("Error", "Please choose product category or product model for searching!",
                                parent=self.root)
        elif value == "":
            messagebox.showerror("Error", "Please enter a product category or a product model", parent=self.root)
        else:
            try:
                cursorList = list(procol.find({attribute: value}))
                if len(cursorList) != 0:
                    num_emptyProduct = 0
                    for x in cursorList:
                        filter1List = list(itemcol.find({'$and':[{'Category': x['Category']}, {'Model': x['Model']}, {'PurchaseStatus': 'Unsold'}]}))
                        collection_filter1.insert_many(filter1List)
                        print(filter1List)

                        if price == '':
                            collection_filter2 = db["filter2"]
                            if len(filter1List) != 0:
                                collection_filter2.insert_many(filter1List)
                            filter2List = list(collection_filter2.find())
                        elif price != str(x['Price']):
                            collection_filter2 = db["filter2"]
                            filter2List = list(collection_filter2.find())
                        else:
                            collection_filter2 = db["filter2"]
                            if len(filter1List) != 0:
                                collection_filter2.insert_many(filter1List)
                            filter2List = list(collection_filter2.find())

                        if color == '':
                            collection_filter3 = db["filter3"]
                            if len(filter2List) != 0:
                                collection_filter3.insert_many(filter2List)
                            filter3List = filter2List
                        else:
                            filter3List = list(collection_filter2.find({'Color': color}))
                            collection_filter3 = db["filter3"]
                            if len(filter3List) != 0:
                                collection_filter3.insert_many(filter3List)

                        if factory == '':
                            collection_filter4 = db["filter4"]
                            if len(filter3List) != 0:
                                collection_filter4.insert_many(filter3List)
                            filter4List = filter3List
                        else:
                            filter4List = list(collection_filter3.find({'Factory': factory}))
                            collection_filter4 = db["filter4"]
                            if len(filter4List) != 0:
                                collection_filter4.insert_many(filter4List)

                        if productionYear == '':
                            collection_filter5 = db["filter5"]
                            if len(filter4List) != 0:
                                collection_filter5.insert_many(filter4List)
                            filter5List = filter4List
                        else:
                            filter5List = list(collection_filter4.find({'ProductionYear': productionYear}))
                            collection_filter5 = db["filter5"]
                            if len(filter5List) != 0:
                                collection_filter5.insert_many(filter5List)

                        if powerSupply == '':
                            collection_filter6 = db["filter6"]
                            if len(filter5List) != 0:
                                collection_filter6.insert_many(filter5List)
                            filter6List = filter5List
                        else:
                            filter6List = list(collection_filter5.find({'PowerSupply': powerSupply}))
                            collection_filter6 = db["filter6"]
                            if len(filter6List) != 0:
                                collection_filter6.insert_many(filter6List)

                        count = len(filter6List)
                        if count != 0:
                            self.product_table.insert('', END, values=(x['Category'], x['Model'],
                                                                x['Price'], x['Warranty'], count))
                        else:
                            num_emptyProduct = num_emptyProduct + 1
                        collection_filter1.delete_many({})
                        collection_filter2.delete_many({})
                        collection_filter3.delete_many({})
                        collection_filter4.delete_many({})
                        collection_filter5.delete_many({})
                        collection_filter6.delete_many({})
                    self.product_table.pack()
                    if num_emptyProduct == len(cursorList):
                        searchResult = "There is no product that satisfies your filter. Try to select another filter"
                        lable_searchResult = Label(self.detail_frame, text=str(searchResult), bg="pale violet red",
                                                   fg="white",
                                                   font=("calibri", 13, "bold"))
                        lable_searchResult.grid(row=0, column=1, pady=20, padx=7, sticky="w")
                    else:
                        searchResult = "The product that satisfies your filtering is as follows"
                        lable_searchResult = Label(self.detail_frame, text=str(searchResult), bg="pale violet red",
                                                   fg="white",
                                                   font=("calibri", 13, "bold"))
                        lable_searchResult.grid(row=0, column=1, pady=20, padx=7, sticky="w")
                else:
                    searchResult = "There is no product that satisfies your filter. Try to select another filter"
                    lable_searchResult = Label(self.detail_frame, text=str(searchResult), bg="pale violet red",
                                                    fg="white",
                                                    font=("calibri", 13, "bold"))
                    lable_searchResult.grid(row=0, column=1, pady=20, padx=7, sticky="w")
            except Exception as es:
                messagebox.showerror("Error", f"Error due to: {str(es)}", parent=self.root)

if __name__ =="__main__":
    root=Tk()
    main = CustomerSearchProduct(root)
    root.mainloop()