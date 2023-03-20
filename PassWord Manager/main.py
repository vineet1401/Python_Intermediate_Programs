from tkinter import *
import random
import pandas as pd
import json
from tkinter import messagebox

# --------------------------------------ADD TO FILE------------------------------------------------

def Add():
    website = website_name.get()
    user = user_name.get()
    password = password_name.get()

    dic = {
        website: {
        "User":user, 
        "Password":password}
        }

    if(len(website)==0 or len(user)==0 or len(password)==0):
        messagebox.showinfo(title="Data Entry", message="You can't leave any field box empty!")
    else:
        try:
            with open("password.json", "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            with open("password.json", "w") as file:
                json.dump(dic, file, indent=4)
        else:
            data.update(dic)
            with open("password.json", "w") as file:
                json.dump(data, file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ------------------------------------SEARCH IN FILE--------------------------------------------------
def search():
    website = website_entry.get()
    try:
        with open("password.json") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="File not Found")
    else:
        if website in data:
            email = data[website]["User"]
            password = data[website]["Password"]
            messagebox.showinfo(title=website, message=f"User Name : {email} \nPassword : {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")

# --------------------------------GENERATE PASSWORD------------------------------------------

def Generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z','!', '#', '$', '%', '&', '(', ')', '*', '+', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    mypass = random.choice(letters)
    for i in range(15):
        mypass += (random.choice(letters))
    password_entry.insert(0, f"{mypass}")
    
# -----------------------------------------WINDOW LAYOUT-------------------------------------------------------------

window = Tk()
window.title("Password Manager".center(200))
window.config(height=500, width=700, padx=20, pady=20, background="#f7f5dd")

# ------------------------------------------BACKGROUND OF WINDOW-------------------------------------------------

canvas = Canvas(height=200, width=400, bg="#f7f5dd", highlightthickness=0)
lock = PhotoImage(file="D:\CODING MATERIAL\Python Practise\INTERMEDIATE PYTHON PROGRAMMING\TKINTER PROGRAM\PassWord Manager\lock.png")
canvas.create_image(200, 80, image=lock)
canvas.create_text(200, 180, text="Password Manager", font=("Courier", 25, 'bold'), fill='blue')
canvas.grid(row= 0, column=0, columnspan=3)

#-------------------------------------------HEADING LABEL------------------------------------------------------------------ 

label = Label()
label.config(text="Add your User Name and Password and add it to the File.", font=("Courier", 10), background="#f7f5dd")
label.grid(row=2, column=0, columnspan=3)

# ----------------------------------------------WEBSITE ENTRY-------------------------------------------------------------

website = Label(height=2)
website.config(text='Website :', font=("Courier", 12, 'bold'), background="#f7f5dd", fg='black')
website.grid(row=3, column=0)

website_name = StringVar()
website_entry = Entry(width=21, justify=LEFT)
website_entry.config(textvariable=website_name)
website_entry.grid(row=3, column=1)

#----------------------------------------SEARCH BUTTON--------------------------------------------------
search_button = Button(text="SEARCH", command=search, width=15, justify=RIGHT)
search_button.config(font=("Courier", 12, "bold"), background="white", height=1)
search_button.grid(row=3, column=2)

# -------------------------------------------------------------------------
user = Label(height=2)
user.config(text='Email/Username :', font=("Courier", 12, 'bold'), background="#f7f5dd", fg='black')
user.grid(row=4, column=0)

user_name = StringVar()
username_entry = Entry(width=50, justify=LEFT)
username_entry.config(textvariable=user_name)
username_entry.grid(row=4, column=1, columnspan=2)
username_entry.insert(0, "sakpalvineet1401@gmail.com")

# -----------------------------------------------------------------------------

password = Label(height=2)
password.config(text='Password :', font=("Courier", 12, 'bold'), background="#f7f5dd", fg='black')
password.grid(row=5, column=0)

password_name = StringVar()
password_entry = Entry(width=21, justify='left')
password_entry.config(textvariable=password_name)
password_entry.grid(row=5, column=1)

# ------------------------------------------------------------------------------------------------

generate_button = Button(text='Generate', width=15, command=Generate)
generate_button.config(font=("Courier", 12, 'bold'), background='white', height=1)
generate_button.grid(row=5, column=2)

# ------------------------------------------------------------------------------------------

add = Button(text='Add Password', width=30, command=Add)
add.config(font=("Courier", 12, 'bold'), background='white', height=1)
add.grid(row=6, column=1, columnspan=2)

# -------------------------------------------------------------------------

success = Label(pady=10, padx=10)
success.grid(row=7, column=1, columnspan=2)






window.mainloop()