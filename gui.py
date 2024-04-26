from tkinter import *
from tkinter import messagebox

#Method
def Login():
    username = entry1.get()
    password = entry2.get()

    #Decision making
    if username == " " and password == " ":
        messagebox.showinfo("", "Please fill in blank spaces")

    elif username == "joshua" and password == "cyb3rs3c":
        messagebox.showinfo("", "Login successful")

    else:
        messagebox.showinfo("", "Enter correct details!")

#constructor frame
root = Tk()
root.title("Login")
root.geometry("300x400")

global entry1
global entry2

#constructor window
Label(root, text = "Username").place(x = 20, y = 20)
Label(root, text = "Password").place(x = 20, y = 60)

entry1 = Entry(root, bd = 5)
entry1.place(x = 120, y = 20)
entry2 = Entry(root, bd = 5)
entry2.place(x = 120, y = 60)

Button(root, text = "Login", command = Login, height = 2, bd = 3).place(x = 30, y = 100)

#Add mainloop(root)
root.mainloop()

