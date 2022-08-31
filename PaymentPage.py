from tkinter import *
from tkinter import messagebox
import mysql.connector
from datetime import date
from datetime import datetime

class Payment_Page:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1320x700+0+0")
        self.root.title("Billing Software")
        self.root.resizable(False, False)
        bg_color = "white"
        title = Label(self.root, text="REQUEST SUBMISSION & PAYMENT", bd=15, bg="black", fg="white",
                      font=("times new roman", 30, "bold"), pady=2).pack(fill=X)

        self.cardname = StringVar()
        self.cardnumber = StringVar()
        self.carddate = StringVar()
        self.cvv = StringVar()
        self.paymentID = StringVar()
        self.customerID = StringVar()
        self.amtPayable = IntVar()
        self.customerID = StringVar()
        self.todayDate = date.today()
        self.administratorID = StringVar()
        self.itemID = StringVar()
        self.requestID = StringVar(0)
        self.materialFee = IntVar()

        f = open("store_custanditemID", "r")
        print(f)
        profile_details = []
        for line in f:
            profile_details.append(line.rstrip())
        self.itemID.set(profile_details[0])
        self.customerID.set(profile_details[1])
        self.administratorID.set(profile_details[2])
        self.amtPayable.set(profile_details[3])
        self.requestID.set(profile_details[4])
        self.materialFee.set(profile_details[5])


        self.paymentID.set("Payment"+self.itemID.get()) #have to update system ( updated below )

        F1 = Frame(self.root, bd=8, relief=GROOVE, bg= "white")
        F1.place(x=0, y=80, width=1320, height=550)


        cname_lbl = Label(F1, text="Card Details", bg="white", fg="black", font=("times new roman", 40, "bold")).place(x=500, y=80)

        cardname = Label(F1, text="Name on card:", bg="white", fg="black",
                      font=("times new roman", 15, "bold")).place(x=350, y=160)
        cardnamentry = Entry(F1, textvariable=self.cardname, font="arial 12", bd=7, relief=SUNKEN).place(x=550, y=160)

        cardnumber = Label(F1, text="Card Number:", bg="white", fg="black",
                           font=("times new roman", 15, "bold")).place(x=350, y=200)
        cardnumberentry = Entry(F1, textvariable=self.cardnumber, font="arial 12", bd=7, relief=SUNKEN).place(x=550, y=200)

        carddate = Label(F1, text="Date (MM/YY):", bg="white", fg="black",
                           font=("times new roman", 15, "bold")).place(x=350, y=240)
        carddateentry = Entry(F1, textvariable=self.carddate, font="arial 12", bd=7, relief=SUNKEN).place(x=550, y=240)

        cardcvv = Label(F1, text="CVV:", bg="white", fg="black",
                         font=("times new roman", 15, "bold")).place(x=350, y=280)
        cardcvv = Entry(F1, textvariable=self.cvv, font="arial 12", bd=7, relief=SUNKEN).place(x=550, y=280)

        confirmpayment = Button(F1, text="Confirm Payment and Exit", command=self.cfmpayment, bg="cadetblue", fg="white", pady=15, bd=4,
                          width=5, font="arial 14 bold").place(x=500, y=330, width=300, height=50)

        Exit_btn = Button(F1, text="Exit", command=self.Exit_app, bg="cadetblue", fg="white", pady=15, bd=4,
                          width=5, font="arial 14 bold").place(x=1200, y=430)

        F2 = Frame(self.root, bd=8, relief=GROOVE, bg="white")
        F2.place(x=0, y=630, width=1320, height=70)

        cardcvv = Label(F2, text="Thank you!", bg="white", fg="black",
                        font=("times new roman", 15, "bold")).place(x=600, y=10)


    def cfmpayment(self):
        con = mysql.connector.connect(host="localhost", user="root", password="s63127734", database="oshes")
        cur = con.cursor()

        cur.execute("UPDATE request SET requestStatus = 'In progress' WHERE requestID = %s",
                    (self.requestID.get(),))
        row = cur.fetchone()

        cur.execute("INSERT INTO payment VALUES (%s, %s, %s, %s)",
                    (self.paymentID.get(),  str(date.today()), self.amtPayable.get(), self.customerID.get()))

       # cur.execute("UPDATE servicefee SET paymentID = " + self.paymentID.get() + " WHERE requestID = %s", (self.requestID.get()))
        cur.execute("UPDATE servicefee SET paymentID = %s WHERE requestID = %s", (self.paymentID.get(), self.requestID.get()))

        cur.execute("UPDATE servicefee SET flatFee = '40', materialFee = %s WHERE requestID = %s",
                    (self.materialFee.get(), self.requestID.get()))

        op = messagebox.showinfo("Payment", "Payment completed.")


        #cur.execute("UPDATE payment SET paymentID = %s WHERE requestID = %s", (self.paymentID.get(), self.requestID.get()))


        con.commit()
        con.close()
        self.root.destroy()


    def Exit_app(self):
        self.root.destroy()

if __name__ == "__main__":
    root = Tk()
    obj = Payment_Page(root)
    root.mainloop()

