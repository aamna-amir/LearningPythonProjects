# 6. Contact Book
# This is an excellent python project idea for beginners. 
# Everyone uses a contact book to save contact details, including name, address, phone number, and even email address. 
# This is a command-line project where you will design a contact book application that users can use to save and find contact details. 
# The application should also allow users to update contact information, delete contacts, and list saved contacts. 
# The SQLite database is the ideal platform for saving contacts.

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

    def search_contact(self):
        search = input("Enter Name: ")
        for contact in contact_list:
            if contact['Full Name'] == search:
                for key, value in contact.items():
                    print("\n-------------------Contact Book-------------------\n")
                    print(key, " \t:\t", value)

    def update_contact(self):
        search = input("Enter Name: ")
        for contact in contact_list:
            if contact['Full Name'] == search:
                print("\n-------------------Update Contact-------------------\n")
                contact['Full Name'] = input("\nFull Name\t: \t")
                contact['Address'] = input("Address\t\t: \t")
                contact['Phone No'] = input("Phone No.\t: \t")
                contact['Email Address'] = input("Email Address\t: \t")
    

c1 = Contact('','','','')

while True:
    print("\n-------------------Contact Book-------------------\n")

    user = int(input("\n1. Add Contact\n2. Contact Details\n3. Search Contact\n4. Update Contact\n5. Delete Contact\n6. Exit\n\nEnter Option No. : "))
    if user == 1:
        c1.add_contact()
    elif user == 2:
        c1.display()
    elif user == 3:
        c1.search_contact()
    elif user == 4:
        c1.update_contact()
    else:
        print("\n-------------------Saved-------------------\n")
        break
# print("\n",contact_list)