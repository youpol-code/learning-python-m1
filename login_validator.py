def check_login(username:str,password:str) -> bool:
    # นี่คือส่วน Decision Making (อ้างอิง Python Automation บทที่ 3)
    if username=="admin" and password=="1234":
        return True
    else:
        return False

# --- ส่วนทดสอบการทำงาน (จำลอง User กรอกข้อมูล) ---
print("-- โปรแกรมเข้าสู่ระบบ (จำลอง) ---")
user_input: str = input("Username: ")
pass_input: str = input("Password: ")

# เรียกใช้ฟังก์ชันตรวจสอบ
if check_login(user_input,pass_input):
    print("✅ Access Granted: ยินดีต้อนรับเข้าสู่ระบบ!")
    # ในอนาคต ตรงนี้คือโค้ดเปิดหน้าต่างใหม่ของ Tkinter
else:
    print("❌ Access Denied: ข้อมูลไม่ถูกต้อง")
    # ในอนาคต ตรงนี้คือโค้ดขึ้นแจ้งเตือน messageBox.showerror ใน Tkinter