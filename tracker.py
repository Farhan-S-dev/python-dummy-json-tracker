# What: Import the requests library
# Why: We need this tool to send HTTP requests and fetch data from web servers over the internet.
import requests

# What: Import the csv module
# Why: Python's built-in tool for creating and writing data into Comma-Separated Values files.
import csv

# What: Define the API endpoint URL for our dummy e-commerce competitor site
# Why: Keeping the URL in a variable makes our code cleaner and easy to update if the endpoint changes.
URL = "https://dummyjson.com/products"

# What: Send an HTTP GET request to fetch the product catalog
# Why: This contacts the server and downloads the raw JSON package containing our product data.
response = requests.get(URL)

# What: Check if the HTTP request was successful (Status code 200)
# Why: Ensures we only proceed if the server successfully returned data without errors.
if response.status_code == 200:
    # What: Convert the raw response text into a Python dictionary
    # Why: APIs return data in JSON format; converting it allows Python to read it as standard dictionaries and lists.
    data = response.json()

    # What: Extract the 'products' list from the main dictionary
    # Why: The actual product items are nested inside the 'products' key of the JSON response.
    products_list = data.get("products", [])

    # What: Open a new CSV file in write mode with utf-8 encoding and empty newline settings
    # Why: 'w' creates/overwrites the file, 'newline=""' prevents blank lines on Windows, and 'utf-8' acts as the universal converter for text compatibility.
    filename = "competitor_prices.csv"
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        # What: Write the header row to the CSV file
        # Why: Defines clear column titles so we know what data each column represents when opened in Excel or Google Sheets.
        writer.writerow(["Product Title", "Price ($)", "Stock", "Category"])

        # What: Loop through each individual product item in our products list
        # Why: This allows us to process and pull specific metrics from every item one by one.
        for item in products_list:
            # What: Extract specific keys (title, price, stock, category) from the current product dictionary
            # Why: Grabs only the exact details we want to track rather than saving unnecessary data.
            title = item.get("title")
            price = item.get("price")
            stock = item.get("stock")
            category = item.get("category")

            # What: Write the extracted product values as a new row in the CSV file
            # Why: Saves a clean row of competitor pricing and inventory data into our local spreadsheet.
            writer.writerow([title, price, stock, category])

    print(f"Successfully saved {len(products_list)} products to {filename}!")

else:
    # What: Print an error message if the connection fails
    # Why: Helps us troubleshoot immediately if the server is down or the URL is incorrect.
    print(f"Failed to connect. Status code: {response.status_code}")