import shelve
from hashlib
# Using the hashlib library, using the sha256 algorithm to hash a given password
sha256 = hashlib.sha256()
# Return hashed password
def HashPassword(password):
    sha256.update(password)
    return password