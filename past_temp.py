# -*- coding: utf-8 -*-
import sys
import urllib.request
from bs4 import BeautifulSoup

if len(sys.argv) == 4:
    year = sys.argv[1]
    month = sys.argv[2] 
    day = sys.argv[3]
else:
    year = "2019"
    month = "9"
    day = "19"
prec_no="44" #Tokyo
block_no="1002" #Nerima

url = "http://www.data.jma.go.jp/obd/stats/etrn/view/hourly_a1.php?prec_no="+prec_no+"&block_no="+block_no+"&year="+year+"&month="+month+"&day="+day+"&view="

f = urllib.request.urlopen(url)
html = f.read().decode('utf-8')

soup = BeautifulSoup(html, "html.parser")

locations = soup.findAll("h3")

if len(locations) == 0:
    print("could not obtain data")
    sys.exit()
location = locations[0]
tables = soup.findAll("table" , {"id":"tablefix1"})
if len(tables) == 0:
    print("could not obtain data")
    sys.exit()
table=tables[0]

rows = table.findAll("tr")
rows.pop(0)
rows.pop(0)
print(location.get_text())
print("Time","Temperature")
for row in rows:
   cells = row.findAll(['td', 'th'])
   print(cells[0].get_text()+","+cells[2].get_text())

