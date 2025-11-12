# Python-Inventory-Management-Basics 📦

This is a simple Python script that uses the **Dictionary** data structure to demonstrate basic **Inventory Management** operations.

It illustrates how to:
1.  Define an initial inventory.
2.  Update existing stock levels.
3.  Remove an item from the inventory and retrieve its quantity (using `popitem()`).
4.  Safely check the stock level of an item, even if it doesn't exist in the dictionary (using `get()`).

## ⚙️ Code Details

The initial inventory is stored in the `inventory` dictionary:

```python
inventory = {
    "Laptop": 10,
    "Smartphone": 25,
    "Tablet": 15,
    "Headphones": 30,
    "Smartwatch": 20
}
```

The following operations are performed in the script:

Stock Update:

10 units are added to the Smartphone stock.

5 units are added to the Headphones stock.

Item Sold (Simulating a Sale):

The last inserted item is removed from the dictionary using inventory.popitem().

The name of the item sold (sold_item) and its quantity (sold_quantity) are printed.

Stock Check (get()):

The stock level of Camera is checked using inventory.get("Camera", "Out of Stock"). Since Camera is not present, the default value "Out of Stock" is printed.

Final Inventory:

The remaining final inventory dictionary after all operations is printed.

🚀 Expected Output
When you run the code, you should get the following output:

Sold item: Smartwatch, Quantity: 20
Stock level of Camera: Out of Stock
{'Laptop': 10, 'Smartphone': 35, 'Tablet': 15, 'Headphones': 35}
🛠️ How to Run
Save the code as a Python file (e.g., inventory_script.py).

Run the script using Python in your terminal or command prompt:

Bash

python inventory_script.py
