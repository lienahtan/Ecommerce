from pymongo import MongoClient
from tkinter import *
# from tkinter.ttk import *
import tkinter.messagebox as mb
from PIL import ImageTk, Image

#Making Connection
myclient = MongoClient("mongodb://localhost:27017/")

#database
db = myclient["OSHES"]

#Created or Swqitched to Collection
#name: product

Collection = db["product"]

light = Collection.find({"Category":"Lights"})
for lights in light:
    print(lights)

'''
root = Tk()

class Search:

    def __init__(self, root):

        self.root = root
        self.root.title("Login System (OSHES)")
        self.root.geometry("1280x700+200+70")
        self.root.resizable(False, False)

        #Adding image#

        self.image=ImageTk.PhotoImage(file="/Login/light5.jpg")
        self.label=Label(self.root, image=self.image)
        self.label.pack()

        
        #Login Frame
        frame1=Frame(self.root, bg="white")
        frame1.place(x=480, y=100, width=700, height=500)

        #Name
        name = Label(frame1, text = "Name", font=("calibri",15,"bold"),bg="white", fg="gray")
        name.place(x=50,y=100)
        
        txt_name = Entry(frame1, font=("calibri",15), bg="lightgray", state=DISABLED, textvariable=x)
        txt_name.place(x=50, y=130, width=250)


main = Search(root)
root.mainloop()
'''



