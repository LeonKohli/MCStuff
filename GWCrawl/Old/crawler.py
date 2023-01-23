import requests
from bs4 import BeautifulSoup
import csv
import re

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
with open('prices1.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['Name', 'Stück Min', 'Stück Max', 'Stack Min', 'Stack Max', 'DK Min', 'DK Max']
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
        data_bs_content = item.get("data-bs-content")
        stueck_min = "N/A"
        stueck_max = "N/A"
        stack_min = "N/A"
        stack_max = "N/A"
        dk_min = "N/A"
        dk_max = "N/A"
        
        stueck_match = re.search(r'Stück: (.*?) - (.*?)', data_bs_content)
        if stueck_match:
            stueck_min = stueck_match.group(1)
            stueck_max = stueck_match.group(2)
            
        stack_match = re.search(r'Stack: (.*?) - (.*?)', data_bs_content)
        if stack_match:
            stack_min = stack_match.group(1)
            stack_max = stack_match.group(2)
            
        dk_match = re.search(r'DK: (.*?) - (.*?)', data_bs_content)
        if dk_match:
            dk_min = dk_match.group(1)
            dk_max = dk_match.group(2)
            
        # Write the data to the CSV file
        writer.writerow({'Name': name, 'Stück Min': stueck_min, 'Stück Max': stueck_max, 'Stack Min': stack_min, 'Stack Max': stack_max, 'DK Min': dk_min, 'DK Max': dk_max})

    
print("Scraping page", page_number, "complete.")

            