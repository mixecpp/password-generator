import os
import secrets
import string

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def generate_password(length=16):
    characters = string.ascii_letters + string.digits + "@!_*"
    password = "".join(secrets.choice(characters) for _ in range(length))
    return password