userName="Samuel"
passWord="sam83"
userinput = input("Enter the user name: ")
passwordinput = input("Enter The pass word: ")
if userinput==userName:
    if passwordinput==passWord:
        print("Login successful")
    else:
        print("Password is invalid")
else:
    print("The username and password are invalid")