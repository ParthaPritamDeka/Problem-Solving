



### Quick and dirty Code to convert a Styyring to CSV using Pandas Dataframe


import json
import requests
import urllib2
import csv
import pandas as pd

response = urllib2.urlopen('########')

data = response.read()

data = data.replace('[','')
data = data.replace(']','')
data = data.replace('(','')


data_list = data.split('),') 

new_list = []

for i in data_list:
    dum_list = i.split(',')
    #break
    new_list.append(dum_list)

df = pd.DataFrame(new_list, columns=['country', 'city', .....'])

print df.head()

df.to_csv('C:\\Users\\212452403\\Downloads\\MSK_latest.csv')


