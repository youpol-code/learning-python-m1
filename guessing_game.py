import random 

def guessing_game() -> None:
    answer = random.randint(1,100)

    guess : int = -1
    guess_count : int = 0
    while guess !=answer:
        # รับค่า input (อย่าลืมแปลงเป็น int)
        # เช็ค if / elif / else
        #    - ถ้า guess < answer -> print "Too low"
        #    - ถ้า guess > answer -> print "Too high"
        #    - ถ้าเท่ากัน -> print "Just right!"
        guess_count +=1
        guess = int(input("Please guess number 1-100 :"))
        if guess < answer: 
            print("Too low")
        elif guess > answer:
            print("Too high")
        else:
            print("Just right!")
            print(f"You guest time {guess_count:,}")
            break
        
        

# เรียกใช้งานฟังก์ชัน
guessing_game()