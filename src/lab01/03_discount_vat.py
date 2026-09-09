price = int(input("Введите цену (₽): "))
discount = float(input("Введите скидку (%): "))
vat = float(input("Введите НДС (%): "))
base = price * (1 - discount / 100)
vat_amount = base * (vat / 100)
total = base + vat_amount
print(f'''База после скидки: {base} ₽
НДС: {vat_amount} ₽
Итого к оплате: {total} ₽''')

