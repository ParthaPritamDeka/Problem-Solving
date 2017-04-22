

from bs4 import BeautifulSoup
import requests
import json
import os

html_page = "virgin_and_logan_airport.html"

data = []
test = {}
info = {}

f = "FL-ATL.html"
test["courier"], test["airport"] = f[:6].split("-")




with open(html_page, "r") as html:
        soup = BeautifulSoup(html)


#table = soup.find('table',{'class':'dataTDRight'})
        table = soup.find("table",{"class":"dataTDRight"})
        #print table
        print "\n"
        print "\n"
        trs = soup.find_all('tr', {'class':'dataTDRight'})
        #print trs


        for tr in trs[0:]:
            tds = tr.find_all('td')
            info["courier"] = test["courier"]
            info["airport"] = test["airport"]
            info['year'] = int(tds[0].get_text())
            info['month'] = tds[1].get_text()
            flights = {}
            flights['domestic'] = tds[2].get_text()#.replace(',',''))
            flights['international'] = tds[3].get_text()#.replace(',',''))
            info['flights'] = flights
            #data.append(info["courier"])
            #data.append(info["airport"])
            data.append(info)
'''
for tr in trs[:-1]:
    tds = tr.find_all('td')
    info['year'] = int(tds[0].get_text())
    info['month'] = tds[1].get_text()
    flights = {}
    flights['domestic'] = int(tds[2].get_text().replace(',',''))
    flights['international'] = int(tds[3].get_text().replace(',',''))
    info['flights'] = flights
    data.append(info)
'''

#print trs[0]
#print
print len(data)
