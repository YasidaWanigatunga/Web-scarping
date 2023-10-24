import requests
from bs4 import BeautifulSoup
import csv

# URL of the main page
url = "https://www.lowes.com/b/southwire?searchTerm=southwire"
headers = {
        "authority": "www.lowes.com",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "accept-language": "en-US,en;q=0.9",
        "cookie": "dbidv2=0d292122-e66b-4272-b8a4-62a0f29a943a; al_sess=FuA4EWsuT07UWryyq/3foLdk3wZHsJmvnJ0j3dDngWZALtAxIEzmfCcXftAQJ/+1; LEXP=C; region=central; AKA_A2=A; EPID=MGQyOTIxMjItZTY2Yi00MjcyLWI4YTQtNjJhMGYyOWE5NDNh; bm_sz=39BDF98EF2ACC248F9107C1189DD2D5B~YAAQBQk+F7nG+NKJAQAAhbVZ8xTja5DsAXQskjCpcZTw6eHAXCr1BNtD7QJI5iglJE3QBzGDRmW/EiAWgfyOHTy22AwP+x7JkG36alIXc9bTavkKIGuAAdhDEBGRdJTOavq9rV6Zlukhu3SahFK6iL3XAOQVa46TRMcpby+CiVbjExx81nhJ3DigH6FwajZy+hlMfeqXNMd7EmxsP5i0cImzbA/ClnXCkYJth3tojtJ7rUUaUOZ5h9KtL+A//8qnTxtP6Bfc/VvXiMzsaCgR/BFbRWNG8nDxc3q1q5umhZyoIQ==~3290675~3621432; _lgsid=1692004893640; AMCVS_5E00123F5245B2780A490D45%40AdobeOrg=1; g_amcv_refreshed=1; AMCV_5E00123F5245B2780A490D45%40AdobeOrg=-1303530583%7CMCIDTS%7C20315%7CMCMID%7C81592274547428562392258898316432433423%7CMCAAMLH-1692609694%7C3%7CMCAAMB-1692609694%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1692012094s%7CNONE%7CvVersion%7C3.3.0; sn=1985; sd=%7B%22id%22%3A%221985%22%2C%22zip%22%3A%2299701%22%2C%22city%22%3A%22Fairbanks%22%2C%22state%22%3A%22AK%22%2C%22name%22%3A%22Fairbanks%20Lowe's%22%2C%22region%22%3A%2214%22%7D; zipcode=99701; nearbyid=1985; zipstate=AK; purchase-test-ordersummarynew=false; purchase-test-lowes-pay=show; discover-exp-1=abt12035c; _tt_enable_cookie=1; _ttp=yb6yMhYZnBc5k_g4RlL0z5a_JoT; _gcl_au=1.1.607320959.1692004903; _fbp=fb.1.1692004906861.257977508; IR_gbd=lowes.com; audience=DIY; session_id=570bdd73-e36e-426f-ad6b-b75ae8b02f68; _pin_unauth=dWlkPVpqRTROVE13WVRFdE9EZGtZeTAwTlRJeUxUZzFaVGt0TWpZMFkyWXlNamt5TWpKag; mdLogger=false; kampyle_userid=3807-9acf-9198-36d9-8c84-8156-4da9-4d1f; _abck=08963A0B6D9BB684C6F878ABA82CA99D~0~YAAQBQk+F0rq+NKJAQAAfDxd8wr5IVV4Km05bkpf1Q6j3PWrax8nD+XfC2Xd+z9AT+FLTJwveRP8tGpricsbjT+QMQqSDkuZXcDtDxke5HV2v8pamfAbC6QRfMN94mwo79mPAqwtaXZN0a5YZqzCey5fgzxK4BaSU4ix0MIA04J09/CGbdYlXu+bbHw/sASpImrBtJrLtdV0KKpz0vflUoIjF1bYFdctvq0XUuyMC2Xf7GeVYKpldxrCtNS5PpUp5dc+PPTwZUCwYJoDkUa/lNcg8td58HG0cBhrp9W1aczECnpJCiFvuRX30OaQAKjzlQ9js+8uv1HwpokNTOHUhKQPwZyGEowO3DddeT210DJQ7eEE6szMTkJRfXeID4O7vGsJNksOPw4P3m4W+cZ/8aMU+UipJkwGRPjVn043PitE6bcJBVsFDzbxBP6hZ5o9+uITHBjsYQI=~-1~-1~-1; ak_bmsc=232F059214671EF3ABAF221DF98BC904~000000000000000000000000000000~YAAQBQk+F2/q+NKJAQAAHEJd8xQJN0S2iaZ0QryWIcse4CRu3vIvjpCh5l5WnR9RU5Ez1AeE/8Yhq0YUlQVmgFbpxkJ4fH/ONM0UoaZnC5qNilpMk9/U194mJ/QA3R7XTdy8kAWkacy8aF7XEO0tTM2S4IiTMjiFRWlsGVU7U2PjmCfdrcUiqdx5g03vCfqAZLjquzv0GBv/Nfnuop5e0t32Odpw8JpACaNnKzu8e9BW7yWasl6T0Mv1jSjB14U4oujI5fgE7sEU4nw0ls/lphfgNWmY6XnD6zjP08uNqdoMqL+HJ060uPQAEZKD02m1lBrnpjrrV3wVuZxUCWCXK2BjWex0DwSeC8rFPYXqRk1izRio7Ypi/xVFY6xEgorX1c/dnzq2bcnRseiFAcX6UDXDL+Lituv7PeBuJMhC1xS69tJxYZpmnd+b2/abFWDgED2JmSuBeqRSmtKlGrw6Cm9AXeVB3vImvcHrrb6kmPMm7zTHQiZWGkJa+PHvtF1D+/W8fzNn96J6ntOUoonGEiNBFkM4iZVMUm3QcrjYv1TMFvKBp20zy9p8Wtg5ZZJ4Ul145P+fQ/a6WQFgccaBC8UjQT+SLcC4nMfS4QQy4/9ib6mPT10ubXUo1d2k8ZlIOSZjmdfCBLgSYpxEYpPyJRFcqs1ZMQ==; sbsd=000000000085a856605933401d90e4e927bc4aaf20bcb7aa332a2c45cf89e21fec060b5c7b4b692e4f-3ecf-4f69-8a9c-7beff6df2a5416946840221692005122; __gads=ID=4ab46f8df73910e1:T=1692005133:RT=1692005133:S=ALNI_MZHyANTYB07lO8owz20Iv05kAw4vw; __gpi=UID=00000c2c61808d55:T=1692005133:RT=1692005133:S=ALNI_MZnl4a9Djjbbke8sroOjRZesFnhLw; akavpau_default=1692005526~id=256125ece053f721399ca65fc768825a; fs_uid=#Q8RZE#acf7bf9a-f4e3-4d2a-a4d9-5c52b16f292e:677448ae-c838-4951-bf56-d841ea9843d4:1692004895466::6#cbcb2c9c#/1723540894; p13n=%7B%22zipCode%22%3A%2299701%22%2C%22storeId%22%3A%221985%22%2C%22state%22%3A%22AK%22%2C%22audienceList%22%3A%5B%5D%7D; g_previous=%7B%22gpvPageLoadTime%22%3A%220.00%22%2C%22gpvPageScroll%22%3A%2227%7C38%7C11%7C3576%22%2C%22gpvSitesections%22%3A%22landing-page%2Cbrand%2Cmerchandising-category%2Csouthwire%22%2C%22gpvSiteId%22%3A%22desktop%22%2C%22gpvPageType%22%3A%22brand%22%7D; akaalb_prod_dual=1692091637~op=PROD_GCP_EAST_CTRL_DFLT:PROD_DEFAULT_CTRL|PROD_GCP_EAST_CTRL_C:PROD_CTRL_C|~rv=22~m=PROD_DEFAULT_CTRL:0|PROD_CTRL_C:0|~os=352fb8a62db4e37e16b221fb4cefd635~id=864e3e8b7c9e89506b2e7135dc9a9c2a; bm_sv=07A0CF85B57627BF60E33DFF41AAFA69~YAAQBQk+F9H5+NKJAQAAuQJf8xSYgBqGGWoYa9ZPiMt/c+3p5ox5lPpJL4fNl0UkZ6INei9KoDW54yjPlLmRoaSvhgOMOB/oxMKrCaYE8egZQWwP3HA0Z4SBMMOlUVOBYbp42QVbQSD6J0sfI8Spk0hUBItCuNYonUEE5DJ9U5//AOBovnfo8REZ1pFm1w8AEcPgEdbxlvwaHngbkrw/oAUaH+YPW0FfudHClPoMTeGncc4XWpK7sPVgsMMIb4tm~1; _uetsid=ffb2d9603a8311eeb8cc9da564e1bd93; _uetvid=ffb32ce03a8311eeab30fb63917ff160; IR_12374=1692005237138%7C0%7C1692005237138%7C%7C; IR_PI=0230f186-3a84-11ee-941f-236dffbad69c%7C1692091637138; kampyleUserSession=1692005238388; kampyleUserSessionsCount=4; kampyleSessionPageCounter=1; kampyleUserPercentile=62.450254808920945; fs_lua=1.1692005254179; RT=\"z=1&dm=lowes.com&si=d210c84f-6e79-4823-b149-1b67e5bc771b&ss=llao0rny&sl=7&tt=1ion&bcn=%2F%2F684d0d47.akstat.io%2F&nu=v1iprqm&cl=g971\"",
        "referer": "https://www.lowes.com/b/southwire?searchTerm=southwire",
        "sec-ch-ua": "\"Not/A)Brand\";v=\"99\", \"Google Chrome\";v=\"115\", \"Chromium\";v=\"115\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "same-origin",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
    }
# Send an HTTP GET request to the URL
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")
category_elements = soup.find_all('div', class_='sc-98d7ri_engage-common-2')

# Initialize a list to store category data
category_data = []

# Iterate through category elements
for category in category_elements:
    category_name = category.find("a").text
    category_link = category.find("a", href=True)["href"]
    act_link='https://www.lowes.com/'+category_link
    category_data.append({"name": category_name, "link": act_link})

# Print category data
for category in category_data:
    print("Category:", category["name"])
    print("Link:", category["link"])
    print()

with open("categories.csv", "w", newline="", encoding="utf-8") as csvfile:
    fieldnames = ["name", "link"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(category_data)

# Iterate through each category and retrieve product information
for category in category_data:
    category_name = category["name"]
    category_link = category["link"]

    category_response = requests.get(category_link, headers=headers)
    print(category_response)
    category_soup = BeautifulSoup(category_response.content, "html.parser")
    product_elements = category_soup.select(".tile_group")
    print(f"Products in category: {category_name}\n")
    for product in product_elements:
        product_name = product.select_one(".description-spn").text
        product_price = product.select_one(".prdt-actl-pr").text
        print(f"Product Name: {product_name}")
        print(f"Price: {product_price}\n")
