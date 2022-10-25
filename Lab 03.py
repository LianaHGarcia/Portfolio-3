password_1 = input("Please enter a new password:")
password_2 = input("Please re-enter the password:")
length = len(password_1)
if (password_1 == password_2):

    if length < 8 or length > 13:
        print("Password needs to be between 8-12 characters")
    else:
        print("Password set")
else:
    print("Your passwords do not match")