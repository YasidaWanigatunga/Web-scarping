from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import csv
import time

# Initialize Chrome WebDriver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://ikman.lk/en/ads")
Vehicles= driver.find_element(By.XPATH,'//span[@class="name--1H5Tb" and text()="Vehicles"]')
Vehicles.click()

VehicleSearchbox=driver.find_element(By.XPATH,'//input[@name="query" and @type="search" and @class="search-input--PtfH8 serp--1fE3f"]')
VehicleSearchbox.send_keys('lancer ex')
search_button_locator = driver.find_element(By.XPATH, '//button[contains(@class, "search-button--1_VmY") and @type="submit"]')
search_button_locator.click()
# Defining vehicle data array to store vehicle details
vehicle_data = []
# Give the javascript time to render
time.sleep(3)
soup=BeautifulSoup(driver.page_source, "html.parser")
# Find all advertisement containers
category_elements = soup.find_all('div', class_='content--3JNQz')

for category in category_elements:
    title = category.find("h2",class_='title--3yncE').text
    price = category.find("div",class_='price--3SnqI').text
    vehicle_data.append([title, price])

# Save data to CSV
csv_file_path = 'vehicle_data.csv'
with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Title', 'Price'])

    for data in vehicle_data:
        csv_writer.writerow(data)

print("Data saved to", csv_file_path)

# Close the WebDriver
driver.quit()









