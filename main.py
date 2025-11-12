
inventory = {
    "Laptop": 10,
    "Smartphone": 25,
    "Tablet": 15,
    "Headphones": 30,
    "Smartwatch": 20
}

inventory.update({"Smartphone": inventory["Smartphone"] + 10})
inventory.update({"Headphones": inventory["Headphones"] + 5})

sold_item, sold_quantity = inventory.popitem()
print(f"Sold item: {sold_item}, Quantity: {sold_quantity}")

camera_stock = inventory.get("Camera", "Out of Stock")
print(f"Stock level of Camera: {camera_stock}")
print(inventory)
