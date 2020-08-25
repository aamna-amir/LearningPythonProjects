# 7. Email Slicer
# This is a convenient program that has a lot of use in the future. 
# The program helps get you the username and domain name from an email address. 
# You can even customize the application and send a message to the host with this information.

email = input("Enter your email address: ")

user_name = email[:email.index("@")]

domain = email[email.index("@")+1:]

print(f"Your user name is {user_name} and domain is {domain}")