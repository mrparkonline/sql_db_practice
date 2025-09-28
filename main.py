# SQL DB Creator

import sqlite3
import random

connection = sqlite3.connect("./database.db")
cursor = connection.cursor()

product_table_query = """
CREATE TABLE IF NOT EXISTS Products (
    product_id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_name TEXT NOT NULL,
    price REAL NOT NULL,
    stock_quantity INTEGER DEFAULT 0
);
"""

sales_query = """
CREATE TABLE IF NOT EXISTS Sales (
    sales_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    sale_count INTEGER DEFAULT 0
);
"""

def add_random_employees(cursor):
    first_names = ["Alice", "Bob", "Carol", "David", "Evelyn", "Frank", "Grace", "Hector"]
    last_names = ["Smith", "Johnson", "Brown", "Taylor", "Wilson", "Clark", "Lewis", "Walker"]
    employees = {
        i: {
            "first_name": random.choice(first_names),
            "last_name": random.choice(last_names),
            "sale_count": random.randint(0, 50)   # random number of sales
        }
        for i in range(1, 6)   # generate 5 employees
    }

    for i, employee in employees.items():
        query = """
            INSERT INTO Sales (first_name, last_name, sale_count) VALUES (?, ?, ?)
        """
        cursor.execute(query, (employee["first_name"], employee["last_name"], employee["sale_count"]))

def add_random_products(cursor):
    hype_products = [
        "Supreme T-Shirt",
        "Labubu Figure",
        "Pokemon Cards Pack",
        "Yeezy Sneakers",
        "Kaws Companion",
        "Bearbrick 1000%",
        "Off-White Hoodie",
        "Funko Pop Rare",
        "Travis Scott Jordans",
        "Louis Vuitton Wallet"
    ]

    # Generate a dictionary of random products
    products = {
        i: {
            "product_name": hype_products[i],
            "price": round(random.uniform(50.0, 500.0), 2),   # hype items often $$$
            "stock_quantity": random.randint(1, 20)            # rare / limited stock
        }
        for i in range(10)   # generate 9 random products
    }

    for i, product in products.items():
        query = "INSERT INTO Products (product_name, price, stock_quantity) VALUES (?, ?, ?)"

        cursor.execute(
            query, 
            (
                product["product_name"], 
                product["price"], 
                product["stock_quantity"]
            )
        )

add_random_products(cursor)
#cursor.execute("DELETE FROM Products;")
#cursor.execute(product_table_query)
#cursor.execute(sales_query)

# commit changes and close
connection.commit()
connection.close()