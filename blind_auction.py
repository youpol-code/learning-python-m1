# blind_auction.py

print("Welcome to the secret auction program.")

bids = {}
bidding_finished : bool = False

def find_highest_bidder(bidding_record : dict):
    highest_bid = 0
    winner = ""
    # bidding_record หน้าตาแบบนี้: {"Angela": 123, "James": 321}
    
    # --- โจทย์ของคุณ: เขียน Loop หาคนชนะ ---
    # 1. วนลูป bidding_record
    # 2. เอาค่าราคา (bid_amount) ออกมา
    # 3. เทียบว่า bid_amount > highest_bid หรือไม่?
    # 4. ถ้าจริง ให้ update ค่า highest_bid และ winner
    # ------------------------------------
    for key in bidding_record:
        if bidding_record[key] > highest_bid:
            highest_bid = bidding_record[key]
            winner = key
            
    print(f"The winner is {winner} with a bid of ${highest_bid}")

while not bidding_finished:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    
    # 1. เอา name กับ price ใส่ลงใน bids dictionary
    bids[name] = price
    
    # 2. ถามว่าจะไปต่อไหม
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    
    if should_continue == "no":
        bidding_finished = True
        find_highest_bidder(bids)
    elif should_continue == "yes":
        # พิมพ์ขึ้นบรรทัดใหม่เยอะๆ เพื่อหลอกว่าเคลียร์หน้าจอ (คนต่อไปจะได้ไม่เห็นราคา)
        print("\n" * 20)