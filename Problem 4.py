import requests
from bs4 import BeautifulSoup
import re
import os

headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Host": "www.kallanish.com",
        "Origin": "https://www.kallanish.com",
        "Referer": "https://www.kallanish.com/en/",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-User": "?1",
        "Cookie": "csrftoken=zfnYhIaAoybI8cv5tsukY7jjl4V9gxh6aiaYRqkZQ0pSj8zxjyKot5yVg64R68Sp"
    }
data = {
        "csrfmiddlewaretoken": "ctOyIM8SNBMUw7daMqVdGkn3SDxmOOHYNwByiuihf304H3hCCwbhbiCFNFG4Epih",
        "username": "antony.fisher@mintecglobal.com",
        "password": "antony",
        "next": "/en/prices/list/ferrous/regions/europe/"
    }
base_url = "https://www.kallanish.com"
login_url = base_url + "/en/login/"

with requests.Session() as session:
        r = session.post(login_url, data=data, headers=headers)
        soup = BeautifulSoup(r.text, "html.parser")
        print(soup)
        tkn_input = soup.find("input", {"name": "csrfmiddlewaretoken"})

        if tkn_input:
                tkn = tkn_input["value"]
                data["csrfmiddlewaretoken"] = tkn
                response = session.post(login_url, data=data, headers=headers)

                if response.status_code == 200:
                        print("Login successful!")

                        # Continue with your code for fetching and processing pages
                else:
                        print("Login failed. Status code:", response.status_code)
                        print("Response content:", response.text)
        else:
                print("CSRF token input not found on the page.")

# Find and calculate average of Latest Price column
latest_price_cells = soup.find_all("td", class_="latest-price")
prices = [float(re.sub(r'[^\d.]', '', cell.get_text())) for cell in latest_price_cells]
average_price = sum(prices) / len(prices) if prices else None

# Add the average to each row
for cell in latest_price_cells:
    cell.parent.append(soup.new_tag("td", string=str(average_price)))

# Save the modified Europe page
with open("europe_page_with_average.html", "w", encoding="utf-8") as f:
    f.write(soup.prettify())

print("Average added and Europe page saved.")

