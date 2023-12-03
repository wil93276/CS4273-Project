import shelve
import hashlib
# Return hashed password
def HashPassword(password):
    # Using the hashlib library, using the sha256 algorithm to hash a given password
    sha256 = hashlib.sha256()
    sha256.update(password.encode()) # Updated method takes encoded data as an argument
    return password
