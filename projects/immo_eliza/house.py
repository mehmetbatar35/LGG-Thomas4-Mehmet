import requests
from bs4 import BeautifulSoup

class House():
    cheat_immo = { 
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
                }
    
    def __init__(self, url):
        self.url = url
        self.price = self.get_price(url)

    def property(self):
        cheat_immo = { 
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
                }        
        # url = 'https://www.immoweb.be/en/search/house/for-sale?countries=BE&page=1&orderBy=relevance'
        response = requests.get(url, headers = cheat_immo)
        soup = BeautifulSoup(response.content, 'html.parser')
        urls = self.search_link(soup)
        list_price = []
        for url in urls:
            price = self.get_price(url)
            list_price.append(price)
        return list_price 
    
    def search_link(soup: BeautifulSoup):
        list_links = []
        maison_link_soup = soup.find_all('a', attrs={"class":"card__title-link"})
        for link in maison_link_soup:
            list_links.append(link["href"])
        return list_links        

    def get_price(self, url):
        cheat_immo = { 
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
                }        
        response = requests.get(url, headers = cheat_immo)
        soup = BeautifulSoup(response.content, 'html.parser')
        price_soup = soup.find("p", attrs={"class": "classified__price"}).find("span", class_="sr-only").get_text()
        print(price_soup)



