from bs4 import BeautifulSoup
import requests, openpyxl

excel=openpyxl.Workbook()
sheet=excel.active
sheet.title="dam"
#sheet.append(['Reservoirs','Full Depth','Full Capacity','Current Year Level','Current Year Storage','Current Year Inflow','Current Year Outflow','Last Year Level','Last Year Storage'])

try:
    response=requests.get('https://tnagriculture.in/ARS/home/reservoir')
    soup=BeautifulSoup(response.text, 'html.parser')
    print(soup)
    datas=soup.find('tbody').find_all("tr")

    for data in datas:
        #print(data)
        dam_1=data.find('tr' ,class_="bg-info").text
        dam_2=data.find('tr', class_="bg-primary").text
        print(dam_1)
        sheet.append([dam_1,dam_2])
        break

except Exception as e:
    print(e)

excel.save("dams.xlsx")