# -*- coding: utf-8 -*-

# Fujifilm
# F-SERIES 


import urllib.request
from bs4 import BeautifulSoup
import os

url = "https://en.wikipedia.org/wiki/Fujifilm_FinePix_F_series"

req = urllib.request.urlopen(url)
article = req.read().decode()
    
with open('Fuji.html', 'w') as fo:
    fo.write(article)
        
article = open('Fuji.html').read()
soup = BeautifulSoup(article, 'html.parser')
tables = soup.find_all('table', class_='sortable')

for table in tables:
    
    with open('../../currated_data/fujifilm-models.json', 'a') as fo:
        for tr in table.find_all('tr'):
            tds = tr.find_all('td')
            if not tds:
                continue
            
            tds = tr.find_all('td')
            name = tds[0].text.strip()
            if(len(name) > 7):
                splitet_name = name.split("F")
                while("" in splitet_name):
                    splitet_name.remove("")
                for name in splitet_name:
                    model = "F"+name
                    line = "[" + '"' + model + '","' + model[:1] + " "+ model[1:]+ '","' + model[:1] + "-"+ model[1:]  + '"],'
                    print(line.upper(), file =fo)
            else:
                model = name
                line = "[" + '"' + model + '","' + model[:1] + " "+ model[1:]+ '","' + model[:1] + "-"+ model[1:]  + '"],'
                print(line.upper(), file = fo)

os.remove("Fuji.html")

# %% j-series 

url = 'https://en.wikipedia.org/wiki/Fujifilm_FinePix_J_series'

req = urllib.request.urlopen(url)
article = req.read().decode()
    
with open('Fuji.html', 'w') as fo:
    fo.write(article)
        
article = open('Fuji.html').read()
soup = BeautifulSoup(article, 'html.parser')
                    
paragraphs = soup.find_all('ul')

for paragraph in paragraphs:
    with open('../../currated_data/fujifilm-models.json', 'a') as fo:
        for lines in paragraph.find_all('li'):
            name = lines.text.strip()
            if name != "" and  name[0] == "J" :
                if name.endswith(" (discontinued)"):
                    name = name[:len(name)- len(" (discontinued)")]
                if name[-1] == "]":
                    name = name[:len(name)-3]
                #print(name)
                line = "[" + '"' + name + '","' + name[:1] + " "+ name[1:]+ '","' + name[:1] + "-"+ name[1:]  + '"],'
                if name[:2] == "JX":
                    line = "[" + '"' + name + '","' + name[:2] + " "+ name[2:]+ '","' + name[:2] + "-"+ name[2:]  + '"],'
                if name[:2] == "JV":
                    line = "[" + '"' + name + '","' + name[:2] + " "+ name[2:]+ '","' + name[:2] + "-"+ name[2:]  + '"],'
                if name[:2] == "JZ":
                    line = "[" + '"' + name + '","' + name[:2] + " "+ name[2:]+ '","' + name[:2] + "-"+ name[2:]  + '"],'
                print(line.upper(), file = fo)
                
os.remove("Fuji.html")  

# %% s-series

url = 'https://en.wikipedia.org/wiki/Fujifilm_FinePix_S-series'

req = urllib.request.urlopen(url)
article = req.read().decode()
    
with open('Fuji.html', 'w') as fo:
    fo.write(article)
        
article = open('Fuji.html').read()
soup = BeautifulSoup(article, 'html.parser')
                    
paragraphs = soup.find_all('ul')

for paragraph in paragraphs:
    with open('../../currated_data/fujifilm-models.json', 'a') as fo:
        for lines in paragraph.find_all('li'):
            for name in lines.find_all('a'):
                if not name:
                    continue
                name = name.text.strip()
                if "Fujifilm FinePix " in name: 
                    name = name.replace("Fujifilm FinePix ","")
                    name = name.replace("cameras", "")
                    name2 = "FinePix " + name
                    
                    line1 = "[" + '"' + name + '","' + name[:1] + " "+ name[1:]+ '","' + name[:1] + "-"+ name[1:]  + '",'
                    line2 =  '"' + name2 + '","' + name2[:9] + " "+ name2[9:]+ '","' + name2[:9] + "-"+ name2[9:]  + '"],'

                    if name[:2] == "HS":
                        line1 = "[" + '"' + name + '","' + name[:2] + " "+ name[2:]+ '","' + name[:2] + "-"+ name[2:]  + '",'
                        line2 ='"' + name2 + '","' + name2[:10] + " "+ name2[10:]+ '","' + name2[:10] + "-"+ name2[10:]  + '"],'
                    if name[:2] == "SL":
                        line1 = "[" + '"' + name + '","' + name[:2] + " "+ name[2:]+ '","' + name[:2] + "-"+ name[2:]  + '",'
                        line2 =  '"' + name2 + '","' + name2[:10] + " "+ name2[10:]+ '","' + name2[:10] + "-"+ name2[10:]  + '"],'
                    print((line1 + line2).upper(), file=fo)
                
os.remove("Fuji.html")  
# %% HS series, T - series
with open('../../currated_data/fujifilm-models.json', 'a') as fo:
    lines = ['["HS 20", "HS-20", "HS20"],',
             '["HS 25", "HS-25", "HS25"],',
             '["HS 30", "HS-30", "HS30"],',
             '["HS 33", "HS-33", "HS33"],',
             '["HS 35", "HS-35", "HS35"],',
             '["HS 50", "HS-50", "HS50"],',
             '["FinePix T200","FinePix T-200","FinePix T 200","T200","T-200","T 200"]',
             '["FinePix T300","FinePix T-300","FinePix T 300","T300","T-300","T 300"]',
             '["FinePix T350","FinePix T-350","FinePix T 350","T350","T-350","T 350"]',
             '["FinePix T400","FinePix T-400","FinePix T 400","T400","T-400","T 400"]'
             ]
    for line in lines: 
        
        print(line.upper(), file = fo)



# %% XP - series
        
        
        
url = 'https://en.wikipedia.org/wiki/Fujifilm_FinePix_XP-series'

req = urllib.request.urlopen(url)
article = req.read().decode()
    
with open('Fuji.html', 'w') as fo:
    fo.write(article)
        
article = open('Fuji.html').read()
soup = BeautifulSoup(article, 'html.parser')
                    
paragraphs = soup.find_all('ul')

for paragraph in paragraphs:
    with open('../../currated_data/fujifilm-models.json', 'a') as fo:
        for lines in paragraph.find_all('li'):
            if not lines:
                continue
            
            name = lines.text.strip()
            if "FinePix" in name:
                name = name.replace("FinePix ","")
                index_of_bracket = name.find('[')
                name = name[:index_of_bracket]
                name = name.replace(" ", "")
                if name != "FujifilmFinePi" and name != "Fujifilmcamera":
                    line = "[" + '"' + name + '","' + name[:2] + " "+ name[2:]+ '","' + name[:2] + "-"+ name[2:]  + '"],'
                    print(line, file=fo)


                
os.remove("Fuji.html") 

# %% z-series

url = 'https://en.wikipedia.org/wiki/Fujifilm_FinePix_Z-series'

req = urllib.request.urlopen(url)
article = req.read().decode()
    
with open('Fuji.html', 'w') as fo:
    fo.write(article)
        
article = open('Fuji.html').read()
soup = BeautifulSoup(article, 'html.parser')
                    
paragraphs = soup.find_all('ul')

for paragraph in paragraphs:
    with open('../../currated_data/fujifilm-models.json', 'a') as fo:
        for lines in paragraph.find_all('li'):
            for name in lines.find_all('a'):
                if not name:
                    continue
                name = name.text.strip()
                if "FinePix" in name: 
                    name = name.replace("FinePix ", "")
                    name = name.replace(" ", "")
                    if name != "FujifilmFinePix" and name != "Fujifilmcameras":
                        print(name)
                        line = "[" + '"' + name + '","' + name[:1] + " "+ name[1:]+ '","' + name[:1] + "-"+ name[1:]  + '"],'
                        print(line,file=fo)

                
os.remove("Fuji.html")  


# %% x-series

url = 'https://en.wikipedia.org/wiki/Fujifilm_X_series'

req = urllib.request.urlopen(url)
article = req.read().decode()
    
with open('Fuji.html', 'w') as fo:
    fo.write(article)
        
article = open('Fuji.html').read()
soup = BeautifulSoup(article, 'html.parser')
                    
paragraphs = soup.find_all('ul')

for paragraph in paragraphs:
    with open('../../currated_data/fujifilm-models.json', 'a') as fo:
        for lines in paragraph.find_all('li'):
            for name in lines.find_all('a'):
                if not name:
                    continue
                name = name.text.strip()
                if "Fujifilm" in name:
                    name = name.replace("Fujifilm ","")
                    name = name.replace("Finepix ","")
                    
                    if name == "X-mount" or name == "Corp. v. Benun" or name == "digital cameras":
                        break
                    name = name.replace("-","")

                    line = "[" + '"' + name + '","' + name[:1] + " "+ name[1:]+ '","' + name[:1] + "-"+ name[1:]  + '"],'
                    print(line,file=fo)
                
os.remove("Fuji.html")


# %% fujifillm.com 

urls = ["https://www.fujifilm.com/support/digital_cameras/specifications/j/",
       "https://www.fujifilm.com/support/digital_cameras/specifications/a/",
       "https://www.fujifilm.com/support/digital_cameras/specifications/f/",
       "https://www.fujifilm.com/support/digital_cameras/specifications/s/",
       "https://www.fujifilm.com/support/digital_cameras/specifications/t/",
       "https://www.fujifilm.com/support/digital_cameras/specifications/x/",
       "https://www.fujifilm.com/support/digital_cameras/specifications/xp/",
       "https://www.fujifilm.com/support/digital_cameras/specifications/z/"]

for url in urls:
    req = urllib.request.urlopen(url)
    article = req.read().decode()
        
    with open('Fuji.html', 'w') as fo:
        fo.write(article)
            
    article = open('Fuji.html').read()
    soup = BeautifulSoup(article, 'html.parser')
                        
    paragraphs = soup.find_all('span', {"class":"titleText"})
    
    with open('../../currated_data/fujifilm.json', 'a') as fo:
        for title in paragraphs:
            name = title.text.strip()
            if "FinePix" in name:
                line = ""
                name = name.replace("FinePix ","")
                if " / " in name:
                    split_string = name.split(" / ")
                    for name in split_string:
                        print(name)
                        line = "[" + '"' + name + '","' + name[:1] + " "+ name[1:]+ '","' + name[:1] + "-"+ name[1:]  + '"],'
                        if (name[:2] == "JX" or name[:2] == "JV" or name[:2] == "JZ" or
                            name[:2] == "HS" or name[:2] == "SL" or name[:2] == "AV" or name[:2] == "AX"):
                            line = "[" + '"' + name + '","' + name[:2] + " "+ name[2:]+ '","' + name[:2] + "-"+ name[2:]  + '"],'
                        print(line.upper(), file = fo)
                              
                else:
                    print(name)
                    line = "[" + '"' + name + '","' + name[:1] + " "+ name[1:]+ '","' + name[:1] + "-"+ name[1:]  + '"],'
                    if (name[:2] == "JX" or name[:2] == "JV" or name[:2] == "JZ" or
                        name[:2] == "HS" or name[:2] == "SL" or name[:2] == "AV" or name[:2] == "AX"):
                        line = "[" + '"' + name + '","' + name[:2] + " "+ name[2:]+ '","' + name[:2] + "-"+ name[2:]  + '"],'
                    print(line.upper(),file=fo)
                
    os.remove("Fuji.html")
  