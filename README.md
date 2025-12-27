# 📘 Learning Python Full Stack (M1 Edition)

โปรเจกต์สำหรับเรียนรู้ Python ตั้งแต่ศูนย์จนถึงระดับ Pro (The Thinking Developer Path)
> **Note:** รันบนสภาพแวดล้อม Mac M1 (Apple Silicon) ด้วย `uv` package manager

## 🛠 Tech Stack
| Category | Tool | Description |
| :--- | :--- | :--- |
| Language | Python 3.x | Modern syntax with Type Hinting |
| Dev Tool | VS Code | With Black Formatter & Pylance |
| Version Control | Git | Branching & Merging workflow |
| Package Manager | uv | Ultra-fast Python package installer |

## 📚 Course Progress
- [x] **Day 1:** Syntax, Variables, f-string (`receipt.py`)
- [x] **Day 1:** Lists & Basic Data Structures (`basket.py`)
- [ ] **Day 2:** Loops & Logic (Next Step)
- [ ] **Day 3:** Functions & Modules

## 💻 Code Example (Day 1: Type Hinting)
ตัวอย่างการเขียน Clean Code พร้อมระบุชนิดตัวแปร:
```python
product_name: str = "MacBook Pro M1"
price: float = 45000.00
quantity: int = 2

total: float = price * quantity
print(f"Total: {total:,.2f} THB")