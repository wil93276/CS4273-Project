def ValidatePassword(password): # return true if password > 8 char, contains >= 1 uppercase, contains >= 1 number, and all chars are ascii. Otherwise print relevant error messages and return false
                                # takes plaintext password as argument

    numCount = 0 #initalize amount of numbers used in password to 0
    uppercaseCount = 0 #initialize amount of uppercase chars used in password to 0 
    invalidPassword = False #this bool allows us to inform user of multiple errors in the password rather than immediately returning false upon first error encountered

    if (len(password) <= 8):
        print("Password must be 9 or more characters in length")
        invalidPassword = True
    if(not password.isascii()):# will return false immediately, will not be checking isnumeric or isupper on non-ascii characters
        print("Password must be comprised of ASCII characters only")
        return False 

    for character in password: # iterate through each character to count number of uppercase characters and numbers
        if(character.isnumeric()):
            numCount+=1
        elif(character.isupper()):
            uppercaseCount+=1

    if(numCount < 1):
        invalidPassword = True
        print("Password must contain at least one number")
    if(uppercaseCount < 1):
        invalidPassword = True
        print("Password must contain at least one uppercase character")

    if(invalidPassword):
        return False
    else:
        return True
    


def ValidationTest():
    passwordArr = []
    passwordArr.append("HelloHello123")
    passwordArr.append("Abcdefg12345")
    passwordArr.append("Hello5")
    passwordArr.append("hello55555555")
    passwordArr.append("hello")
    passwordArr.append("рпакуеукапвы")

    for i in range(6):
        print("Password: " + passwordArr[i])
        print(ValidatePassword(passwordArr[i]))
        print()



if __name__ == "__main__":
    ValidationTest()