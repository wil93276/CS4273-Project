import shelve
import hashlib
# Using the hashlib library, using the sha256 algorithm to hash a given password
sha256 = hashlib.sha256()
# Return hashed password
def HashPassword(password):
    hasher = hashlib.sha256()
    hasher.update(password.encode()) #update method takes encoded data as argument
    return password