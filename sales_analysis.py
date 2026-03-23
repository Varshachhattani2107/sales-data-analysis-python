import csv

total_sales = 0
sales_data = []

with open("sales_data.csv", "r") as file:
    reader = csv.DictReader(file)
    
    for row in reader:
        sale = int(row["Sales"])
        total_sales += sale
        sales_data.append(sale)

# Average Sales
average_sales = total_sales / len(sales_data)

# Highest & Lowest
max_sale = max(sales_data)
min_sale = min(sales_data)

print("Total Sales:", total_sales)
print("Average Sales:", average_sales)
print("Highest Sale:", max_sale)
print("Lowest Sale:", min_sale)
