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
            line1 = ""
            line2 = ""
            line3 = ""
            line4 = ""
            line5 = ""

            if not tds:
                continue
            name = tds[0].text.strip()
            if "-" in name:
                line1 = "[" + '"' + name + '",' + '"' + name.replace("-"," ")+'","' + name.replace("-","")+ '"],'
                line2 = "[" + '"' + name + 'K",' + '"' + name.replace("-"," ")+'K","' + name.replace("-","")+ 'K"],'
                line3 = "[" + '"' + name + 'Y",' + '"' + name.replace("-"," ")+'Y","' + name.replace("-","")+ 'Y"],'
                line4 = "[" + '"' + name + 'M",' + '"' + name.replace("-"," ")+'M","' + name.replace("-","")+ 'M"],'
                line5 = "[" + '"' + name + 'N",' + '"' + name.replace("-"," ")+'N","' + name.replace("-","")+ 'N"],'                
                line1 = line1.upper().replace("SONY ","")
                line2 = line2.upper().replace("SONY ","")
                line3 = line3.upper().replace("SONY ","")
                line4 = line4.upper().replace("SONY ","")
                line5 = line5.upper().replace("SONY ","")
                print(line2, file=fo)
                print(line3, file=fo)
                print(line4, file=fo)
                print(line5, file=fo)

            else:
                line1 = ("[" + '"' + name.replace("\u03B1","ALPHA")  + '",' + '"'+ name.replace("\u03B1","ALPHA A")   + '", "' +
                          name.replace("\u03B1","ALPHA ")+  '" ,"'+ name.replace("\u03B1","A ")+ '" ,"'+ name.replace("\u03B1","A")+'"], ' ) 
                line1 = line1.upper().replace("SONY ","")
            print(line1, file=fo)
            

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
           if name[-1] == "]" and name[-3] == "["  :
               name =name[:-3]
           if name[-1] == "]" and name[-4] == "[" :
               name =name[:-4]
           line2 = ""    
           if name[-1] == "V":
               name = name[:-1]
           if name[-1] == "/":
               name = name[:-1]

           line = "[" + '"' + name.upper().replace("DSC-","")+ '","' +name.upper() +'"],'
           print(line, file=fo)
           line2 = "[" + '"' + name.upper().replace("DSC-","")+ 'V","' +name.upper() +'V"],'
           print(line2, file=fo)
           
         
paragraphs = soup.find_all('ul')

for paragraph in paragraphs:
    with open('../../currated_data/sony-models.json', 'a') as fo:
        for lines in paragraph.find_all('li'):
            for title in lines.find_all('b'):
                name = title.text.strip()
                if name != "series":
                    line = "[" + '"' + name.upper().replace("DSC-","")+ '","' +name.upper() +'"],'
                    print(line, file=fo)
                    line = "[" + '"' + name.upper().replace("DSC-","")+ 'V","' +name.upper() +'V"],'
                    print(line, file=fo)
                    
               
           
os.remove('List_of_Sony_%CE%B1_cameras.html')               

 