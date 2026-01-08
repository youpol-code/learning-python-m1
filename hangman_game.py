# hangman_game.py
import random
from hangman_words import word_list
from hangman_art import stages, logo

# 1. Setup เกม
print(logo)
chosen_word : str = random.choice(word_list)
word_length : int = len(chosen_word)

end_of_game : bool = False
lives : int = 6

# สร้าง List เก็บช่องว่าง เช่น ['_', '_', '_']
display = []
for _ in range(word_length):
    display.append("_")

print(f"Pssst, the solution is {chosen_word}.") # (เอาไว้แอบดูตอนเทส)

# 2. เริ่มวนลูปเกม
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    # --- ส่วนที่คุณต้องเขียน Logic ---
    
    # Check 1: วนลูปเช็คตัวอักษรใน chosen_word ทีละตัว
    # ถ้าตัวอักษรตรงกับ guess ให้เอา guess ไปใส่ใน display ที่ตำแหน่งเดียวกัน
    # Hint: ใช้ for loop คู่กับ enumerate หรือ range(word_length) ก็ได้
    
    # Check 2: ถ้า guess ไม่อยู่ใน chosen_word
    # ให้ลด lives ลง 1
    # และถ้า lives เหลือ 0 ให้จบเกม (end_of_game = True) แล้วบอกว่า "You lose."
    if guess in chosen_word:
         for position in range(word_length):
             letter = chosen_word[position]
             if letter == guess:
                 display[position] = letter
    else:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
    # -------------------------------

    # Join list ให้เป็น string เพื่อปริ้นท์สวยๆ เช่น "p _ t _ o n"
    print(f"{' '.join(display)}")

    # Check 3: เช็คว่าชนะหรือยัง? (ถ้าไม่มี "_" เหลือใน display แล้ว)
    if "_" not in display:
        end_of_game = True
        print("You win! 🎉")
    
    # Check 4: ถ้าแพ้ (Logic lives == 0 อยู่ข้างบนแล้ว)
    if lives == 0:
        end_of_game = True
        print("You lose. 💀")
        print(f"The word was: {chosen_word}")

    # ปริ้นท์รูปคนแขวนคอ (stages) โดยใช้ index จาก lives
    print(stages[lives])