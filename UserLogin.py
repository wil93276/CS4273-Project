import shelve
import HashPassword

def UserLogin(username,password):
#Hashes input password
#Checks if input password matches the hash for the given username
#On a match, return true; otherwise, return false

    # accept user input of username and password
    username_input = input("Enter username: ");
    password_input = input("Enter password: ");
    
    # hash the input password
    passHash = HashPassword(password_input);
    
    with shelve.open('accountInfo') as db:
        # check that username is in the database
        # check that password matches the one corresponding to the username in the database
        if (username in db) and (db[username] == passHash):
            return True
        else:
            return False
