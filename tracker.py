import requests
import csv

URL = "https://dummyjson.com/products"

response = requests.get(URL)

if response.status_code == 200:
    data = response.json()
    products_list = data.get("products", [])

    filename = "competitor_prices.csv"

    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Product Title", "Price ($)", "Stock", "Category"])

        for item in products_list:
            title = item.get("title")
            price = item.get("price")
            stock = item.get("stock")
            category = item.get("category")

            writer.writerow([title, price, stock, category])

    print(f"Successfully saved {len(products_list)} products to {filename}!")

else:
    print(f"Failed to connect. Status code: {response.status_code}")
