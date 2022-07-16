from pydoc import classname
import requests
from bs4 import BeautifulSoup

import xlsxwriter

url = "https://fr.wikipedia.org/wiki/Arrondissement_du_B%C3%A9nin"
page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")


#print(commune.get_text())
'''

arrondissements = soup.select(".mw-parser-output h3 + p a")
for a in arrondissements:
    print(a.get_text())
'''

communes = soup.select("h3 .mw-headline a")
paragraphes = soup.select(".mw-parser-output h3 + p")

results = []


for i in range(len(communes)):
    commune = communes[i].get_text()
    
    p = paragraphes[i]
    arrondissements = []
    for a in p.select("a"):
        
        arrondissement = a.get_text()
        arrondissements.append(arrondissement)
        
    #prepend communes in arrondissements arrays
    arrondissements.insert(0, commune)
        
    results.append(arrondissements)
    
#print(results)  

workbook = xlsxwriter.Workbook('arrondissement.xlsx')
worksheet = workbook.add_worksheet()

row = 1
col = 0

for col, arronds in enumerate(results):
    for row, a in enumerate(arronds):
        worksheet.write_string(row, col, a)
    
workbook.close()

    
   

    
    
    