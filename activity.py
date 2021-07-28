from selenium import webdriver 
from bs4 import BeautifulSoup
import time
import csv
import requests
import pandas as pd
START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser=webdriver.Chrome('chromedriver')
browser.get(START_URL)
soup = BeautifulSoup(browser.page_source, "html.parser")
stars_table=soup.find('table')
temp_list=[]
table_rows=stars_table.find_all('tr')
for tr in table_rows:
    td=tr.find_all('td')
    row=[i.text.rstrip() for i in td ]
    temp_list.append(row)
stars_names=[]
distance=[]
mass=[]
radius=[]
lum=[]
for i in range(1,len(temp_list)):
    stars_names.append(temp_list[i][1])
    distance.append(temp_list[i][3])
    mass.append(temp_list[i][5])
    lum.append(temp_list[i][7])
    radius.append(temp_list[i][6])
df2=pd.DataFrame(list(zip(stars_names,distance,mass,radius,lum)),columns=['name','dis','ms','rd','lum'])
df2.to_csv('stars.csv')