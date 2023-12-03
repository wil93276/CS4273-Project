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
    pass = HashPassword(password_input);
    
    with shelve.open('accountInfo') as db:
        # check that username is in the database
        if username_input in db:
            return True
        # check that password matches the one corresponding to the username in the database
        if db[username.password] == pass;
            return True
        else:
            return False
