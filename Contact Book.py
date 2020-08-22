# 6. Contact Book
# This is an excellent python project idea for beginners. 
# Everyone uses a contact book to save contact details, including name, address, phone number, and even email address. 
# This is a command-line project where you will design a contact book application that users can use to save and find contact details. 
# The application should also allow users to update contact information, delete contacts, and list saved contacts. 
# The SQLite database is the ideal platform for saving contacts.

print("\n-------------------Contact Book-------------------\n")

contact_list = []
class Contact:
    def __init__(self, name, address, phone, email):
        self.name = name
        self.address = address
        self.phone = phone
        self.email = email

    def add_contact(self):
        print("\n-------------------Add New Contact-------------------")
        name = input("\nFull Name\t: \t")
        self.name = name
        address = input("Address\t\t: \t")
        self.address = address
        phone = input("Phone No.\t: \t")
        self.phone = phone
        email = input("Email Address\t: \t")
        self.email = email
        contact_dict = {'Full Name': self.name, 'Address': self.address, 'Phone No': self.phone, 'Email Address': self.email}
        contact_list.append(contact_dict)

    def display(self):
        print("\n-------------------Contact Details-------------------\n")
        i = 0
        for contact in contact_list:
            i += 1
            print('Contact ', i,"\n")
            for key, value in contact.items():
                print(key, " \t:\t", value)

c1 = Contact('','','','')
c1.display()
c1.add_contact()
print("\n",contact_list)
c1.display()