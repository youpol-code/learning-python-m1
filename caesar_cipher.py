# Fix 1: เบิ้ล list เพื่อรองรับการ shift เกิน z
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# Fix 2: ใช้ Modulo (%) เพื่อกันกรณี user ใส่ shift มาเป็นล้าน (เช่น shift 100)
# 100 % 26 = เศษ 22 (มันจะวนรอบให้เองอัตโนมัติ)
shift = shift % 26 

def caesar(start_text: str, shift_amount: int, cipher_direction: str):
    end_text = ""
    for letter in start_text:
        
        # Fix 3: เช็คก่อนว่าตัวอักษรมีใน list ไหม? (จัดการ space และ symbols)
        if letter in alphabet:
            position = alphabet.index(letter)
            if cipher_direction == "encode":
                new_position = position + shift_amount
            elif cipher_direction == "decode":
                new_position = position - shift_amount
            new_letter = alphabet[new_position]
            end_text += new_letter
        else:
            # ถ้าไม่ใช่ a-z (เช่น space) ให้ใส่ตัวเดิมลงไปเลย
            end_text += letter
            
    print(f"The {cipher_direction}d text is {end_text}")

caesar(start_text=text, shift_amount=shift, cipher_direction=direction)