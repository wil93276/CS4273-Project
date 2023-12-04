import shelve
from ValidatePassword import ValidatePassword #line added by john 11/27 4:40PM
from HashPassword import HashPassword 

def CreateUser(username, password):
    with shelve.open('accountInfo') as db:
        if username in db:
            db.close()
            return False
        if not ValidatePassword(password): 
            db.close()
            return False
        db[username] = HashPassword(password)
        db.close()
        return True


#Unit tests
#Test that tries to create an account with a valid username and password
def CreateUserSuccess():
    if CreateUser("TESTUSER", "Testpass1!"):
        print("TEST PASS: Succeed on attempt to create user with unique username and valid password")
    else:
        print("TEST FAIL: Succeed on attempt to create user with unique username and valid password")

#Test that tries to create an account with an existing username
def CreateUserExisting():
    if not CreateUser("TESTUSER", "Testpass1!"):
        print("TEST PASS: Fail on attempt to create user with existing username")
    else:
        print("TEST FAIL: Fail on attempt to create user with existing username")

#Test that tries to create an account with an invalid password
def CreateUserBadPass():
    if not CreateUser("TESTUSER2", "Badpas1"):
        print("TEST PASS: Fail on attempt to create user with password less than 8 characters")
    else:
        print("TEST FAIL: Fail on attempt to create user with password less than 8 characters")
    
    if not CreateUser("TESTUSER3", "badpassword1"):
        print("TEST PASS: Fail on attempt to create user with password containing no uppercase character")
    else:
        print("TEST FAIL: Fail on attempt to create user with password containing no uppercase character")
    
    if not CreateUser("TESTUSER4", "Badpassword"):
        print("TEST PASS: Fail on attempt to create user with password containing no number character")
    else:
        print("TEST FAIL: Fail on attempt to create user with password containing no number character")
    

#Run all tests if this file is run
if __name__ == "__main__":
    CreateUserSuccess()
    CreateUserExisting()
    CreateUserBadPass()
    
    #Test that it fails to create users in test shelve file
    print(CreateUser("user1", "Password1"))
    print(CreateUser("user2", "Password2"))
    print(CreateUser("user3", "Password3"))

    #Delete the test users from the shelve file
    with shelve.open('accountInfo') as db:
        if "TESTUSER" in db:
            del db["TESTUSER"]
        if "TESTUSER2" in db:
            del db["TESTUSER2"]
        if "TESTUSER3" in db:
            del db["TESTUSER3"]
        if "TESTUSER4" in db:
            del db["TESTUSER4"]
