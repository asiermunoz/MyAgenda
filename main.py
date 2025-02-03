import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.geometry("600x400")

input_name = tk.Entry(window)
label_name = tk.Label(window, text = "Name: ")

input_phone = tk.Entry(window)
label_phone = tk.Label(window, text = "Phone: ")

tree_contacts = ttk.Treeview(window, columns=("id", "name", "phone"), show="headings")

contacts = [

]

def add():
    name = input_name.get()
    phone = input_phone.get()
    id = len(contacts) + 1
    #contacts.append([id, name, phone])
    #print(contacts)
    update()

def update():
    for elem in tree_contacts.get_children:
        tree_contacts.delete(elem)
    for contact in contacts:
        tree_contacts.insert("", "end", values=())


btn_add = tk.Button(window, text = "add", command=add)


#PACKS

label_name.pack()
input_name.pack(pady=(0,20))
label_phone.pack()
input_phone.pack(pady=(0,20))
btn_add.pack()
tree_contacts.pack(pady=20)

tree_contacts.heading("id", text="ID")
tree_contacts.heading("name", text="NAME")
tree_contacts.heading("phone", text="PHONE")

tree_contacts.insert("", "end", values=(1, "luis", 12345))


window.mainloop()