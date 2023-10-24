from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import csv
import time

# Initialize Chrome WebDriver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://ikman.lk/en/ads")

Vehicles= driver.find_element(By.XPATH,'//span[@class="name--1H5Tb" and text()="Vehicles"]')
Vehicles.click()

VehicleSearchbox=driver.find_element(By.XPATH,'//input[@name="query" and @type="search" and @class="search-input--PtfH8 serp--1fE3f"]')
VehicleSearchbox.send_keys('lancer ex')
search_button_locator = driver.find_element(By.XPATH, '//button[contains(@class, "search-button--1_VmY") and @type="submit"]')
search_button_locator.click()


vehicle_data = []
soup=BeautifulSoup(driver.page_source, 'html.parser')

# Find all advertisement containers
ads = soup.find_all('li', class_='normal--2QYVk gtm-normal-ad')
title = ads.find('h2', class_='heading--2eONR').text.strip()
price = ads.find('div', class_='amount--3NTpl').text.strip()
vehicle_data.append([title, price])
# Extract titles and prices and store in the array
# for ad in ads:
#     title = ad.find('h2', class_='heading--2eONR').text.strip()
#     price = ad.find('div', class_='amount--3NTpl').text.strip()
#     vehicle_data.append([title, price])



# Close the WebDriver
driver.quit()
print(vehicle_data)
# Save data to CSV
csv_file_path = 'vehicle_data.csv'
with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Title', 'Price'])

    for data in vehicle_data:
        csv_writer.writerow(data)

print("Data saved to", csv_file_path)