from password import generate_password
from password import clear
from check import check_for_update

length = input("Custom length (Enter for 16): ").strip()
try:
    length = int(length)
    if length <= 0:
        length = 16
except ValueError:  
    length = 16

amount = input("Custom amount (Enter for 1): ").strip()
try:
    amount = int(amount)
    if amount <= 0:
        amount = 1
except ValueError:
    amount = 1
clear()
print("generated",amount,"passwords: ")
for i in range(amount):
 custom_password = generate_password(length)
 print(custom_password)

input("Press Enter to exit...")