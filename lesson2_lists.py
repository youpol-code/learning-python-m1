"""
Workshop 2: Python Lists & Loops
Topic: การจัดการข้อมูลชุด (Lists) และการวนซ้ำ (Loops) แบบ Clean Code
Author: Your Name
Repository: learning-python-m1
"""

import datetime

def calculate_age(birth_year: int) ->int:
    """
    ฟังก์ชันคำนวณอายุจากปีเกิด
    Args:
        birth_year (int): ปีเกิด (ค.ศ.)
    Returns:
        int: อายุปัจจุบัน
    """
    current_year = datetime.datetime.now().year
    return current_year - birth_year

def analyze_team_ages(birth_years: list[int]) -> None:
    """
    ฟังก์ชันวิเคราะห์อายุของคนในทีม (Automation Loop)
    Args:
        birth_years (list[int]): รายการปีเกิดของพนักงาน
    """
    print(f"📊 เริ่มต้นวิเคราะห์ข้อมูลพนักงานจำนวน {len(birth_years)} คน...\n")
    # Loop: ดึงปีเกิดออกมาทีละคน แล้วคำนวณทันที
    for year in birth_years:
        age = calculate_age(year)

        # Logic: จำแนกรุ่น (Generation)
        gen = "Gen Z" if year >= 1997 else "Gen Y/X"

        # Display: แสดงผลแบบ Real-time
        print(f" -> เกิดปี {year} : อายุ {age} ปี ({gen})")

    print("\n✅ การวิเคราะห์เสร็จสมบูรณ์")

if __name__=="__main__":
    print("--- 🟢 Lesson 2: Lists & Loops ---")

    # 1. สร้าง List (กล่องเก็บข้อมูลหลายตัว)
    team_years: list[int] =[1990,1995,2000,1985,2005]

    # 2. ส่งข้อมูลเข้าฟังก์ชันประมวลผล
    analyze_team_ages(team_years)