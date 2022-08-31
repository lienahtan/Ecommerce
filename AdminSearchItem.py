from tkinter import *
from tkinter import ttk, messagebox
# noinspection PyUnresolvedReferences
# from PIL import Image
import pymongo
from pymongo import MongoClient

# client = MongoClient()
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["OSHES"]
collection = db["items"]
#root = Tk()


class AdminSearchItem:

    def __init__(self, root):

        self.root = root
        self.root.title("Admin Search Item System (OSHES)")
        self.root.geometry("1280x700+200+70")
        self.root.resizable(False, False)
        self.root.config(bg="ghost white")

        # Background is black
        self.frame1 = Frame(self.root, bg="medium violet red")
        self.frame1.place(x=250, y=50, height=800, width=700)

        # Search Frame is Blue
        self.frame = Frame(self.root, bg="light blue")
        self.frame.place(x=350, y=80, height=150, width=500)

        # Label and Boxes in Search Frame
        self.title = Label(self.frame, text="Admin Search Item System", font=("Calibri", 20, 'bold', "underline"),
                           bg="light blue")
        self.title.place(x=100, y=10)

        self.itemIDLabel = Label(self.frame, text="ITEM ID:", font=("Calibri", 15, 'bold'), fg="#00B0F0", bg="light blue")
        self.itemIDLabel.place(x=210, y=45)

        self.entry1 = Entry(self.frame, font=("times new roman", 15, 'bold'))
        self.entry1.place(x=130, y=70, width=250)

        self.searchButton = Button(self.frame, text="Search", activebackground="#00B0F0",
                                  activeforeground="#00B0F0", fg="#00B0F0",
                                  bg="crimson", font=("Calibre", 15, 'bold'), command=self.admin_search_item)

        self.searchButton.place(x=170, y=105, width=150)

        # ====== Table Frame ========

        table_frame = Frame(self.frame1, bd=0, relief=RIDGE, bg="crimson")
        table_frame.place(x=0, y=200, width=700, height=450)

        scroll_x = Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(table_frame, orient=VERTICAL)
        self.item_table = ttk.Treeview(table_frame,
                                       columns=("ItemID",
                                                "Category", "Color",
                                                "PowerSupply", "Factory",
                                                "ProductionYear", "PurchaseStatus", "Model", "ServiceStatus"),
                                       xscrollcommand=scroll_x.set,
                                       yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.item_table.xview)
        scroll_y.config(command=self.item_table.yview)
        self.item_table.heading("ItemID", text="ItemID")

        self.item_table.heading("Category", text="Category")
        self.item_table.heading("Color", text="Color")
        self.item_table.heading("PowerSupply", text="PowerSupply")
        self.item_table.heading("Factory", text="Factory")
        self.item_table.heading("ProductionYear", text="ProductionYear")
        self.item_table.heading("PurchaseStatus", text="PurchaseStatus")
        self.item_table.heading("Model", text="Model")
        self.item_table.heading("ServiceStatus", text="ServiceStatus")
        #       self.product_table.heading("inventory", text="Inventory Level")
        self.item_table['show'] = 'headings'
        self.item_table.column("ItemID", width=100, anchor=S)

        self.item_table.column("Category", width=100, anchor=S)
        self.item_table.column("Color", width=100, anchor=S)
        self.item_table.column("PowerSupply", width=100, anchor=S)
        self.item_table.column("Factory", width=100, anchor=S)
        self.item_table.column("ProductionYear", width=100, anchor=S)
        self.item_table.column("PurchaseStatus", width=100, anchor=S)
        self.item_table.column("ServiceStatus", width=100, anchor=S)
        self.item_table.column("Model", width=100, anchor=S)
        self.item_table.pack(fill=BOTH, expand=1)

    def admin_search_item(self):
        if (self.entry1.get() == ""):
            messagebox.showerror("Error", "Please enter an item ID!", parent=self.root)
        else:
            try:
                cursor = collection.find({"ItemID": self.entry1.get()})
                if cursor.count() != 0:
                    for index, data in enumerate(cursor):
                        self.item_table.insert('', END, values=(data['ItemID'],
                                                                data['Category'],data['Color'],
                                                                data['PowerSupply'], data['Factory'],
                                                                data['ProductionYear'], data['PurchaseStatus'], data['Model'],
                                                                data['ServiceStatus']))
                    self.item_table.pack()
                else:
                    messagebox.showerror("Error", "No Item Found!", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Error due to: {str(es)}",parent=self.root)

    # Forget Password: https://www.youtube.com/watch?v=2xzzLoDV0XY&list=PL4P8sY6zvjk6p9u8T2etiQm6EE_15QF0y&index=6&ab_channel=Webcode



if __name__ =="__main__":
    root=Tk()
    main = AdminSearchItem(root)
    root.mainloop()

