email = input("Enter your e-mail: ")
emailsplit = email.split("@")
username = emailsplit[0]
domain = emailsplit[1]
print("Your e-mail username is",username)
print("Your e-mail domain is",domain)
