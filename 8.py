#  Product Inventory Management
# Calculate the total stock value of each product using Stock Value = Quantity × Price. Also display products whose quantity
# is below 10.
# inventory = {
#  "P101": {"name": "Laptop", "quantity": 5, "price": 45000},
#  "P102": {"name": "Mouse", "quantity": 20, "price": 500},
#  "P103": {"name": "Keyboard", "quantity": 8, "price": 1200},
#  "P104": {"name": "Monitor", "quantity": 12, "price": 10000}
# }
# Expected output:
# Laptop: 225000
# Mouse: 10000
# Keyboard: 9600
# Monitor: 120000
# Low Stock Products:
# Laptop
# Keyboard

inventory = {
  "P101": {"name": "Laptop", "quantity": 5, "price": 45000},
  "P102": {"name": "Mouse", "quantity": 20, "price": 500},
  "P103": {"name": "Keyboard", "quantity": 8, "price": 1200},
  "P104": {"name": "Monitor", "quantity": 12, "price": 10000}
 }

total_stock=0
for i in inventory:
    total_stock=inventory[i]["quantity"]*inventory[i]["price"]
    name=inventory[i]["name"]
    print(f"{name}: {total_stock}")

for j in inventory:
      
   if inventory[j]["quantity"]<10:
        print(f"low stock: {inventory[j]["name"]}")