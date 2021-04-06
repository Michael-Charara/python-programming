# Accept password from the user
print("Password should contain at least 1 upper case letter, one lower case letter, one number, be at least 6 characters in length, and no more than 20 characters in length.")
password = input("Enter password: ")
valid = False

# if statment to check the password for number of characters
if(len(password) > 6 and len(password) <= 20):
    lowercase_letter = False
    uppercase_letter = False
    number = False

    # for-loop to check if password contains one lower letter, one uppercase letter, and one numebr
    for character in password:
        if(character.isupper()):
            uppercase_letter = True
        if(character.islower()):
            lowercase_letter = True
        if(character.isdigit()):
            number = True

        if(lowercase_letter and uppercase_letter and number):
            valid = True
            break
# if statment to check if password is valid or not
if(valid):
    print("password is valid")
else:
    print("Password is Invalid")
