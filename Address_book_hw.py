import tkinter as tk
from tkinter import messagebox

class AddressBookApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Address Book")

        # Contact list stored in memory
        self.contacts = []

        # UI Elements
        self.create_widgets()

    def create_widgets(self):
        # Labels and Entry fields
        tk.Label(self.root, text="Name:").grid(row=0, column=0, sticky="w")
        self.name_entry = tk.Entry(self.root, width=40)
        self.name_entry.grid(row=0, column=1)

        tk.Label(self.root, text="Address:").grid(row=1, column=0, sticky="w")
        self.address_entry = tk.Entry(self.root, width=40)
        self.address_entry.grid(row=1, column=1)

        tk.Label(self.root, text="Mobile Number:").grid(row=2, column=0, sticky="w")
        self.mobile_entry = tk.Entry(self.root, width=40)
        self.mobile_entry.grid(row=2, column=1)

        tk.Label(self.root, text="Email:").grid(row=3, column=0, sticky="w")
        self.email_entry = tk.Entry(self.root, width=40)
        self.email_entry.grid(row=3, column=1)

        tk.Label(self.root, text="Birthday:").grid(row=4, column=0, sticky="w")
        self.birthday_entry = tk.Entry(self.root, width=40)
        self.birthday_entry.grid(row=4, column=1)

        # Listbox to display contacts
        self.contact_listbox = tk.Listbox(self.root, width=50, height=10)
        self.contact_listbox.grid(row=5, column=0, columnspan=2, pady=10)
        self.contact_listbox.bind('<<ListboxSelect>>', self.display_selected_contact)

        # Buttons
        tk.Button(self.root, text="Add", command=self.add_contact).grid(row=6, column=0, sticky="ew")
        tk.Button(self.root, text="Edit", command=self.edit_contact).grid(row=6, column=1, sticky="ew")
        tk.Button(self.root, text="Delete", command=self.delete_contact).grid(row=7, column=0, sticky="ew")
        tk.Button(self.root, text="Save", command=self.save_contact).grid(row=7, column=1, sticky="ew")
        tk.Button(self.root, text="Open", command=self.open_contact).grid(row=8, column=0, columnspan=2, sticky="ew")
        tk.Button(self.root, text="Search", command=self.search_contact).grid(row=9, column=0, columnspan=2, sticky="ew")

    def add_contact(self):
        contact = {
            "Name": self.name_entry.get(),
            "Address": self.address_entry.get(),
            "Mobile": self.mobile_entry.get(),
            "Email": self.email_entry.get(),
            "Birthday": self.birthday_entry.get()
        }

        if contact["Name"]:  # Ensure the name is not empty
            self.contacts.append(contact)
            self.contact_listbox.insert(tk.END, contact["Name"])
            self.clear_entries()
        else:
            messagebox.showwarning("Input Error", "Name field cannot be empty.")

    def display_selected_contact(self, event):
        selected_index = self.contact_listbox.curselection()
        if selected_index:
            contact = self.contacts[selected_index[0]]
            self.fill_entries(contact)

    def edit_contact(self):
        selected_index = self.contact_listbox.curselection()
        if selected_index:
            contact = self.contacts[selected_index[0]]
            contact["Name"] = self.name_entry.get()
            contact["Address"] = self.address_entry.get()
            contact["Mobile"] = self.mobile_entry.get()
            contact["Email"] = self.email_entry.get()
            contact["Birthday"] = self.birthday_entry.get()

            self.contact_listbox.delete(selected_index)
            self.contact_listbox.insert(selected_index, contact["Name"])
            self.clear_entries()
        else:
            messagebox.showwarning("Selection Error", "No contact selected to edit.")

    def delete_contact(self):
        selected_index = self.contact_listbox.curselection()
        if selected_index:
            self.contacts.pop(selected_index[0])
            self.contact_listbox.delete(selected_index)
            self.clear_entries()
        else:
            messagebox.showwarning("Selection Error", "No contact selected to delete.")

    def save_contact(self):
        messagebox.showinfo("Save", "Contacts are saved temporarily in memory while the app is running.")

    def open_contact(self):
        selected_index = self.contact_listbox.curselection()
        if selected_index:
            contact = self.contacts[selected_index[0]]
            messagebox.showinfo("Contact Details",
                                f"Name: {contact['Name']}\nAddress: {contact['Address']}\n"
                                f"Mobile: {contact['Mobile']}\nEmail: {contact['Email']}\n"
                                f"Birthday: {contact['Birthday']}")
        else:
            messagebox.showwarning("Selection Error", "No contact selected to open.")

    def search_contact(self):
        search_name = self.name_entry.get().strip().lower()
        if not search_name:
            messagebox.showwarning("Search Error", "Enter a name to search.")
            return

        for index, contact in enumerate(self.contacts):
            if contact["Name"].strip().lower() == search_name:
                self.contact_listbox.selection_clear(0, tk.END)  # Clear previous selection
                self.contact_listbox.selection_set(index)  # Highlight found contact
                self.contact_listbox.activate(index)
                self.fill_entries(contact)
                return
        
        messagebox.showinfo("Search Result", "No contact found with that name.")

    def fill_entries(self, contact):
        """Fill entry fields with selected contact details."""
        self.name_entry.delete(0, tk.END)
        self.name_entry.insert(0, contact["Name"])
        self.address_entry.delete(0, tk.END)
        self.address_entry.insert(0, contact["Address"])
        self.mobile_entry.delete(0, tk.END)
        self.mobile_entry.insert(0, contact["Mobile"])
        self.email_entry.delete(0, tk.END)
        self.email_entry.insert(0, contact["Email"])
        self.birthday_entry.delete(0, tk.END)
        self.birthday_entry.insert(0, contact["Birthday"])

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)
        self.mobile_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.birthday_entry.delete(0, tk.END)

# Run the app
root = tk.Tk()
app = AddressBookApp(root)
root.mainloop()
