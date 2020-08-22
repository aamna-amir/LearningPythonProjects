# 6. Contact Book
# This is an excellent python project idea for beginners. 
# Everyone uses a contact book to save contact details, including name, address, phone number, and even email address. 
# This is a command-line project where you will design a contact book application that users can use to save and find contact details. 
# The application should also allow users to update contact information, delete contacts, and list saved contacts. 
# The SQLite database is the ideal platform for saving contacts.

print("\nContact Book\n")

class Contact:
    def __init__(self, name, address, phone, email):
        self.name = name
        self.address = address
        self.phone = phone
        self.email = email

    def display(self):
        print("\nContact Details\n")
        print("Name: ", self.name)
        print("Address: ", self.address)
        print("Phone: ", self.phone)
        print("Email: ", self.email)