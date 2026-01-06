import random
from typing import List  


letters : List[str] = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers : List[str] = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols : List[str] = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters : int = int(input("How many letters would you like in your password?\n")) 
nr_symbols : int = int(input(f"How many symbols would you like?\n"))
nr_numbers : int = int(input(f"How many numbers would you like?\n"))

# --- พื้นที่เขียนโค้ดของคุณ ---
# แนวทาง:
# 1. สร้างตัวแปร password เป็น string ว่างๆ หรือ list ว่างๆ
# 2. ใช้ Loop 3 ครั้ง (Loop ตัวอักษร, Loop สัญลักษณ์, Loop ตัวเลข)
# 3. ในแต่ละ Loop ให้สุ่มหยิบของ (random.choice) แล้วเอามาต่อใน password
# ---------------------------

password : List[str]=[]

for number in range(1,nr_letters +1):
    password.append(random.choice(letters))

for number in range(1,nr_numbers +1):
    password.append(random.choice(numbers))

for number in range(1,nr_symbols +1):
    password.append(random.choice(symbols))

random.shuffle(password)

print(f"password random : {''.join(password)}")
