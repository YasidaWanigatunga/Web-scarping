import time
from bs4 import BeautifulSoup
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

# Initialize the WebDriver (choose your browser)
driver = webdriver.Chrome() # Make sure the Chrome driver is installed and in your PATH

# Define the base URL
base_url = "https://www.londonstockexchange.com/indices/ftse-100/constituents/table?page="

# Number of pages to scrape (in your case, 5 pages)
num_pages = 5

# Initialize an empty list to store the data
data = []

# Loop through each page
for page_number in range(1, num_pages + 1):
    # Construct the URL for the current page
    url = f"{base_url}{page_number}"
    driver.get(url)
    time.sleep(3)
    # Wait for the content to load (adjust the timeout as needed)
    wait = WebDriverWait(driver, 30)
    element = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/app-root')))

    # Find all rows within the table
    rows = driver.find_elements(By.XPATH, '//*[@id="ftse-index-table"]/table/tbody/tr')

    # Loop through the rows and extract data from the table
    for row in rows:
        columns = row.find_elements(By.TAG_NAME, 'td')
        if columns: # Make sure it's not the header row
            Code = columns[0].text.strip()
            Name = columns[1].text.strip()
            Currency = columns[2].text.strip()
            Market_cap = columns[3].text.strip()
            price = columns[4].text.strip()
            change = columns[5].text.strip()
            data.append([Code, Name, Currency, Market_cap, price, change])

# Close the browser
driver.quit()

# Create a DataFrame from the collected data
df = pd.DataFrame(data, columns=["Code", "Name", "currency", "Market_cap", "price", "change"])
print(df)
# Save the DataFrame to a CSV file
df.to_csv("LSEG.csv", index=False)