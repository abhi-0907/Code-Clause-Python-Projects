import pyshorteners
from tkinter import *
import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", passwd="12345678", database="mydb973")
mycursor = mydb.cursor()


def convert_url():
    shorterClass = pyshorteners.Shortener()
    long_url = url_field.get()
    short_url = shorterClass.tinyurl.short(long_url)
    url_field.delete(0, END)
    url_field.insert(0, short_url)
    insert_query = "INSERT INTO shortnertable(longer_url,short_url) VALUES(%s,%s)"
    vals = (long_url, short_url)
    mycursor.execute(insert_query, vals)
    mydb.commit()


root = Tk()

root.title("URL Shorter")

appTitle = Label(root, text="URL Shorter", font=("Century 30 bold"))
appTitle.pack(pady=20)

label = Label(root, text="Enter Your URL: ", font=("Century 18"))
label.pack(anchor="w", pady=10)

url_field = Entry(root, font=("Century 15"), width=40)
url_field.pack(anchor="w")

btn = Button(root, text="Convert", font=("Contury 17 bold"), command=convert_url, width=13, height=1, bg="blue",
             fg="white")
btn.pack(pady=30)

root.mainloop()