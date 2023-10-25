username = "python"
password = "rules"
x = 0
while True:
    u_user = input("Username: ")
    u_pass = input("Password: ")

    if u_user == username and u_pass == password:
        print("Welcome")
        break
    else:
        print("Incorrect information.")
        x += 1

    if x == 5:
        print("Access Denied.")
        break