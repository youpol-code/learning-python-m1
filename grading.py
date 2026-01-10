student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

# 1. สร้าง Dict เปล่าๆ ชื่อ student_grades
student_grades = {}

# 2. เขียน Loop วน student_scores
#    - เช็คคะแนน (value) ของแต่ละคน
#    - กำหนดเกรด แล้วใส่ลงใน student_grades [key] = "Grade"

# --- พื้นที่เขียนโค้ดของคุณ ---
for key_student in student_scores:
    grade_num : int = student_scores[key_student]
    grade : str = ""
    if 91 <= grade_num <=100:
        grade = "Outstanding"
    elif 81 <= grade_num <=90:
        grade = "Exceeds Expectations"
    elif 71 <= grade_num <= 80:
        grade = "Acceptable"
    else:
        grade = "Fail"

    student_grades[key_student] =grade

# ---------------------------

print(student_grades)