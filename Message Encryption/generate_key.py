from cryptography.fernet import Fernet

def give_key():
    # Generate key
    key = Fernet.generate_key()
    # String the key in a file
    with open("id.key", "wb") as filekey:
        filekey.write(key)
    return key