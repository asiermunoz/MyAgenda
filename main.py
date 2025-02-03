import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

window = tk.Tk()
window.geometry("600x400")

input_name = tk.Entry(window)
label_name = tk.Label(window, text = "Name: ")

input_phone = tk.Entry(window)
label_phone = tk.Label(window, text = "Phone: ")

tree_contacts = ttk.Treeview(window, columns=("id", "name", "phone"), show="headings")

contacts = []

def add():
    name = input_name.get()
    phone = input_phone.get()
    if not(name and phone):
        messagebox.showwarning("campo vacios", "debes rellenar todos los campos")
        return
    
    for cont in contacts:
        if name in cont and phone in cont:
            messagebox.showwarning("campo repetido", "el nombre o telefono ya existe")
            return
    id = len(contacts) + 1
    contacts.append([id, name, phone])
    print(contacts)
    update()

def update():
    for elem in tree_contacts.get_children():
        tree_contacts.delete(elem)
    for contact in contacts:
        tree_contacts.insert("", "end", values=(contact[0], contact[1], contact[2]))

def remove_selected():
    selected = tree_contacts.selection()
    if selected:
        contacto = tree_contacts.item(selected, "values")
        selected_contact = list(contacto)
        selected_contact = [int(selected_contact[0]), selected_contact[1], selected_contact[2]]
        
        if selected_contact in contacts:
            contacts.remove(selected_contact)
            tree_contacts.delete(selected)
        else:
            print("Contact not found in the list")

def update_selected():
    selected = tree_contacts.selection()
    if selected:
        contacto = tree_contacts.item(selected, "values")
        selected_contact = list(contacto)
        selected_contact = [int(selected_contact[0]), selected_contact[1], selected_contact[2]]
        
        # Capture new values from input fields (assuming you have entry widgets for name and phone)
        new_name = input_name.get()
        new_phone = input_phone.get()
        
        # Find the index of the selected contact in the contacts list
        for idx, contact in enumerate(contacts):
            if contact[0] == selected_contact[0]:
                # Update the contact with new values
                contacts[idx] = [selected_contact[0], new_name, new_phone]
                break
        
        # Update the tree view
        update()

        

btn_add = tk.Button(window, text = "ADD", command=add)

btn_remove = tk.Button(window, text="DEL", command=remove_selected)
btn_update = tk.Button(window, text="UPD", command=update_selected)


#PACKS

label_name.grid(row=0, column=0, pady=5)
input_name.grid(row=0, column=1, pady=5)
label_phone.grid(row=0, column=2, pady=5)
input_phone.grid(row=0, column=3, pady=5)
btn_add.grid(row=1, column=0, pady=5)
btn_remove.grid(row=1, column=1, pady=5)
btn_update.grid(row=1, column=2, pady=5)
tree_contacts.grid(row=2, column=0, columnspan=4)

tree_contacts.heading("id", text="ID")
tree_contacts.heading("name", text="NAME")
tree_contacts.heading("phone", text="PHONE")

tree_contacts.column("id", anchor="center")
tree_contacts.column("name", anchor="center")
tree_contacts.column("phone", anchor="center")


window.mainloop()