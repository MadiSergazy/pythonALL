# -- coding: utf-8 --

from bs4 import BeautifulSoup
import requests
''' работает
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.olx.kz/elektronika/kompyutery-i-komplektuyuschie/nastolnye-kompyutery/astana/")

titcomps = driver.find_elements(By.CLASS_NAME, 'offer-wrapper')
sumcomps = driver.find_elements(By.CLASS_NAME, "price")

for e in titcomps:     #барлық мәлімет аты жері қойған уақыты зат характеристикасы бағасы
    print(e.text)

print('0000000000000000000000000000000000000000')
for e in sumcomps:     #сумма
    print(e.text)

print('pepwpepe')
'''
def parse():
    URL = 'https://www.olx.kz/elektronika/kompyutery-i-komplektuyuschie/nastolnye-kompyutery/astana/'
    HEADERS = {
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36'         #User-Agent нужен чтоб браузер непосчитал нас ботом https://www.whatsmyua.info/
    }
    response = requests.get(URL, headers=HEADERS)#для отпраки запроса на нашу страницу
    soup = BeautifulSoup(response.content, 'html.parser')#мы получаем весь контент с страницы
    items = soup.findAll('div', class_='offer-wrapper')#вставим тэг и класс  ProductCardV category-page-list__product   ProductCardV__ImgWrapper
    comps = []#для помещения в него элементов
    #iteys = soup.find('div', class_='offer-wrapper').find('a', class_='marginright5 link linkWithHash detailsLink linkWithHashPromoted').get_text(strip=True)

    # print(type(items))
    # print(items)
    '''
    for i in items:
        print(i.text)
    iTT = items.find('a', class_='marginright5 link linkWithHash detailsLink')
    print(iTT.text)
    '''
    for item in items:
        s = item.find('a', class_='marginright5 link linkWithHash detailsLink')
        TEGy = item.find('strong')
        print(s)
        print(TEGy)

        # comps.append({
        #
        #     'title': item.find('a', class_='marginright5 link linkWithHash detailsLink'),  #get_text(strip=True),
        #     'price': item.find('p', class_='price').get_text(strip=True),
        #     'link': item.find('a', class_='marginright5 link linkWithHash detailsLink').get('href')
        # }
        # )

    #for comp in comps:
        #print(comp['title'])
        #print(comp['price'])
        #print(comp['price'])

parse()

'''

def parse():
    URL = 'https://www.technodom.kz/astana/search?recommended_by=instant_search&r46_search_query=%D0%BF%D1%8B%D0%BB%D0%B5%D1%81%D0%BE%D1%81&r46_input_query=%D0%BF%D1%8B%D0%BB%D0%B5'
    HEADERS = {  #slovar
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36'         #User-Agent нужен чтоб браузер непосчитал нас ботом https://www.whatsmyua.info/
    }
    response = requests.get(URL, headers=HEADERS)#для отпраки запроса на нашу страницу
    soup = BeautifulSoup(response.content, 'html.parser')#мы получаем весь контент с страницы
    items = soup.find_all('div', class_='ProductCardV category-page-list__product')#вставим тэг и класс  ProductCardV category-page-list__product   ProductCardV__ImgWrapper
    comps = []#для помещения в него элементов
    for item in items:

        "?????"
        comps.append()
        #comps.append(item.find('p', class_="Typography ProductCardV__Title --loading Typography__Body Typography__Body_Bold"))

       #  comps.append({
       #     'title': item.find('p', class_="Typography ProductCardV__Title --loading Typography__Body Typography__Body_Bold").get_text(strip=True)
       #     #'title': item.find('p', class_="Typography ProductCardV__Title --loading Typography__Body Typography__Body_Bold").get_text(strip=True)#strip=True убираем все отступы из текста
       # })
    # for comp in comps:
    #     print(comp)
        # print(comp['title'])

parse()
'''