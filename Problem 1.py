# Import required libraries
import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd

# URL containing the complete list of water utilities
url = "https://www.ewg.org/tapwater/state.php?stab=CA"

# Send a GET request to the URL
page = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(page.content, "html.parser")

# Find the 'More' link URL
more_link = soup.find('a', string='More')['href']
more_url = "https://www.ewg.org/tapwater/search-results.php?stab=CA&searchtype=largesys"

# Send an HTTP GET request to the 'More' page
more_response = requests.get(more_url)
more_soup = BeautifulSoup(more_response.content, 'html.parser')

# Find all 'th' elements to extract table titles
water = soup.find_all('th')

# Extract water table titles
water_table_titles = [title.text.strip() for title in water]

# Create an empty DataFrame with extracted table titles as columns
df = pd.DataFrame(columns=water_table_titles)

# Find all 'tr' elements to extract column data
column_data = soup.find_all('tr')

# Extract data
records = []
table = more_soup.find('table', class_='search-results-table')  # Assign the result to the 'table' variable
rows = table.find_all('tr')[1:]
for row in rows:
    columns = row.find_all('td')
    utility = columns[0].text.strip()
    location = columns[1].text.strip()
    people_served = columns[2].text.strip()
    length = len(df)
    records.append([utility, location, people_served])

# Save the data to a CSV file
water_utilities = "C://Users//Dell//Downloads//water_utilities.csv"
with open('water_utilities.csv', 'w', newline='', encoding='utf-8') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['Utility', 'Location', 'People Served'])
    csvwriter.writerows(records)

# Print a success message
print('Data has been scraped and saved to water_utilities.csv')