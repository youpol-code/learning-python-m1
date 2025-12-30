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
- [x] **Day 2:** Lists & Data Structures 
- [x] **Day 2.1:** Lists & Loops (Feature: Smart Cart Logic) ✅
- [x] **Day 3:** Functions, Modules & Testing

## 💻 Code Example (Day 1: Type Hinting)
ตัวอย่างการเขียน Clean Code พร้อมระบุชนิดตัวแปร:
```python
product_name: str = "MacBook Pro M1"
price: float = 45000.00
quantity: int = 2

total: float = price * quantity
print(f"Total: {total:,.2f} THB")

## 🛒 Day 2: Lists & Data Structures
เรียนรู้การจัดการข้อมูลจำนวนมากผ่านโปรเจกต์ **Shopping Basket** (`basket.py`)

### 🧠 Key Concepts
- **List Indexing:** ข้อมูลเริ่มนับที่ `0`, และตัวสุดท้ายคือ `-1`
- **CRUD Operations:**
    - Create: `items = []`
    - Read: `items[0]`
    - Update: `items[0] = "New Value"`
    - Delete: `items.remove("Value")` หรือ `del items[0]`
- **Sorting:**
    - `sort()`: เรียงถาวร (เปลี่ยน Original List)
    - `sorted()`: เรียงชั่วคราว (Original List เหมือนเดิม)

### ⚠️ Critical Thinking Notes (Don't Forget!)
> **ASCII Trap:** ใน Python, ตัวอักษรพิมพ์ใหญ่ (A-Z) มาก่อนพิมพ์เล็ก (a-z) เสมอ
> เช่น `Zebra` จะถูกเรียงไว้ก่อน `apple` (Z < a)

> **Type Safety:** ห้ามใช้ `.sort()` กับ List ที่มีข้อมูลผสมกัน (`int` + `str`) เพราะจะเกิด `TypeError` ใน Python 3

### 💻 Code Snippet (List Management)
```python
products: list[str] = ["MacBook", "Mouse", "Adapter"]

# Adding & Removing
products.append("Keyboard")  # ต่อท้าย
products.remove("Mouse")     # ลบออก

# Sorting
products.sort()              # เรียง A-Z
print(f"Items: {len(products)}") # นับจำนวน## 🛒 Day 2: Lists & Data Structures
เรียนรู้การจัดการข้อมูลจำนวนมากผ่านโปรเจกต์ **Shopping Basket** (`basket.py`)

### 🧠 Key Concepts
- **List Indexing:** ข้อมูลเริ่มนับที่ `0`, และตัวสุดท้ายคือ `-1`
- **CRUD Operations:**
    - Create: `items = []`
    - Read: `items[0]`
    - Update: `items[0] = "New Value"`
    - Delete: `items.remove("Value")` หรือ `del items[0]`
- **Sorting:**
    - `sort()`: เรียงถาวร (เปลี่ยน Original List)
    - `sorted()`: เรียงชั่วคราว (Original List เหมือนเดิม)

### ⚠️ Critical Thinking Notes (Don't Forget!)
> **ASCII Trap:** ใน Python, ตัวอักษรพิมพ์ใหญ่ (A-Z) มาก่อนพิมพ์เล็ก (a-z) เสมอ
> เช่น `Zebra` จะถูกเรียงไว้ก่อน `apple` (Z < a)

> **Type Safety:** ห้ามใช้ `.sort()` กับ List ที่มีข้อมูลผสมกัน (`int` + `str`) เพราะจะเกิด `TypeError` ใน Python 3

### 💻 Code Snippet (List Management)
```python
products: list[str] = ["MacBook", "Mouse", "Adapter"]

# Adding & Removing
products.append("Keyboard")  # ต่อท้าย
products.remove("Mouse")     # ลบออก

# Sorting
products.sort()              # เรียง A-Z
print(f"Items: {len(products)}") # นับจำนวน## 🛒 Day 2: Lists & Data Structures
เรียนรู้การจัดการข้อมูลจำนวนมากผ่านโปรเจกต์ **Shopping Basket** (`basket.py`)

### 🧠 Key Concepts
- **List Indexing:** ข้อมูลเริ่มนับที่ `0`, และตัวสุดท้ายคือ `-1`
- **CRUD Operations:**
    - Create: `items = []`
    - Read: `items[0]`
    - Update: `items[0] = "New Value"`
    - Delete: `items.remove("Value")` หรือ `del items[0]`
- **Sorting:**
    - `sort()`: เรียงถาวร (เปลี่ยน Original List)
    - `sorted()`: เรียงชั่วคราว (Original List เหมือนเดิม)

### ⚠️ Critical Thinking Notes (Don't Forget!)
> **ASCII Trap:** ใน Python, ตัวอักษรพิมพ์ใหญ่ (A-Z) มาก่อนพิมพ์เล็ก (a-z) เสมอ
> เช่น `Zebra` จะถูกเรียงไว้ก่อน `apple` (Z < a)

> **Type Safety:** ห้ามใช้ `.sort()` กับ List ที่มีข้อมูลผสมกัน (`int` + `str`) เพราะจะเกิด `TypeError` ใน Python 3

### 💻 Code Snippet (List Management)
```python
products: list[str] = ["MacBook", "Mouse", "Adapter"]

# Adding & Removing
products.append("Keyboard")  # ต่อท้าย
products.remove("Mouse")     # ลบออก

# Sorting
products.sort()              # เรียง A-Z
print(f"Items: {len(products)}") # นับจำนวน## 🛒 Day 2: Lists & Data Structures
เรียนรู้การจัดการข้อมูลจำนวนมากผ่านโปรเจกต์ **Shopping Basket** (`basket.py`)

### 🧠 Key Concepts
- **List Indexing:** ข้อมูลเริ่มนับที่ `0`, และตัวสุดท้ายคือ `-1`
- **CRUD Operations:**
    - Create: `items = []`
    - Read: `items[0]`
    - Update: `items[0] = "New Value"`
    - Delete: `items.remove("Value")` หรือ `del items[0]`
- **Sorting:**
    - `sort()`: เรียงถาวร (เปลี่ยน Original List)
    - `sorted()`: เรียงชั่วคราว (Original List เหมือนเดิม)

### ⚠️ Critical Thinking Notes (Don't Forget!)
> **ASCII Trap:** ใน Python, ตัวอักษรพิมพ์ใหญ่ (A-Z) มาก่อนพิมพ์เล็ก (a-z) เสมอ
> เช่น `Zebra` จะถูกเรียงไว้ก่อน `apple` (Z < a)

> **Type Safety:** ห้ามใช้ `.sort()` กับ List ที่มีข้อมูลผสมกัน (`int` + `str`) เพราะจะเกิด `TypeError` ใน Python 3

### 💻 Code Snippet (List Management)
```python
products: list[str] = ["MacBook", "Mouse", "Adapter"]

# Adding & Removing
products.append("Keyboard")  # ต่อท้าย
products.remove("Mouse")     # ลบออก

# Sorting
products.sort()              # เรียง A-Z
print(f"Items: {len(products)}") # นับจำนวน## 🛒 Day 2: Lists & Data Structures
เรียนรู้การจัดการข้อมูลจำนวนมากผ่านโปรเจกต์ **Shopping Basket** (`basket.py`)

### 🧠 Key Concepts
- **List Indexing:** ข้อมูลเริ่มนับที่ `0`, และตัวสุดท้ายคือ `-1`
- **CRUD Operations:**
    - Create: `items = []`
    - Read: `items[0]`
    - Update: `items[0] = "New Value"`
    - Delete: `items.remove("Value")` หรือ `del items[0]`
- **Sorting:**
    - `sort()`: เรียงถาวร (เปลี่ยน Original List)
    - `sorted()`: เรียงชั่วคราว (Original List เหมือนเดิม)

### ⚠️ Critical Thinking Notes (Don't Forget!)
> **ASCII Trap:** ใน Python, ตัวอักษรพิมพ์ใหญ่ (A-Z) มาก่อนพิมพ์เล็ก (a-z) เสมอ
> เช่น `Zebra` จะถูกเรียงไว้ก่อน `apple` (Z < a)

> **Type Safety:** ห้ามใช้ `.sort()` กับ List ที่มีข้อมูลผสมกัน (`int` + `str`) เพราะจะเกิด `TypeError` ใน Python 3

### 💻 Code Snippet (List Management)
```python
products: list[str] = ["MacBook", "Mouse", "Adapter"]

# Adding & Removing
products.append("Keyboard")  # ต่อท้าย
products.remove("Mouse")     # ลบออก

# Sorting
products.sort()              # เรียง A-Z
print(f"Items: {len(products)}") # นับจำนวน## 🛒 Day 2: Lists & Data Structures
เรียนรู้การจัดการข้อมูลจำนวนมากผ่านโปรเจกต์ **Shopping Basket** (`basket.py`)

### 🧠 Key Concepts
- **List Indexing:** ข้อมูลเริ่มนับที่ `0`, และตัวสุดท้ายคือ `-1`
- **CRUD Operations:**
    - Create: `items = []`
    - Read: `items[0]`
    - Update: `items[0] = "New Value"`
    - Delete: `items.remove("Value")` หรือ `del items[0]`
- **Sorting:**
    - `sort()`: เรียงถาวร (เปลี่ยน Original List)
    - `sorted()`: เรียงชั่วคราว (Original List เหมือนเดิม)

### ⚠️ Critical Thinking Notes (Don't Forget!)
> **ASCII Trap:** ใน Python, ตัวอักษรพิมพ์ใหญ่ (A-Z) มาก่อนพิมพ์เล็ก (a-z) เสมอ
> เช่น `Zebra` จะถูกเรียงไว้ก่อน `apple` (Z < a)

> **Type Safety:** ห้ามใช้ `.sort()` กับ List ที่มีข้อมูลผสมกัน (`int` + `str`) เพราะจะเกิด `TypeError` ใน Python 3

### 💻 Code Snippet (List Management)
```python
products: list[str] = ["MacBook", "Mouse", "Adapter"]

# Adding & Removing
products.append("Keyboard")  # ต่อท้าย
products.remove("Mouse")     # ลบออก

# Sorting
products.sort()              # เรียง A-Z
print(f"Items: {len(products)}") # นับจำนวน## 🛒 Day 2: Lists & Data Structures
เรียนรู้การจัดการข้อมูลจำนวนมากผ่านโปรเจกต์ **Shopping Basket** (`basket.py`)

### 🧠 Key Concepts
- **List Indexing:** ข้อมูลเริ่มนับที่ `0`, และตัวสุดท้ายคือ `-1`
- **CRUD Operations:**
    - Create: `items = []`
    - Read: `items[0]`
    - Update: `items[0] = "New Value"`
    - Delete: `items.remove("Value")` หรือ `del items[0]`
- **Sorting:**
    - `sort()`: เรียงถาวร (เปลี่ยน Original List)
    - `sorted()`: เรียงชั่วคราว (Original List เหมือนเดิม)

### ⚠️ Critical Thinking Notes (Don't Forget!)
> **ASCII Trap:** ใน Python, ตัวอักษรพิมพ์ใหญ่ (A-Z) มาก่อนพิมพ์เล็ก (a-z) เสมอ
> เช่น `Zebra` จะถูกเรียงไว้ก่อน `apple` (Z < a)

> **Type Safety:** ห้ามใช้ `.sort()` กับ List ที่มีข้อมูลผสมกัน (`int` + `str`) เพราะจะเกิด `TypeError` ใน Python 3

### 💻 Code Snippet (List Management)
```python
products: list[str] = ["MacBook", "Mouse", "Adapter"]

# Adding & Removing
products.append("Keyboard")  # ต่อท้าย
products.remove("Mouse")     # ลบออก

# Sorting
products.sort()              # เรียง A-Z
print(f"Items: {len(products)}") # นับจำนวน## 🛒 Day 2: Lists & Data Structures
เรียนรู้การจัดการข้อมูลจำนวนมากผ่านโปรเจกต์ **Shopping Basket** (`basket.py`)

### 🧠 Key Concepts
- **List Indexing:** ข้อมูลเริ่มนับที่ `0`, และตัวสุดท้ายคือ `-1`
- **CRUD Operations:**
    - Create: `items = []`
    - Read: `items[0]`
    - Update: `items[0] = "New Value"`
    - Delete: `items.remove("Value")` หรือ `del items[0]`
- **Sorting:**
    - `sort()`: เรียงถาวร (เปลี่ยน Original List)
    - `sorted()`: เรียงชั่วคราว (Original List เหมือนเดิม)

### ⚠️ Critical Thinking Notes (Don't Forget!)
> **ASCII Trap:** ใน Python, ตัวอักษรพิมพ์ใหญ่ (A-Z) มาก่อนพิมพ์เล็ก (a-z) เสมอ
> เช่น `Zebra` จะถูกเรียงไว้ก่อน `apple` (Z < a)

> **Type Safety:** ห้ามใช้ `.sort()` กับ List ที่มีข้อมูลผสมกัน (`int` + `str`) เพราะจะเกิด `TypeError` ใน Python 3

### 💻 Code Snippet (List Management)
```python
products: list[str] = ["MacBook", "Mouse", "Adapter"]

# Adding & Removing
products.append("Keyboard")  # ต่อท้าย
products.remove("Mouse")     # ลบออก

# Sorting
products.sort()              # เรียง A-Z
print(f"Items: {len(products)}") # นับจำนวน## 🛒 Day 2: Lists & Data Structures
เรียนรู้การจัดการข้อมูลจำนวนมากผ่านโปรเจกต์ **Shopping Basket** (`basket.py`)

### 🧠 Key Concepts
- **List Indexing:** ข้อมูลเริ่มนับที่ `0`, และตัวสุดท้ายคือ `-1`
- **CRUD Operations:**
    - Create: `items = []`
    - Read: `items[0]`
    - Update: `items[0] = "New Value"`
    - Delete: `items.remove("Value")` หรือ `del items[0]`
- **Sorting:**
    - `sort()`: เรียงถาวร (เปลี่ยน Original List)
    - `sorted()`: เรียงชั่วคราว (Original List เหมือนเดิม)

### ⚠️ Critical Thinking Notes (Don't Forget!)
> **ASCII Trap:** ใน Python, ตัวอักษรพิมพ์ใหญ่ (A-Z) มาก่อนพิมพ์เล็ก (a-z) เสมอ
> เช่น `Zebra` จะถูกเรียงไว้ก่อน `apple` (Z < a)

> **Type Safety:** ห้ามใช้ `.sort()` กับ List ที่มีข้อมูลผสมกัน (`int` + `str`) เพราะจะเกิด `TypeError` ใน Python 3

### 💻 Code Snippet (List Management)
```python
products: list[str] = ["MacBook", "Mouse", "Adapter"]

# Adding & Removing
products.append("Keyboard")  # ต่อท้าย
products.remove("Mouse")     # ลบออก

# Sorting
products.sort()              # เรียง A-Z
print(f"Items: {len(products)}") # นับจำนวน## 🛒 Day 2: Lists & Data Structures
เรียนรู้การจัดการข้อมูลจำนวนมากผ่านโปรเจกต์ **Shopping Basket** (`basket.py`)

### 🧠 Key Concepts
- **List Indexing:** ข้อมูลเริ่มนับที่ `0`, และตัวสุดท้ายคือ `-1`
- **CRUD Operations:**
    - Create: `items = []`
    - Read: `items[0]`
    - Update: `items[0] = "New Value"`
    - Delete: `items.remove("Value")` หรือ `del items[0]`
- **Sorting:**
    - `sort()`: เรียงถาวร (เปลี่ยน Original List)
    - `sorted()`: เรียงชั่วคราว (Original List เหมือนเดิม)

### ⚠️ Critical Thinking Notes (Don't Forget!)
> **ASCII Trap:** ใน Python, ตัวอักษรพิมพ์ใหญ่ (A-Z) มาก่อนพิมพ์เล็ก (a-z) เสมอ
> เช่น `Zebra` จะถูกเรียงไว้ก่อน `apple` (Z < a)

> **Type Safety:** ห้ามใช้ `.sort()` กับ List ที่มีข้อมูลผสมกัน (`int` + `str`) เพราะจะเกิด `TypeError` ใน Python 3

### 💻 Code Snippet (List Management)
```python
products: list[str] = ["MacBook", "Mouse", "Adapter"]

# Adding & Removing
products.append("Keyboard")  # ต่อท้าย
products.remove("Mouse")     # ลบออก

# Sorting
products.sort()              # เรียง A-Z
print(f"Items: {len(products)}") # นับจำนวน## 🛒 Day 2: Lists & Data Structures
เรียนรู้การจัดการข้อมูลจำนวนมากผ่านโปรเจกต์ **Shopping Basket** (`basket.py`)

### 🧠 Key Concepts
- **List Indexing:** ข้อมูลเริ่มนับที่ `0`, และตัวสุดท้ายคือ `-1`
- **CRUD Operations:**
    - Create: `items = []`
    - Read: `items[0]`
    - Update: `items[0] = "New Value"`
    - Delete: `items.remove("Value")` หรือ `del items[0]`
- **Sorting:**
    - `sort()`: เรียงถาวร (เปลี่ยน Original List)
    - `sorted()`: เรียงชั่วคราว (Original List เหมือนเดิม)

### ⚠️ Critical Thinking Notes (Don't Forget!)
> **ASCII Trap:** ใน Python, ตัวอักษรพิมพ์ใหญ่ (A-Z) มาก่อนพิมพ์เล็ก (a-z) เสมอ
> เช่น `Zebra` จะถูกเรียงไว้ก่อน `apple` (Z < a)

> **Type Safety:** ห้ามใช้ `.sort()` กับ List ที่มีข้อมูลผสมกัน (`int` + `str`) เพราะจะเกิด `TypeError` ใน Python 3

### 💻 Code Snippet (List Management)
```python
products: list[str] = ["MacBook", "Mouse", "Adapter"]

# Adding & Removing
products.append("Keyboard")  # ต่อท้าย
products.remove("Mouse")     # ลบออก

# Sorting
products.sort()              # เรียง A-Z
print(f"Items: {len(products)}") # นับจำนวน## 🛒 Day 2: Lists & Data Structures
เรียนรู้การจัดการข้อมูลจำนวนมากผ่านโปรเจกต์ **Shopping Basket** (`basket.py`)

### 🧠 Key Concepts
- **List Indexing:** ข้อมูลเริ่มนับที่ `0`, และตัวสุดท้ายคือ `-1`
- **CRUD Operations:**
    - Create: `items = []`
    - Read: `items[0]`
    - Update: `items[0] = "New Value"`
    - Delete: `items.remove("Value")` หรือ `del items[0]`
- **Sorting:**
    - `sort()`: เรียงถาวร (เปลี่ยน Original List)
    - `sorted()`: เรียงชั่วคราว (Original List เหมือนเดิม)

### ⚠️ Critical Thinking Notes (Don't Forget!)
> **ASCII Trap:** ใน Python, ตัวอักษรพิมพ์ใหญ่ (A-Z) มาก่อนพิมพ์เล็ก (a-z) เสมอ
> เช่น `Zebra` จะถูกเรียงไว้ก่อน `apple` (Z < a)

> **Type Safety:** ห้ามใช้ `.sort()` กับ List ที่มีข้อมูลผสมกัน (`int` + `str`) เพราะจะเกิด `TypeError` ใน Python 3

### 💻 Code Snippet (List Management)
```python
products: list[str] = ["MacBook", "Mouse", "Adapter"]

# Adding & Removing
products.append("Keyboard")  # ต่อท้าย
products.remove("Mouse")     # ลบออก

# Sorting
products.sort()              # เรียง A-Z
print(f"Items: {len(products)}") # นับจำนวน

## 💻 Code Example (Lesson 2: Logic)
ตัวอย่างการใช้ Loop และ If-Else ใน `smart_cart.py`:
```python
# Loop บวกราคาสินค้า
for price in cart_prices:
    total_cost += price

# เช็คเงื่อนไขงบประมาณ
if user_budget >= net_price:
    print("✅ Purchase Success")
else:
    print("❌ Insufficient Funds")


## 🚀 Day 3: Functions, Modules & Testing
**Status:** Completed ✅

### 📝 สิ่งที่เรียนรู้
1.  **Functions:** แยก Logic การคำนวณออกจากหน้าบ้าน (`def`) เพื่อลดโค้ดซ้ำซ้อน
2.  **Modules:** จัดระเบียบไฟล์โดยแยก `cart_utils.py` (สูตร) ออกจาก `smart_cart.py` (หน้าบ้าน)
3.  **Automated Testing:** เริ่มใช้ `pytest` เขียน Test Case เพื่อตรวจสอบความถูกต้องของ Logic โดยอัตโนมัติ

### 🧪 Code Example (Testing)
ตัวอย่างการเขียน Test เพื่อตรวจสอบส่วนลด:
```python
def test_discount_over_30k():
    # ถ้าซื้อ 50,000 ต้องลด 10% (5,000)
    assert calculate_discount(50000) == 5000