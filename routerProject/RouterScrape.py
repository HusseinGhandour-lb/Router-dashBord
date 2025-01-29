import requests
from bs4 import BeautifulSoup
import csv

#setting links to scrape
links = ['https://ayoubcomputers.com/network-products/router/wi-fi-routers/?&page=1',
         'https://ayoubcomputers.com/network-products/router/wi-fi-routers/?&page=2',
         'https://ayoubcomputers.com/network-products/router/wi-fi-routers/?&page=3',
         'https://ayoubcomputers.com/network-products/router/wi-fi-routers/?&page=4',
         'https://ayoubcomputers.com/network-products/router/wi-fi-routers/?&page=5']

#saving to csv
with open('DifferentRoyters.csv', mode='w', newline='', encoding='utf-8') as file:
    
    writer = csv.writer(file)
    writer.writerow(["Brand", "Price", "Description"])
    
    
    try:
        #entering each link
        for link in links:
            response = requests.get(link)
            soup = BeautifulSoup(response.text, "html.parser")
            routers = soup.find_all('li', class_= 'product')
        
        #extacting brand, price, description
            for router in routers:
                brand = router.find('p', class_= 'card-text').text
                price = router.find('span', class_= 'price--main').text
                description = router.find('h4', class_= 'card-title').text
                writer.writerow([brand, price, description])
                
    except Exception as e:
        print(f"error: {e}")
        
print("Done! :)")