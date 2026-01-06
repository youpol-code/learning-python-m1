
from typing import List

# ข้อมูลตั้งต้น
student_heights : List[int] = [180,124,165,173,189,169,146]

# ตัวแปรสำหรับเก็บผลรวม (สะสมค่า)
total_height : float = 0
# ตัวแปรสำหรับนับจำนวนคน
number_of_students : float = 0

# --- พื้นที่เขียนโค้ดของคุณ ---
# 1. เขียน for loop วนลูป student_heights
# 2. ในแต่ละรอบ ให้เอาความสูงบวกเข้าไปใน total_height
# 3. ในแต่ละรอบ ให้นับจำนวนคนเพิ่มทีละ 1 ใส่ใน number_of_students
# ---------------------------

for student in student_heights:
    total_height += student
    number_of_students += 1

average_height : float = total_height / number_of_students

print(f"ผลรวมความสูง : {total_height}")
print(f"จำนวนนักเรืยน : {number_of_students}")
print(f"ความสูงเฉลี่ย : {average_height:.2f}")



