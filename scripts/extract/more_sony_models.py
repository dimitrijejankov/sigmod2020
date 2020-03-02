# -*- coding: utf-8 -*-

import urllib.request
from bs4 import BeautifulSoup
import os

url = 'https://en.wikipedia.org/wiki/Sony_ILCE_camera'

req = urllib.request.urlopen(url)
article = req.read().decode()
    
with open('List_of_Sony_%CE%B1_cameras.html', 'w') as fo:
    fo.write(article)
        
article = open('List_of_Sony_%CE%B1_cameras.html').read()
soup = BeautifulSoup(article, 'html.parser')
                    
paragraphs = soup.find_all('ul')

for paragraph in paragraphs:
    with open('../../currated_data/sony-models-tralalala.json', 'a') as fo:
        for lines in paragraph.find_all('li'):
            for title in lines.find_all('a'):
                name = title.text.strip()
                if  "Sony Alpha" in name:
                    name = name.replace("Sony Alpha ", "").upper()
                    
                    line = "[" + '"' + name+ '","' +name.replace("-"," ") +'"],'
                    print(line, file=fo)
                    line = "[" + '"' + name+ 'K","' +name.replace("-"," ") +'K"],'
                    print(line, file=fo)
                    line = "[" + '"' + name+ 'Y","' +name.replace("-"," ") +'Y"],'
                    print(line, file=fo)
                    line = "[" + '"' + name+ 'M","' +name.replace("-"," ") +'M"],'
                    print(line, file=fo)
                    line = "[" + '"' + name+ 'N","' +name.replace("-"," ") +'N"],'
             #       print(line)
                    print(line, file=fo)
             #       line = "[" + '"' + name.upper().replace("DSC-","")+ 'V","' +name.upper() +'V"],'
             #       print(line, file=fo)
                    
        
os.remove('List_of_Sony_%CE%B1_cameras.html')               

url = 'https://en.wikipedia.org/wiki/Sony_Mavica'

req = urllib.request.urlopen(url)
article = req.read().decode()
    
with open('List_of_Sony_%CE%B1_cameras.html', 'w') as fo:
    fo.write(article)
        
article = open('List_of_Sony_%CE%B1_cameras.html').read()
soup = BeautifulSoup(article, 'html.parser')
                    
paragraphs = soup.find_all('ul')

for paragraph in paragraphs:
    with open('../../currated_data/sony-models-mavica.json', 'a') as fo:
        for lines in paragraph.find_all('li'):
            name = lines.text.strip()
            
            if  "MVC" in name:
                index_of_mvc = name.find("MVC")
                index_of_bracket = name.find("(")
                name = name[index_of_mvc:index_of_bracket-1]
#               name = name.replace("Sony Alpha ", "").upper()

                line = "[" + '"' + name+ '","'+ name.replace("MVC-","")+'","'+name.replace("-"," ") +'"],'
                print(line)
              #  print(line, file=fo)
             #       line = "[" + '"' + name.upper().replace("DSC-","")+ 'V","' +name.upper() +'V"],'
             #       print(line, file=fo)
                    
        
os.remove('List_of_Sony_%CE%B1_cameras.html')               

