print("SECURE LOGIN")

# This is an input statment that asks for the username and then converts it to lowercase
username = input("Username > ").lower()
password = input("Password > ")
if username == "mark" and password == "password":
    print("Welcome Mark!")
# This is an elif statement that checks if the username and password are correct
elif username == "suzanne" and password == "Su74nne":
    print("Hey there Suzanne!")
elif username == "sam" and password == "password":
    print("Yo Sam!")
else:  # This is an else statement that checks if the username and password are correct
    print("Go Away!!")
