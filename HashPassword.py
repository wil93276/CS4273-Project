import shelve
import hashlib
# Return hashed password
def HashPassword(password):
    # Using the hashlib library, using the sha256 algorithm to hash a given password
    sha256 = hashlib.sha256()
    sha256.update(password.encode()) # Method takes encoded data as an argument
    return sha256.hexdigest() # returns a string object of double length that contains hexadecimal digits
    if __name__ == '__main__':
            print(HashPassword('test'))

