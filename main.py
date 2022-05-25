from bs4 import BeautifulSoup
import requests, openpyxl

try:
    response=requests.get('https://tnagriculture.in/ARS/home/reservoir')
    soup=BeautifulSoup(response.text, 'html.parser')
    #print(soup)
    datas=soup.find('tbody').find_all("tr")

    for data in datas:
        print(data)
        break
except Exception as e:
    print(e)