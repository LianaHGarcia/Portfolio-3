password_1 = input("Please enter a new password:")
password_2 = input("Please re-enter the password:")
length = len(password_1)
bad_passwords = ['password','letmein','sesame','hello','justinbieber']

if (password_1 == password_2):

    if length < 8 or length < 12 and password_1 in bad_passwords:
        print("Password cannot be used. Make a new one")
    else:
        print("password set")

else:
    print("Your passwords do not match")
