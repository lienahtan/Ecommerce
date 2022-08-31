from tkinter import *
from tkinter import ttk, messagebox
# from tkinter.ttk import *
# import tkinter.messagebox as mb
from PIL import ImageTk, Image
import mysql.connector
import datetime

class AutomaticCancel:

    def __init__(self, root):

        self.root = root
        self.root.title("Automatic Cancel")
        self.root.geometry("500x500+0+0")
        self.root.resizable(False, False)

        title = Label(self.root, text="Automatic cancel", font=("calibri", 40, "bold"), bg="light blue", fg="white")
        title.pack(side=TOP, fill=X)

        # =====All Variables=======

        # ======Manage Frame=======
        db_frame = Frame(self.root, bd=4, relief=RIDGE, bg="crimson")
        db_frame.place(x=20, y=100, width=450, height=300)

        db_title = Label(db_frame, text="Automatic Cancel", bg="crimson", fg="white",
                         font=("calibri", 25, "bold"))
        db_title.grid(row=0, columnspan=2, pady=20)

        # ======Button Frame for Request=========
        cancelBtn = Button(db_frame, text="refresh", width=10, command=self.cancel_request)\
            .grid(row=0, column=3, padx=6, pady=10)

    def cancel_request(self):
        con = mysql.connector.connect(host="localhost", user="root", password="s63127734", database="oshes")
        cur = con.cursor()
        cur.execute("update Request as r left join ServiceFee as s on r.requestID = s.requestID "
                    "left join Payment as p on s.paymentID = p.paymentID set r.requestStatus = 'Canceled' "
                    "where p.paymentID is null and timestampdiff(day, requestDate, curdate()) > 10")
        con.commit()
        con.close()

root = Tk()
main = AutomaticCancel(root)
root.mainloop()