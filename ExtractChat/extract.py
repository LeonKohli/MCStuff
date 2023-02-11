import re
import csv

# Compile the regular expression pattern
price_pattern = re.compile(r'(?:verkaufe|verkauft)(?:[\w\s]+)?\s*(.?)(?:[\w\s]+)?(?:für|-> pro|je|ca|ca.)?\s([\d,.]+[kK]?)')


# Open the chat log file
with open('ExtractChat\console-log.txt', 'r', encoding='utf-8') as file:
    # Read the lines of the file
    lines = file.readlines()
    lines = [line.strip() for line in lines]

# Create a list to store the item names and prices
items = []

# Loop through the lines of the file
for line in lines:
    # Search for the item name and price
    match = price_pattern.search(line)
    if match:
        # Extract the item name and price
        item_name = match.group(1)
        item_price = match.group(2)
        # Add the item name and price to the list
        items.append([item_name, item_price])

# Create a new CSV file
with open('prices.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['Name', 'Price']
    writer = csv.writer(csvfile)
    writer.writerow(fieldnames)
    writer.writerows(items)

print("Prices saved to prices")
