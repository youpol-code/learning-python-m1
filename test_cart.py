from cart_utils import calculate_total,calculate_discount

def test_calculate_total_correctly():
    # ลองส่งของราคา 100, 200, 300 ไปรวมกัน
    prices = [100.00,200.00,300.00]
    result = calculate_total(prices)
    # ผลลัพธ์ต้องได้ 600 เป๊ะๆ
    assert result == 600.0

def test_discount_over_30k():
    # ลองส่งยอด 50,000 ไป (ต้องลด 10% คือ 5,000)
    assert calculate_discount(50000) == 5000

def test_discount_under_30k():
    # ลองส่งยอด 10,000 ไป (ต้องไม่ลดเลย คือ 0)
    assert calculate_discount(10000) == 0