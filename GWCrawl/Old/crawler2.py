import requests
from bs4 import BeautifulSoup
import csv

# Define the server switch URL
server_switch_url = "https://wert.griefergames.de/server-switch/switch/4"


# Define the base URL for the category pages
base_url = "https://wert.griefergames.de/"

# Switch the server
session = requests.Session()
session.get(server_switch_url)

# Create a CSV file to store the data
with open('prices.csv', 'w', newline='') as csvfile:
    fieldnames = ['Name', 'Stück', 'Stack', 'DK']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

# Switch the server
session = requests.Session()
session.get(server_switch_url)

# Set the base URL for the category pages
category_base_url = base_url + "item/category/all/"

# Get the HTML for the first category page
response = session.get(category_base_url + "1")
soup = BeautifulSoup(response.text, 'html.parser')

# Find the last page number
pagination = soup.find('ul', class_='pagination')
last_page = int(pagination.find_all('li')[-2].text)

# Create a CSV file to store the data
with open('prices.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['Name', 'Stück', 'Stack', 'DK']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()


    # Loop through the pages
    for page_number in range(1, last_page + 1):
        # Get the HTML for the category page
        category_url = category_base_url + str(page_number)
        response = session.get(category_url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all the items on the page
        items = soup.find_all('a', class_='item-col-display')

        # Loop through the items and extract the prices
        for item in items:
            name = item.find('h5').text.strip()
            prices = item.find('div', class_='mobile-price-display').text.strip()
            stueck = "N/A"
            stack = "N/A"
            dk = "N/A"
            print (prices)
            if "Stück" in prices:
                stueck = prices.split('Stück')[1].strip()
            if "Stack" in prices:
                stack = prices.split('Stack')[1].strip()
            if "DK" in prices:
                dk = prices.split('DK')[1].strip()
        
            # Write the data to the CSV file
            writer.writerow({'Name': name, 'Stück': stueck, 'Stack': stack, 'DK': dk})

print("Scraping complete, data saved to prices.csv")

#Neues Item
#1.16 - noch ohne Preis
#Keine Preisauskunft
#Seltenes Item

