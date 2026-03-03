# receipt_parser.py

import re

# Чтение текста чека из файла
with open("raw.txt", "r", encoding="utf-8") as f:
    receipt_text = f.read()

# 1. Извлечение товаров
item_pattern = re.compile(
    r'\d+\.\n'                      # номер позиции
    r'(.+?)\n'                      # название товара
    r'([\d,]+)\s*x\s*([\d,]+)\n'    # количество и цена за единицу
    r'([\d,]+)',                     # итоговая стоимость
    re.DOTALL
)

items = []
for match in item_pattern.findall(receipt_text):
    name = match[0].strip()
    quantity = float(match[1].replace(',', '.'))
    unit_price = float(match[2].replace(',', '.'))
    total_price = float(match[3].replace(',', '.'))
    items.append({
        'name': name,
        'quantity': quantity,
        'unit_price': unit_price,
        'total_price': total_price
    })

# 2. Извлечение итоговой суммы
total_pattern = re.search(r'ИТОГО:\s*([\d\s,]+)', receipt_text)
total_sum = None
if total_pattern:
    total_sum = float(total_pattern.group(1).replace(' ', '').replace(',', '.'))

# 3. Вывод результата
print("Товары:")
for item in items:
    print(item)

print(f"\nИТОГО: {total_sum}")

