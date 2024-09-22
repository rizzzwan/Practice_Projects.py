from cryptography.fernet import Fernet
import os

def load_key():
    with open("key.key", "rb") as key_file:
        return key_file.read()  

def set_master_password():
    mas_pwd = input("Enter a MASTER password: ")
    with open("master_password.txt", 'w') as f:
        f.write(mas_pwd)  # Store the master password (should ideally be hashed)

def get_master_password():
    with open("master_password.txt", 'r') as f:
        return f.read().strip()  # Use strip() to remove any trailing newline

def view():
    mas_pwd_input = input("Enter your MASTER password to access passwords: ")
    # Compare plain text password instead of encoded version
    if mas_pwd_input == get_master_password():  
        with open("passwords.txt", 'r') as f:
            for line in f.readlines():
                data = line.rstrip()
                user, paswd = data.split(" / ")
                print("User:", user, ", Password:", fer.decrypt(paswd.encode()).decode())
    else:
        print("Invalid master password. Access denied.")

def add():
    name = input("Enter Account: ")
    pwd = input("Enter Password: ")

    with open("passwords.txt", 'a') as f:
        f.write(name + " / " + fer.encrypt(pwd.encode()).decode() + "\n")

if not os.path.exists("master_password.txt"):
    set_master_password()

key = load_key() 
fer = Fernet(key)  

while True:
    mode = input("Would you like to add a new password or view existing ones? (View/Add). Press q to quit? ").lower()
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
