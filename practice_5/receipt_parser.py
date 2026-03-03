import re
import json

def parse_receipt(text):
    # 1️⃣ Extract all prices (e.g., 12.99, 5, 100.50)
    price_pattern = r'\b\d+(?:\.\d{1,2})?\b'
    prices = [float(p) for p in re.findall(price_pattern, text)]
    
    # 2️⃣ Extract product names (assume product names are words before prices)
    # This pattern finds words/phrases preceding a price
    product_pattern = r'([A-Za-z0-9\s]+?)\s+\d+(?:\.\d{1,2})?\b'
    products = [p.strip() for p in re.findall(product_pattern, text)]
    
    # 3️⃣ Calculate total amount
    total_amount = sum(prices)
    
    # 4️⃣ Extract date and time (common formats: dd/mm/yyyy, yyyy-mm-dd, hh:mm)
    date_pattern = r'\b\d{1,2}[/-]\d{1,2}[/-]\d{2,4}\b'
    time_pattern = r'\b\d{1,2}:\d{2}(?:\s?[APMapm]{2})?\b'
    dates = re.findall(date_pattern, text)
    times = re.findall(time_pattern, text)
    
    # 5️⃣ Find payment method (common keywords)
    payment_methods = ["cash", "credit card", "debit card", "visa", "mastercard", "paypal"]
    payment_pattern = r'\b(?:' + '|'.join(payment_methods) + r')\b'
    payment_match = re.search(payment_pattern, text, re.IGNORECASE)
    payment_method = payment_match.group(0) if payment_match else None
    
    # 6️⃣ Structured output
    parsed_data = {
        "products": products,
        "prices": prices,
        "total_amount": total_amount,
        "date": dates[0] if dates else None,
        "time": times[0] if times else None,
        "payment_method": payment_method
    }
    
    return parsed_data


# Example usage
if __name__ == "__main__":
    receipt_text = """
    Grocery Store
    Date: 03/03/2026 Time: 14:25
    Milk 2.50
    Bread 1.75
    Eggs 3.20
    Total 7.45
    Payment Method: Credit Card
    """
    
    parsed_receipt = parse_receipt(receipt_text)
    
    print(json.dumps(parsed_receipt, indent=4))