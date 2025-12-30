def calculate_total(price_list: list[float]) -> float:
    """
    คำนวณราคารวมสินค้าในตะกร้า
    """
    total = 0.0
    for price in price_list:
        total += price
    return total

def calculate_discount(total_amount: float) -> float:
    """
    คำนวณส่วนลด: ซื้อเกิน 30,000 ลด 10%, ถ้าน้อยกว่านั้นไม่ลด
    """
    if total_amount > 30000:
        return total_amount * 0.10
    return 0.0