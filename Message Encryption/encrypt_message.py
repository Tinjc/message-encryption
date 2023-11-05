from cryptography.fernet import Fernet

def encrypt(message):
    # Opening the key
    with open("id.key", "rb") as filekey:
        key = filekey.read()
    # Using the generated key
    fernet = Fernet(key)
    # Actually ENCRYPTING the file
    encrypted = fernet.encrypt(message)
    with open("enc_message.txt", "wb") as file:
        file.write(encrypted)

    

