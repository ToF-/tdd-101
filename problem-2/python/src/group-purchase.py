import csv
import sys

if len(sys.argv) < 3:
    print("usage: python3 group-purchase <input-orders.csv> <output-purchase.csv>")
    exit()

input_file_path = sys.argv[1]
output_file_path = sys.argv[2]

purchases = dict()
total = 0.0
orders_shipping = 0.0
orders_total = 0.0
orders_grand_total = 0.0

with open(input_file_path, mode = 'r', newline = '') as file:
    reader = csv.DictReader(file, delimiter = ',')
    for row in reader:
        label = row['label'].strip()
        amount = float(row['total'])
        if label.startswith('~'):
            if label == '~ total':
                orders_total = amount
            elif label == '~ shipping':
                orders_shipping = amount
            elif label == '~ grand total':
                orders_grand_total = amount
        else:
            buyer = row['buyer'].strip()
            if not buyer in purchases:
                purchases[buyer] = 0.0
            purchases[buyer] = purchases[buyer] + amount
            orders_total = orders_total + amount


total = 0.0
with open(output_file_path, mode = 'w', newline = '') as file:
    fieldnames = ['buyer','amount','shipping','total']
    writer = csv.DictWriter(file, delimiter = ',', fieldnames = fieldnames)
    writer.writeheader()
    total_amount = 0.0
    total_shipping = 0.0
    grand_total = 0.0
    for buyer, amount in purchases.items():
        shipping = round((amount / orders_total) * orders_shipping, 2)
        total = amount + shipping
        writer.writerow({'buyer': buyer, 'amount': amount, 'shipping': shipping, 'total': total})
        total_amount = total_amount + amount
        total_shipping = total_shipping + shipping
        grand_total = grand_total + total
    writer.writerow({'buyer': '~ total', 'amount': round(total_amount, 2), 'shipping': round(total_shipping,2), 'total': round(grand_total,2)})


