import requests
from bs4 import BeautifulSoup
import csv
import re
import datetime
import os

# Define the server switch URL
server_switch_url = "https://wert.griefergames.de/server-switch/switch/4"


# Define the base URL for the category pages
base_url = "https://wert.griefergames.de/"


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

current_dir = os.getcwd()

prices_dir = os.path.join(current_dir, "prices")
if not os.path.exists(prices_dir):
    os.makedirs(prices_dir)
    
now = datetime.datetime.now()

file_name = f"{prices_dir}\prices_{now.strftime('%Y-%m-%d %H-%M-%S')}.csv"

# Create a CSV file to store the data
with open(file_name, 'w', newline='', encoding='utf-8') as csvfile:
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
            stueck = re.search(r'Stück\s*:\s*([\d\.]+[kK]?\s*-\s*[\d\.]+[kK]?)', prices)
            stack = re.search(r'Stack\s*:\s*([\d\.]+[kK]?\s*-\s*[\d\.]+[kK]?)', prices)
            dk = re.search(r'DK\s*:\s*([\d\.]+[kK]?\s*-\s*[\d\.]+[kK]?)', prices)
            stueck = stueck.group(1).strip() if stueck else "N/A"
            stack = stack.group(1).strip() if stack else "N/A"
            dk = dk.group(1).strip() if dk else "N/A"
        
            # Write the data to the CSV file
            writer.writerow({'Name': name, 'Stück': stueck, 'Stack': stack, 'DK': dk})

print("Scraping complete, data saved to prices.csv")

#Neues Item
#1.16 - noch ohne Preis
#Keine Preisauskunft
#Seltenes Item

