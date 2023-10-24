from bs4 import BeautifulSoup
import requests

url = 'https://www.ewg.org/tapwater/search-results.php?stab=CA&searchtype=largesys'

page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
print(soup)

soup.find_all('table')

table = soup.find_all('table')
print(table)

world_titles = table.find_all
world_titles

world_table_titles = [title.text.strip() for title in world_titles]

print(world_table_titles)

import pandas as pd
df = pd.DataFrame(columns = world_table_titles)

df

column_data = table.find_all('tr')

for row in column_data[1:]:
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]

    length = len(df)
    df.loc[length] = individual_row_data

    print(df)

    df.to_csv(r'C:\Users\Dell\Downloads\Test1.csv', index = False)


