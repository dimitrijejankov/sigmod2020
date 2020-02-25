# -*- coding: utf-8 -*-

import urllib.request
from bs4 import BeautifulSoup
import os

urls = ['https://en.wikipedia.org/wiki/List_of_Sony_E-mount_cameras',
        'https://en.wikipedia.org/wiki/List_of_Sony_A-mount_cameras',
        ]
for url in urls:
    req = urllib.request.urlopen(url)
    article = req.read().decode()
    
    with open('List_of_Sony_%CE%B1_cameras.html', 'w') as fo:
        fo.write(article)
        
    article = open('List_of_Sony_%CE%B1_cameras.html').read()
    soup = BeautifulSoup(article, 'html.parser')
    tables = soup.find_all('table', class_='sortable')
    
    
    for table in tables:
        ths = table.find_all('th')
        headings = [th.text.strip() for th in ths]
        if headings[0] == ['Name', 'Model', 'Code']:
            break
        
    with open('../../currated_data/sony-models.json', 'a') as fo:
        for tr in table.find_all('tr'):
            tds = tr.find_all('td')
            if not tds:
                continue
            name, model = [td.text.strip() for td in tds[:2]]
            line = "[" + '"' + name+ '",' + '"' + model+ '"]'
            
            print(line, file=fo)

os.remove('List_of_Sony_%CE%B1_cameras.html')


url = 'https://en.wikipedia.org/wiki/List_of_Sony_Cyber-shot_cameras#D_series'

req = urllib.request.urlopen(url)
article = req.read().decode()
    
with open('List_of_Sony_%CE%B1_cameras.html', 'w') as fo:
    fo.write(article)
        
article = open('List_of_Sony_%CE%B1_cameras.html').read()
soup = BeautifulSoup(article, 'html.parser')
tables = soup.find_all('table', class_='wikitable')
    
for table in tables:
   # print(table)
   with open('../../currated_data/sony-models.json', 'a') as fo:
       for trs in table.find_all('tr'):    
           tds = trs.find_all('td')
           if not tds:
               continue
           name= tds[0].text.strip()
           if name[-1] == "]" and (name[-3] == "[" or name[-4] == "[" ):
               name =name[:-3]
           line = "[" + '"' + name+  '"]'
           print(line)
           print(line, file=fo)
           
           
           
os.remove('List_of_Sony_%CE%B1_cameras.html')               

 