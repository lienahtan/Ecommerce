from tkinter import *
import math, random, os
from tkinter import ttk, messagebox
import tkinter.ttk
import mysql.connector
from datetime import datetime, date, timedelta

class Bill_App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1320x700+0+0")
        self.root.title("Billing Software")
        self.root.resizable(False, False)
        bg_color = "black"
        title = Label(self.root, text="PURCHASE PAYMENT  ", bd=15, bg="black", fg="white",
                      font=("times new roman", 30, "bold"), pady=2).pack(fill=X)
        # ================Variables==========================
        # ================Cosemetics==========================

        self.soap = IntVar()
        self.light1 = IntVar()
        self.light2 = IntVar()
        self.LightSmart = IntVar()
        self.Safe1 = IntVar()
        self.Safe2 = IntVar()
        self.Safe3 = IntVar()
        self.safesmart = IntVar()

        colorOpt = ["White", "Blue", "Yellow", "Green", "Black"]
        self.l_color1 = StringVar()
        self.l_color1.set(colorOpt[0])
        self.l_color2 = StringVar()
        self.l_color2.set(colorOpt[0])
        self.l_color3 = StringVar()
        self.l_color3.set(colorOpt[0])

        colorOpt1 = ["White", "Black"]
        self.l_safe1 = StringVar()
        self.l_safe1.set(colorOpt1[0])
        self.l_safe2 = StringVar()
        self.l_safe2.set(colorOpt1[0])
        self.l_safe3 = StringVar()
        self.l_safe3.set(colorOpt1[0])
        self.l_safe4 = StringVar()
        self.l_safe4.set(colorOpt1[0])


        # ================Total Product Price variables==========================

        self.total_light_price = StringVar()
        self.total_safe_price = StringVar()

        # ================Cutomers==================================

        self.customerID = StringVar()
        self.c_name = StringVar()
        self.c_phon = StringVar()
        self.bill_no = StringVar()
        self.search_bill = StringVar()
        self.address = StringVar()

        f = open("store_custID.txt", "r")
        profile_details = []
        for line in f:
            profile_details.append(line.rstrip())

        self.customerID.set(profile_details[0])
        self.c_name.set(profile_details[1])
        self.c_phon.set(profile_details[4])
        self.address.set(profile_details[5])

        # =============Customer Details Frame
        F1 = LabelFrame(self.root, bd=8, text="Your Details", font=("times new roman", 25, "bold"), fg="white",
                        bg=bg_color)
        F1.place(x=0, y=80, relwidth=1)

        statusOpt = ["Unsold"]
        self.purchaseStatus = StringVar()
        self.purchaseStatus.set(statusOpt[0])
        status_P = OptionMenu(F1, self.purchaseStatus, *statusOpt).place(x=1000, y=1000)

        soldOpt = ["Sold"]
        self.soldStatus = StringVar()
        self.soldStatus.set(soldOpt[0])
        status_S = OptionMenu(F1, self.soldStatus, *soldOpt).place(x=1500, y=1500)

        light1Opt = ["001"]
        self.light1Status = StringVar()
        self.light1Status.set(light1Opt[0])
        status_001 = OptionMenu(F1, self.light1Status, *light1Opt).place(x=1500, y=1500)

        light2Opt = ["002"]
        self.light2Status = StringVar()
        self.light2Status.set(light2Opt[0])
        status_002 = OptionMenu(F1, self.light2Status, *light2Opt).place(x=1500, y=1500)

        light3Opt = ["003"]
        self.light3Status = StringVar()
        self.light3Status.set(light3Opt[0])
        status_003 = OptionMenu(F1, self.light3Status, *light3Opt).place(x=1500, y=1500)

        safe1Opt = ["004"]
        self.safe1Status = StringVar()
        self.safe1Status.set(safe1Opt[0])
        status_004 = OptionMenu(F1, self.safe1Status, *safe1Opt).place(x=1500, y=1500)

        safe2Opt = ["005"]
        self.safe2Status = StringVar()
        self.safe2Status.set(safe2Opt[0])
        status_005 = OptionMenu(F1, self.safe2Status, *safe2Opt).place(x=1500, y=1500)

        safe3Opt = ["006"]
        self.safe3Status = StringVar()
        self.safe3Status.set(safe3Opt[0])
        status_006 = OptionMenu(F1, self.safe3Status, *safe3Opt).place(x=1500, y=1500)

        safe4Opt = ["007"]
        self.safe4Status = StringVar()
        self.safe4Status.set(safe4Opt[0])
        status_007 = OptionMenu(F1, self.safe4Status, *safe4Opt).place(x=1500, y=1500)

        cname_lbl = Label(F1, text="ID", bg=bg_color, fg="White", font=("times new roman", 15, "bold")).grid(
            row=0, column=0, padx=0, pady=0)
        cname_txt = Entry(F1, width=15, textvariable=self.customerID, font="arial 12", bd=7, relief=SUNKEN, state="readonly").grid(row=0,
                                                                                                                                   column=1,
                                                                                                                                   pady=0,
                                                                                                                                   padx=3)

        cphn_lbl = Label(F1, text="Name", bg=bg_color, fg="White", font=("times new roman", 15, "bold")).grid(
            row=0, column=2, padx=0, pady=5)
        cphn_txt = Entry(F1, width=15, textvariable=self.c_name, font="arial 12", bd=7, relief=SUNKEN, state="readonly").grid(row=0,
                                                                                                                              column=3,
                                                                                                                              pady=5,
                                                                                                                              padx=3)

        c_bill_lbl = Label(F1, text="Contact No", bg=bg_color, fg="White", font=("times new roman", 15, "bold")).grid(
            row=0, column=4, padx=0, pady=5)
        c_bill_txt = Entry(F1, width=15, textvariable=self.c_phon, font="arial 12", bd=7, relief=SUNKEN, state="readonly").grid(
            row=0, column=5, pady=5, padx=3)


        c_bill_lbl = Label(F1, text="Address", bg=bg_color, fg="White", font=("times new roman", 15, "bold")).grid(
            row=0, column=6, padx=0, pady=5)
        c_bill_txt = Entry(F1, width=25, textvariable=self.address, font="arial 12", bd=7, relief=SUNKEN, state="readonly").grid(
            row=0, column=7, pady=5, padx=10)

        #bill_btn = Button(F1, text="Search", command=self.find_bill, width=10, bd=7, font="arial 12").grid(row=0,column=8,padx=6,pady=3)

        # ===========LIGHT CATEGORY=========
        bg_color2 = "white"

        F2 = LabelFrame(self.root, bd=20, text="Items Bought", font=("times new roman", 25, "bold"), fg="black", bg="white")
        F2.place(x=5, y=180, width=500, height=380)

        bath_lbl = Label(F2, text="Lights \n"
                                  "Category", font=("times new roman", 13, "bold"), bg="WHITE", fg="red").place(x=10, y=10)

        bath_lbl = Label(F2, text="Qty", font=("times new roman", 13, "bold"), bg="WHITE", fg="red").place(x=120, y=10)

        bath_lbl = Label(F2, text="Color", font=("times new roman", 13, "bold"), bg=bg_color2, fg="red").place(x=190, y=10)

        bath_lbl = Label(F2, text="Power \n"
                                  "Source", font=("times new roman", 13, "bold"), bg=bg_color2, fg="red").place(x=290, y=10)

        bath_lbl = Label(F2, text="Price per \n "
                                  "Unit ($)", font=("times new roman", 13, "bold"), bg=bg_color2, fg="red").place(x=360, y=10)

        #        tkinter.ttk.Separator(F2, orient=VERTICAL).place(x=180, y=10, width=2, height=300)
        #           tkinter.ttk.Separator(F2, orient=HORIZONTAL).place(x=0, y=50, width=460, height=2)

        #All the lights StringVar for models, colors and locks
        self.lbl_light1 = StringVar()
        self.lbl_light1.set("Light1")
        self.lbl_light2 = StringVar()
        self.lbl_light2.set("Light2")
        self.lbl_light3 = StringVar()
        self.lbl_light3.set("SmartHome1")
        self.powlight1 = StringVar()
        self.powlight2 = StringVar()
        self.powlight3 = StringVar()






        light1_lbl = Label(F2, text="Light1", font=("times new roman", 12, "bold"), bg=bg_color2,
                           fg=bg_color, textvariable = self.lbl_light1).place(x=10, y=70)
        light1_entry = Entry(F2, width=10, textvariable=self.light1, font=("times new roman", 14, "bold"), bd=5,
                             relief=SUNKEN).place(x=120, y=70, width=40, height=40)
        light1_txt = Label(F2, width=10, text="50", font=("times new roman", 14, "bold"), bd=5,
                           relief=SUNKEN).place(x=380, y=70, width=60, height=40)
        light1_color = OptionMenu(F2, self.l_color1, *colorOpt).place(x=190, y=70)
        light1_power = ttk.Combobox(F2, font=("calibri", 10), state='readonly', justify=CENTER, textvariable=self.powlight1)
        light1_power.place(x=290, y=75, width=60)
        light1_power['values'] = ("USB", "Battery")
        light1_power.current(0)




        light2_lbl = Label(F2, text="Light2", font=("times new roman", 12, "bold"), bg=bg_color2,
                           fg=bg_color, textvariable = self.lbl_light2).place(x=10, y=140)
        light2_entry = Entry(F2, width=10, textvariable=self.light2, font=("times new roman", 14, "bold"), bd=5,
                             relief=SUNKEN).place(x=120, y=140, width=40, height=40)
        light2_txt = Label(F2, width=10, text="60", font=("times new roman", 14, "bold"), bd=5,
                           relief=SUNKEN).place(x=380, y=140, width=60, height=40)
        light2_color = OptionMenu(F2, self.l_color2, *colorOpt).place(x=190, y=140)
        light2_power = ttk.Combobox(F2, font=("calibri", 10), state='readonly', justify=CENTER, textvariable=self.powlight2)
        light2_power.place(x=290, y=145, width=60)
        light2_power['values'] = ("USB", "Battery")
        light2_power.current(0)




        lightsmart_lbl = Label(F2, text="SmartHome1", font=("times new roman", 12, "bold"), bg=bg_color2,
                               fg=bg_color, textvariable = self.lbl_light3).place(x=10, y=210)
        lightsmart_entry = Entry(F2, width=10, textvariable=self.LightSmart, font=("times new roman", 14, "bold"), bd=5,
                                 relief=SUNKEN).place(x=120, y=210, width=40, height=40)
        lightsmart_txt = Label(F2, width=10, text="70", font=("times new roman", 14, "bold"), bd=5,
                               relief=SUNKEN).place(x=380, y=210, width=60, height=40)
        light3_color = OptionMenu(F2, self.l_color3, *colorOpt).place(x=190, y=210)
        light3_power = ttk.Combobox(F2, font=("calibri", 10), state='readonly', justify=CENTER, textvariable=self.powlight3)
        light3_power.place(x=290, y=215, width=60)
        light3_power['values'] = ("USB", "Battery")
        light3_power.current(0)



        # ============SAFE CATEGORY=========
        bg_color2 = "white"

        F2 = LabelFrame(self.root, bd=20, text="Items Bought", font=("times new roman", 25, "bold"), fg="black", bg="white")
        F2.place(x=480, y=180, width=500, height=380)

        bath_lbl = Label(F2, text="Safe \n"
                                  "Category", font=("times new roman", 13, "bold"), bg="WHITE", fg="red").place(x=10, y=10)

        bath_lbl = Label(F2, text="Qty", font=("times new roman", 13, "bold"), bg="WHITE", fg="red").place(x=120, y=10)

        bath_lbl = Label(F2, text="Color", font=("times new roman", 13, "bold"), bg=bg_color2, fg="red").place(x=190,
                                                                                                               y=10)

        bath_lbl = Label(F2, text="Power \n"
                                  "Source", font=("times new roman", 13, "bold"), bg=bg_color2, fg="red").place(x=290,
                                                                                                                y=10)

        bath_lbl = Label(F2, text="Price per \n "
                                  "Unit ($)", font=("times new roman", 13, "bold"), bg=bg_color2, fg="red").place(x=360,
                                                                                                                  y=10)

        #        tkinter.ttk.Separator(F2, orient=VERTICAL).place(x=170, y=10, width=2, height=300)
        #        tkinter.ttk.Separator(F2, orient=HORIZONTAL).place(x=0, y=50, width=460, height=2)

        self.lbl_safe1 = StringVar()
        self.lbl_safe1.set("Safe1")
        self.lbl_safe2 = StringVar()
        self.lbl_safe2.set("Safe2")
        self.lbl_safe3 = StringVar()
        self.lbl_safe3.set("Safe3")
        self.lbl_safe4 = StringVar()
        self.lbl_safe4.set("SmartHome1")
        self.powsafe1 = StringVar()
        self.powsafe2 = StringVar()
        self.powsafe3 = StringVar()
        self.powsafe4 = StringVar()

        self.light001 = StringVar()
        self.light001.set("4")

      #  light001 = Label(F2, text="1", textvariable=self.light001).place(x=2000, y=2000)

        safe1_lbl = Label(F2, text="Safe1", font=("times new roman", 12, "bold"), bg=bg_color2,
                          fg=bg_color).place(x=10, y=70)
        safe1_entry = Entry(F2, width=10, textvariable=self.Safe1, font=("times new roman", 14, "bold"), bd=5,
                            relief=SUNKEN).place(x=120, y=70, width=40, height=40)
        safe1_txt = Label(F2, width=10, text="100", font=("times new roman", 14, "bold"), bd=5,
                          relief=SUNKEN).place(x=380, y=70, width=60, height=40)
        safe1_color = OptionMenu(F2, self.l_safe1, *colorOpt1).place(x=190, y=70)
        safe1_power = ttk.Combobox(F2, font=("calibri", 10), state='readonly', justify=CENTER, textvariable=self.powsafe1)
        safe1_power.place(x=290, y=75, width=60)
        safe1_power['values'] = "Battery"
        safe1_power.current(0)

        safe2_lbl = Label(F2, text="Safe2", font=("times new roman", 12, "bold"), bg=bg_color2,
                          fg=bg_color).place(x=10, y=140)
        safe2_entry = Entry(F2, width=10, textvariable=self.Safe2, font=("times new roman", 14, "bold"), bd=5,
                            relief=SUNKEN).place(x=120, y=140, width=40, height=40)
        safe2_txt = Label(F2, width=10, text="120", font=("times new roman", 14, "bold"), bd=5,
                          relief=SUNKEN).place(x=380, y=140, width=60, height=40)
        safe2_color = OptionMenu(F2, self.l_safe2, *colorOpt1).place(x=190, y=140)
        safe2_power = ttk.Combobox(F2, font=("calibri", 10), state='readonly', justify=CENTER, textvariable=self.powsafe2)
        safe2_power.place(x=290, y=145, width=60)
        safe2_power['values'] = "Battery"
        safe2_power.current(0)

        safe3_lbl = Label(F2, text="Safe3", font=("times new roman", 12, "bold"), bg=bg_color2,
                          fg=bg_color).place(x=10, y=210)
        safe3_entry = Entry(F2, width=10, textvariable=self.Safe3, font=("times new roman", 14, "bold"), bd=5,
                            relief=SUNKEN).place(x=120, y=210, width=40, height=40)
        safe3_txt = Label(F2, width=10, text="125", font=("times new roman", 14, "bold"), bd=5,
                          relief=SUNKEN).place(x=380, y=210, width=60, height=40)
        safe3_color = OptionMenu(F2, self.l_safe3, *colorOpt1).place(x=190, y=210)
        safe3_power = ttk.Combobox(F2, font=("calibri", 10), state='readonly', justify=CENTER, textvariable=self.powsafe3)
        safe3_power.place(x=290, y=215, width=60)
        safe3_power['values'] = "Battery"
        safe3_power.current(0)

        safe4_lbl = Label(F2, text="SmartHome1", font=("times new roman", 12, "bold"), bg=bg_color2,
                          fg=bg_color).place(x=10, y=280)
        safe4_entry = Entry(F2, width=10, textvariable=self.safesmart, font=("times new roman", 14, "bold"), bd=5,
                            relief=SUNKEN).place(x=120, y=280, width=40, height=40)
        safe4_txt = Label(F2, width=10, text="200", font=("times new roman", 14, "bold"), bd=5,
                          relief=SUNKEN).place(x=380, y=280, width=60, height=40)
        safe4_color = OptionMenu(F2, self.l_safe4, *colorOpt1).place(x=190, y=280)
        safe4_power = ttk.Combobox(F2, font=("calibri", 10), state='readonly', justify=CENTER, textvariable=self.powsafe4)
        safe4_power.place(x=290, y=285, width=60)
        safe4_power['values'] = "Battery"
        safe4_power.current(0)

        # ===============Bill Area=============
        F5 = Frame(self.root, bd=8, relief=GROOVE)
        F5.place(x=980, y=180, width=340, height=380)

        bill_title = Label(F5, text="YOUR BILL", font="arial 15 bold", bd=7, relief=GROOVE).pack(fill=X)
        scrol_y = Scrollbar(F5, orient=VERTICAL)
        self.txtarea = Text(F5, yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT, fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH, expand=1)

        # ==============Button Frame=============

        F6 = LabelFrame(self.root, bd=8, text="BILL MENU", font=("times new roman", 20, "bold"), fg="black", bg="white")
        F6.place(x=0, y=560, relwidth=1, height=140)
        m1_lbl = Label(F6, text="Total Light Price", bg="white", fg="black",
                       font=("times new roman", 15, "bold")).grid(row=0, column=0, padx=20, pady=1, sticky="w")
        m1_txt = Entry(F6, width=18, textvariable=self.total_light_price, font="arial 10 bold", bd=7, relief=SUNKEN, state="readonly").grid(
            row=0, column=1, padx=10, pady=1)

        m2_lbl = Label(F6, text="Total Safe Price", bg="white", fg="black",
                       font=("times new roman", 15, "bold")).grid(row=0, column=3, padx=20, pady=1, sticky="w")
        m2_txt = Entry(F6, width=18, textvariable=self.total_safe_price, font="arial 10 bold", bd=7, relief=SUNKEN, state="readonly").grid(
            row=0, column=4, padx=10, pady=1)


        btn_F = Frame(F6, bd=7, relief=GROOVE)
        btn_F.place(x=720, width=590, height=102)

        total_btn = Button(btn_F, text="Total", command=self.total, bg="cadetblue", fg="white", pady=15, bd=4, width=10,
                           font="arial 14 bold").grid(row=0, column=0, padx=5, pady=5)
        GBill_btn = Button(btn_F, text="Generate Bill", command=self.bill_area, bg="cadetblue", fg="white", pady=15,
                           bd=4, width=10, font="arial 14 bold").grid(row=0, column=1, padx=5, pady=5)
        Clear_btn = Button(btn_F, text="Clear", command=self.clear_data, bg="cadetblue", fg="white", pady=15, bd=4,
                           width=10, font="arial 14 bold").grid(row=0, column=2, padx=5, pady=5)
        Exit_btn = Button(btn_F, text="Exit", command=self.Exit_app, bg="cadetblue", fg="white", pady=15, bd=4,
                          width=10, font="arial 14 bold").grid(row=0, column=3, padx=4, pady=5)

        self.welcome_bill()

    # =============functions for working=============================
    def total(self):
        self.c_fc_p = self.light1.get() * 50
        self.c_fw_p = self.light2.get() * 60
        self.c_hs_p = self.LightSmart.get() * 70

        self.total_cosemetic_price = float(
            self.c_fc_p +
            self.c_fw_p +
            self.c_hs_p
        )
        self.total_light_price.set("SGD " + str(self.total_cosemetic_price))

        self.c_hg_p = self.Safe1.get() * 100
        self.g_f_p = self.Safe2.get() * 120
        self.g_d_p = self.Safe3.get() * 125
        self.g_w_p = self.safesmart.get() * 200

        self.total_total_safe_price = float(
            self.c_hg_p +
            self.g_f_p +
            self.g_d_p +
            self.g_w_p
        )
        self.total_safe_price.set("SGD " + str(self.total_total_safe_price))


        self.Total_bill = float(
            self.total_cosemetic_price +
            self.total_total_safe_price)

    def welcome_bill(self):
        self.txtarea.delete('1.0', END)
        self.txtarea.insert(END, "\t Welcome to OSHSE \n")
        self.txtarea.insert(END, f"\n Customer ID : {self.customerID.get()}")
        self.txtarea.insert(END, f"\n Customer Name : {self.c_name.get()}")
        self.txtarea.insert(END, f"\n Phone Number : {self.c_phon.get()}")
        self.txtarea.insert(END, f"\n Address : {self.address.get()}")
        self.txtarea.insert(END, f"\n ====================================")
        self.txtarea.insert(END, f"\n Products\t\tQTY\t\tPrice")
        self.txtarea.insert(END, f"\n ====================================")

    def bill_area(self):
        if self.customerID.get() == "" or self.c_phon.get() == "":
            messagebox.showerror("Error", "Customer Details are must")
        elif self.total_light_price.get() == "SGD 0.0" and self.total_safe_price.get() == "SGD 0.0" :
            messagebox.showerror("Error", "No Product Purchased")
        else:
            self.welcome_bill()

            if self.light1.get() != 0:
                self.txtarea.insert(END, f"\n Light1\t\t{self.light1.get()}\t\t{self.c_fc_p}")

            if self.light2.get() != 0:
                self.txtarea.insert(END, f"\n Light2\t\t{self.light2.get()}\t\t{self.c_fw_p}")

            if self.LightSmart.get() != 0:
                self.txtarea.insert(END, f"\n SmartHome1-Light\t\t{self.LightSmart.get()}\t\t{self.c_hs_p}")

            if self.Safe1.get() != 0:
                self.txtarea.insert(END, f"\n Safe1\t\t{self.Safe1.get()}\t\t{self.c_hg_p}")

            if self.Safe2.get() != 0:
                self.txtarea.insert(END, f"\n Safe2\t\t{self.Safe2.get()}\t\t{self.g_f_p}")

            if self.Safe3.get() != 0:
                self.txtarea.insert(END, f"\n Safe3\t\t{self.Safe3.get()}\t\t{self.g_d_p}")

            if self.safesmart.get() != 0:
                self.txtarea.insert(END, f"\n SmartHome1-Safe\t\t{self.safesmart.get()}\t\t{self.g_w_p}")

            self.txtarea.insert(END, f"\n ------------------------------------")
            self.txtarea.insert(END, f"\n Total Bill : \t\t SGD {self.Total_bill}")
            self.txtarea.insert(END, f"\n ------------------------------------")


            if self.powlight1.get() == "USB" and self.light1.get() >= 1:
                messagebox.showerror("Error", "Light 1 (USB) is out of stock. Please select others.")
            elif (self.powlight1.get() == "Battery" or self.powlight2.get() == "Battery" or self.powlight3.get() == "Battery"
                or self.powsafe1.get() == "Battery" or self.powsafe2.get() == "Battery" or self.powsafe3.get() == "Battery"
                or self.powsafe4.get() == "Battery" or self.powlight2.get() == "USB" or self.powlight3.get() == "USB" or
                self.powsafe1.get() == "USB" or self.powsafe2.get() == "USB" or self.powsafe3.get() == "USB" or
                self.powsafe4.get() == "USB"):
                self.save_bill()



        con = mysql.connector.connect(host="localhost", user="root", password="s63127734", database="oshes")
        cur = con.cursor()



        if self.light1.get() == 0:
            print()

        # elif self.powlight1.get() == "USB":
        #     messagebox.showerror("Error", "Light 1 (USB) is out of stock. Please select others.")



        elif self.light1.get() == 1:
            cur.execute("UPDATE Item SET customerID = %s, purchaseStatus = %s, "
                        "dateOfPurchase = %s WHERE purchaseStatus = %s and color = %s and "
                        "powerSupply = %s and productID = %s ORDER BY itemID DESC LIMIT 1",
                 (self.customerID.get(),
                  self.soldStatus.get(),
                  date.today(),
                  self.purchaseStatus.get(),
                  self.l_color1.get(),
                  self.powlight1.get(),
                  self.light1Status.get()))
            row = cur.fetchone()
            con.commit()


        elif self.light1.get() == 2:
            cur.execute(
                "UPDATE Item SET customerID = %s, purchaseStatus = %s, "
                        "dateOfPurchase = %s WHERE purchaseStatus = %s and color = %s and "
                        "powerSupply = %s and productID = %s ORDER BY itemID DESC LIMIT 2",
                (self.customerID.get(),
                 self.soldStatus.get(),
                 date.today(),
                 self.purchaseStatus.get(),
                 self.l_color1.get(),
                 self.powlight1.get(),
                 self.light1Status.get()
                 ))
            row = cur.fetchone()

            con.commit()


        elif self.light1.get() == 3:
            cur.execute(
                "UPDATE Item SET customerID = %s, purchaseStatus = %s, "
                "dateOfPurchase = %s WHERE purchaseStatus = %s and color = %s and "
                "powerSupply = %s and productID = %s ORDER BY itemID DESC LIMIT 3",
                (self.customerID.get(),
                 self.soldStatus.get(),
                 date.today(),
                 self.purchaseStatus.get(),
                 self.l_color1.get(),
                 self.powlight1.get(),
                 self.light1Status.get()
                 ))
            row = cur.fetchone()

            con.commit()
        else:  ### need to select and give error if it is out of stock.
            messagebox.showerror("Error", "Quantity Selected for Lights 1 is above inventory level OR Out of Stock. \n"
                                          "Please try again", parent=self.root)
            print(0)

        # =========================================================Light 2======================================================================
        if self.light2.get() == 0:
            print()

        elif self.light2.get() == 1:
            cur.execute(
                "UPDATE Item SET customerID = %s, purchaseStatus = %s, "
                "dateOfPurchase = %s WHERE purchaseStatus = %s and color = %s and "
                "powerSupply = %s and productID = %s ORDER BY itemID DESC LIMIT 1",
                (self.customerID.get(),
                 self.soldStatus.get(),
                 datetime.now(),
                 self.purchaseStatus.get(),
                 self.l_color2.get(),
                 self.powlight2.get(),
                 self.light2Status.get()
                 ))
            row = cur.fetchone()

            con.commit()

        elif self.light2.get() == 2:
            cur.execute(
                "UPDATE Item SET customerID = %s, purchaseStatus = %s, "
                "dateOfPurchase = %s WHERE purchaseStatus = %s and color = %s and "
                "powerSupply = %s and productID = %s ORDER BY itemID DESC LIMIT 2",
                (self.customerID.get(),
                 self.soldStatus.get(),
                 date.today(),
                 self.purchaseStatus.get(),
                 self.l_color2.get(),
                 self.powlight2.get(),
                 self.light2Status.get()
                 ))
            row = cur.fetchone()

            con.commit()
        elif self.light2.get() == 3:
            cur.execute(
                "UPDATE Item SET customerID = %s, purchaseStatus = %s, "
                "dateOfPurchase = %s WHERE purchaseStatus = %s and color = %s and "
                "powerSupply = %s and productID = %s ORDER BY itemID DESC LIMIT 3",
                (self.customerID.get(),
                 self.soldStatus.get(),
                 date.today(),
                 self.purchaseStatus.get(),
                 self.l_color2.get(),
                 self.powlight2.get(),
                 self.light2Status.get()
                 ))
            row = cur.fetchone()

            con.commit()
        else:  ### need to select and give error if it is out of stock.
            messagebox.showerror("Error", "Quantity Selected for Lights 2 is above inventory level OR Out of Stock. \n"
                                          "Please try again", parent=self.root)
            print(0)

            # =========================================================Light 3======================================================================
        if self.LightSmart.get() == 0:
            print()

        elif self.LightSmart.get() == 1:
            cur.execute(
                "UPDATE Item SET customerID = %s, purchaseStatus = %s, "
                "dateOfPurchase = %s WHERE purchaseStatus = %s and color = %s and "
                "powerSupply = %s and productID = %s ORDER BY itemID DESC LIMIT 1",
                (self.customerID.get(),
                 self.soldStatus.get(),
                 date.today(),
                 self.purchaseStatus.get(),
                 self.l_color3.get(),
                 self.powlight3.get(),
                 self.light3Status.get()
                 ))
            row = cur.fetchone()

            con.commit()
        elif self.LightSmart.get() == 2:
            cur.execute(
                "UPDATE Item SET customerID = %s, purchaseStatus = %s, "
                "dateOfPurchase = %s WHERE purchaseStatus = %s and color = %s and "
                "powerSupply = %s and productID = %s ORDER BY itemID DESC LIMIT 2",
                (self.customerID.get(),
                 self.soldStatus.get(),
                 date.today(),
                 self.purchaseStatus.get(),
                 self.l_color3.get(),
                 self.powlight3.get(),
                 self.light3Status.get()
                 ))
            row = cur.fetchone()

            con.commit()
        elif self.LightSmart.get() == 3:
            cur.execute(
                "UPDATE Item SET customerID = %s, purchaseStatus = %s, "
                "dateOfPurchase = %s WHERE purchaseStatus = %s and color = %s and "
                "powerSupply = %s and productID = %s ORDER BY itemID DESC LIMIT 3",
                (self.customerID.get(),
                 self.soldStatus.get(),
                 date.today(),
                 self.purchaseStatus.get(),
                 self.l_color3.get(),
                 self.powlight3.get(),
                 self.light3Status.get()
                 ))
            row = cur.fetchone()

            con.commit()
        else:  ### need to select and give error if it is out of stock.
            messagebox.showerror("Error", "Quantity Selected for SmartHome1 is above inventory level OR Out of Stock. \n"
                                          "Please try again", parent=self.root)
            print(0)

        #===========================================================Safe =================================================================
        if self.Safe1.get() == 0:
            print()

        elif self.Safe1.get() == 1:
            cur.execute(
                "UPDATE Item SET customerID = %s, purchaseStatus = %s, "
                "dateOfPurchase = %s WHERE purchaseStatus = %s and color = %s and "
                "powerSupply = %s and productID = %s ORDER BY itemID DESC LIMIT 1",
                (self.customerID.get(),
                 self.soldStatus.get(),
                 date.today(),
                 self.purchaseStatus.get(),
                 self.l_safe1.get(),
                 self.powsafe1.get(),
                 self.safe1Status.get()
                 ))
            row = cur.fetchone()

            con.commit()
        elif self.Safe1.get() == 2:
            cur.execute(
                "UPDATE Item SET customerID = %s, purchaseStatus = %s, "
                "dateOfPurchase = %s WHERE purchaseStatus = %s and color = %s and "
                "powerSupply = %s and productID = %s ORDER BY itemID DESC LIMIT 2",
                (self.customerID.get(),
                 self.soldStatus.get(),
                 date.today(),
                 self.purchaseStatus.get(),
                 self.l_safe1.get(),
                 self.powsafe1.get(),
                 self.safe1Status.get()
                 ))
            row = cur.fetchone()

            con.commit()
        elif self.Safe1.get() == 3:
            cur.execute(
                "UPDATE Item SET customerID = %s, purchaseStatus = %s, "
                "dateOfPurchase = %s WHERE purchaseStatus = %s and color = %s and "
                "powerSupply = %s and productID = %s ORDER BY itemID DESC LIMIT 3",
                (self.customerID.get(),
                 self.soldStatus.get(),
                 date.today(),
                 self.purchaseStatus.get(),
                 self.l_safe1.get(),
                 self.powsafe1.get(),
                 self.safe1Status.get()
                 ))
            row = cur.fetchone()

            con.commit()
        else:  ### need to select and give error if it is out of stock.
            messagebox.showerror("Error", "Quantity Selected for Safe 1 is above inventory level OR Out of Stock. \n"
                                          "Please try again", parent=self.root)
            print(0)

        #==============Safe 2 ======================
        if self.Safe2.get() == 0:
            print()

        elif self.Safe2.get() == 1:
            cur.execute(
                "UPDATE Item SET customerID = %s, purchaseStatus = %s, "
                "dateOfPurchase = %s WHERE purchaseStatus = %s and color = %s and "
                "powerSupply = %s and productID = %s ORDER BY itemID DESC LIMIT 1",
                (self.customerID.get(),
                 self.soldStatus.get(),
                 date.today(),
                 self.purchaseStatus.get(),
                 self.l_safe2.get(),
                 self.powsafe2.get(),
                 self.safe2Status.get()
                 ))
            row = cur.fetchone()

            con.commit()
        elif self.Safe2.get() == 2:
            cur.execute(
                "UPDATE Item SET customerID = %s, purchaseStatus = %s, "
                "dateOfPurchase = %s WHERE purchaseStatus = %s and color = %s and "
                "powerSupply = %s and productID = %s ORDER BY itemID DESC LIMIT 2",
                (self.customerID.get(),
                 self.soldStatus.get(),
                 date.today(),
                 self.purchaseStatus.get(),
                 self.l_safe2.get(),
                 self.powsafe2.get(),
                 self.safe2Status.get()
                 ))
            row = cur.fetchone()

            con.commit()
        elif self.Safe2.get() == 3:
            cur.execute(
                "UPDATE Item SET customerID = %s, purchaseStatus = %s, "
                "dateOfPurchase = %s WHERE purchaseStatus = %s and color = %s and "
                "powerSupply = %s and productID = %s ORDER BY itemID DESC LIMIT 3",
                (self.customerID.get(),
                 self.soldStatus.get(),
                 date.today(),
                 self.purchaseStatus.get(),
                 self.l_safe2.get(),
                 self.powsafe2.get(),
                 self.safe2Status.get()
                 ))
            row = cur.fetchone()

            con.commit()
        else:  ### need to select and give error if it is out of stock.
            messagebox.showerror("Error", "Quantity Selected for Safe 2 is above inventory level OR Out of Stock. \n"
                                          "Please try again", parent=self.root)
            print(0)

        #=====================Safe 3 =========================
        if self.Safe3.get() == 0:
            print()

        elif self.Safe3.get() == 1:
            cur.execute(
                "UPDATE Item SET customerID = %s, purchaseStatus = %s, "
                "dateOfPurchase = %s WHERE purchaseStatus = %s and color = %s and "
                "powerSupply = %s and productID = %s ORDER BY itemID DESC LIMIT 1",
                (self.customerID.get(),
                 self.soldStatus.get(),
                 date.today(),
                 self.purchaseStatus.get(),
                 self.l_safe3.get(),
                 self.powsafe3.get(),
                 self.safe3Status.get()
                 ))
            row = cur.fetchone()

            con.commit()
        elif self.Safe3.get() == 2:
            cur.execute(
                "UPDATE Item SET customerID = %s, purchaseStatus = %s, "
                "dateOfPurchase = %s WHERE purchaseStatus = %s and color = %s and "
                "powerSupply = %s and productID = %s ORDER BY itemID DESC LIMIT 2",
                (self.customerID.get(),
                 self.soldStatus.get(),
                 date.today(),
                 self.purchaseStatus.get(),
                 self.l_safe3.get(),
                 self.powsafe3.get(),
                 self.safe3Status.get()
                 ))
            row = cur.fetchone()

            con.commit()
        elif self.Safe3.get() == 3:
            cur.execute(
                "UPDATE Item SET customerID = %s, purchaseStatus = %s, "
                "dateOfPurchase = %s WHERE purchaseStatus = %s and color = %s and "
                "powerSupply = %s and productID = %s ORDER BY itemID DESC LIMIT 3",
                (self.customerID.get(),
                 self.soldStatus.get(),
                 date.today(),
                 self.purchaseStatus.get(),
                 self.l_safe3.get(),
                 self.powsafe3.get(),
                 self.safe3Status.get()
                 ))
            row = cur.fetchone()

            con.commit()
        else:  ### need to select and give error if it is out of stock.
            messagebox.showerror("Error", "Quantity Selected for Safe 3 is above inventory level OR Out of Stock. \n"
                                          "Please try again", parent=self.root)
            print(0)

        #======================= Safe 4 =========================
        if self.safesmart.get() == 0:
            print()

        elif self.safesmart.get() == 1:
            cur.execute(
                "UPDATE Item SET customerID = %s, purchaseStatus = %s, "
                "dateOfPurchase = %s WHERE purchaseStatus = %s and color = %s and "
                "powerSupply = %s and productID = %s ORDER BY itemID DESC LIMIT 1",
                (self.customerID.get(),
                 self.soldStatus.get(),
                 date.today(),
                 self.purchaseStatus.get(),
                 self.l_safe4.get(),
                 self.powsafe4.get(),
                 self.safe4Status.get()
                 ))
            row = cur.fetchone()

            con.commit()
        elif self.safesmart.get() == 2:
            cur.execute(
                "UPDATE Item SET customerID = %s, purchaseStatus = %s, "
                "dateOfPurchase = %s WHERE purchaseStatus = %s and color = %s and "
                "powerSupply = %s and productID = %s ORDER BY itemID DESC LIMIT 2",
                (self.customerID.get(),
                 self.soldStatus.get(),
                 date.today(),
                 self.purchaseStatus.get(),
                 self.l_safe4.get(),
                 self.powsafe4.get(),
                 self.safe4Status.get()
                 ))
            row = cur.fetchone()

            con.commit()
        elif self.safesmart.get() == 3:
            cur.execute(
                "UPDATE Item SET customerID = %s, purchaseStatus = %s, "
                "dateOfPurchase = %s WHERE purchaseStatus = %s and color = %s and "
                "powerSupply = %s and productID = %s ORDER BY itemID DESC LIMIT 3",
                (self.customerID.get(),
                 self.soldStatus.get(),
                 date.today(),
                 self.purchaseStatus.get(),
                 self.l_safe4.get(),
                 self.powsafe4.get(),
                 self.safe4Status.get()
                 ))
            row = cur.fetchone()
            con.commit()
        else:  ### need to select and give error if it is out of stock.
            messagebox.showerror("Error", "Quantity Selected for SmartHome1 is above inventory level OR Out of Stock. \n"
                                          "Please try again", parent=self.root)
            








    def save_bill(self):
        if self.powlight1 != "USB":
            op = messagebox.askyesno("Saving Bill.....", "Do You Want Save your Bill")

        if op > 0:
            self.bill_data = self.txtarea.get('1.0', END)
            f1 = open(r"C:\Login"+"\Bills" + str(self.customerID.get()) + ".txt", "w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saving.....",
                                f"{self.customerID.get()} Your Bill No : {self.customerID.get()}  Successfully Saved. Please see the Bills folder on bill directory to see your Bills")
        else:
            return

    def find_bill(self):
        present = "no"
        for i in os.listdir("Bills/"):
            if i.split('.')[0] == self.search_bill.get():
                f1 = open(f"Bills/{i}", "r")
                self.txtarea.delete('1.0', END)
                for d in f1:
                    self.txtarea.insert(END, d)
                f1.close()
                present = "yes"
        if present == "no":
            messagebox.showerror("Error", "Invalid Bill Number ..Please Enter Valid Bill Number")

    def clear_data(self):
        op = messagebox.askyesno("Clearing...", "Do You Really Want to Clear All data")
        if op > 0:
            # ================Cosemetics==========================

            self.light1.set(0)
            self.light2.set(0)
            self.LightSmart.set(0)
            self.Safe1.set(0)

            self.Safe3.set(0)
            self.safesmart.set(0)

            # ================Total Product Price variables==========================

            self.total_light_price.set("")
            self.total_safe_price.set("")


            # ================Cutomers==================================

            #self.customerID.set("")
            #self.c_phon.set("")

            self.bill_no.set("")

            self.search_bill.set("")
            self.welcome_bill()


    def Exit_app(self):
        op = messagebox.askyesno("Exit", "Do You Really Want to Exit")
        if op > 0:
            self.root.destroy()

if __name__ =="__main__":
    root=Tk()
    main = Bill_App(root)
    root.mainloop()
