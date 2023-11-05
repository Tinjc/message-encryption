from cryptography.fernet import Fernet
from encrypt_message import encrypt


def decrypt(key):
    fernet = Fernet(key)
    # Opening the encrypted file
    with open("enc_message.txt", "rb") as enc_file:
        encrypted = enc_file.read()
    # Actually DECRYPTING the file
    decrypted = fernet.decrypt(encrypted)

    # Opening the file in write mode and
    # writing the decrypted data to a file
    with open("dec_message.txt", "wb") as dec_file:
        dec_file.write(decrypted)