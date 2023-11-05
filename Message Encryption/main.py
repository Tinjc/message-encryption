
from generate_key import give_key
from encrypt_message import encrypt
from decrypt_message import decrypt

if __name__ == '__main__':

    print("Welcome to the encryption terminal.")
    print("You can encrypt or decrypt messages.")


    service = input("What do you need to do?\n")
    if service.lower() == "encrypt":
        print("You choose encryption!")

        with open("message.txt", "wb") as filename:
            message = input("What message do you need encrypting").encode()
            filename.write(message)

        print("You need a key to encrypt!")
        key = give_key()
        encrypt(message)

    elif service.lower() == "decrypt":
        print("You choose decryption!")
        with open("id.key", "rb") as filename:
            key = filename.read()
        decrypt(key)
    else:
        print("Not a valid command!")