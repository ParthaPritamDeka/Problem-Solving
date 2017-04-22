import requests
from bs4 import BeautifulSoup

s = requests.Session()

r_get = s.get("http://www.transtats.bts.gov/Data_Elements.aspx?Data=2")

soup = BeautifulSoup(r_get.text)
viewstate_element = soup.find(id="__VIEWSTATE")
viewstate = viewstate_element["value"]

eventvalidation_element = soup.find(id ="__EVENTVALIDATION")
eventvalidation = eventvalidation_element["value"]



r_post = s.post("http://www.transtats.bts.gov/Data_Elements.aspx?Data=2",
                    data={'AirportList': "FL",
                          'CarrierList': "ATL",
                          'Submit': 'Submit',
                          "__EVENTTARGET": "",
                          "__EVENTARGUMENT": "",
                          "__EVENTVALIDATION": eventvalidation,
                          "__VIEWSTATE": viewstate
                    })


f=open("FL-ATL.html", "w")
f.write(r_post.text)

