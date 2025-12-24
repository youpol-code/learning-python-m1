"""
Module: Age Utilities
หน้าที่: เก็บฟังก์ชันคำนวณเกี่ยวกับอายุ (แยกออกมาเพื่อให้เรียกใช้ซ้ำได้ง่าย)
"""

import datetime

def get_current_year() ->int:
    """ดึงปีปัจจุบัน (ค.ศ.)"""
    return datetime.datetime.now().year

def calculate_age(birth_year: int) -> int:
    """
    คำนวณอายุ
    Args:
        birth_year (int): ปีเกิด
    Returns:
        int: อายุ
    """
    return get_current_year() - birth_year

def check_generation(birth_year:int) ->str:
    """ตรวจสอบ Generation"""
    if birth_year >= 2010:
        return "Gen Alpha"
    elif birth_year >= 1997:
        return "Gen Z"
    elif birth_year >= 1981:
        return "Gen Y (Millennials)"
    else:
        return "Gen X / Boomer"

