# 6. Contact Book
# This is an excellent python project idea for beginners. 
# Everyone uses a contact book to save contact details, including name, address, phone number, and even email address. 
# This is a command-line project where you will design a contact book application that users can use to save and find contact details. 
# The application should also allow users to update contact information, delete contacts, and list saved contacts. 
# The SQLite database is the ideal platform for saving contacts.

print("\nContact Book\n")

contact_list = []
class Contact:
    def __init__(self, name, address, phone, email):
        self.name = name
        self.address = address
        self.phone = phone
        self.email = email

    def add_contact(self):
        print("\nAdd New Contact")
        name = input("\nName: \t\t")
        self.name = name
        address = input("Address: \t")
        self.address = address
        phone = input("Phone No.: \t")
        self.phone = phone
        email = input("Email: \t\t")
        self.email = email
        contact_dict = {'Name': self.name, 'Address': self.address, 'Phone No': self.phone, 'Email': self.email}
        contact_list.append(contact_dict)

    def display(self):
        print("\nContact Details\n")
        print("Name: \t\t", self.name)
        print("Address: \t", self.address)
        print("Phone: \t\t", self.phone)
        print("Email: \t\t", self.email)

c1 = Contact('','','','')
c1.display()
c1.add_contact()
c1.add_contact()
print(contact_list)
c1.display()