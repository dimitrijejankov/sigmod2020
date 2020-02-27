import json
import os

os.chdir('../..')

sites = ['2013_camera_specs/www.walmart.com/',
         '2013_camera_specs/buy.net/',
         '2013_camera_specs/www.buzzillions.com/',
         '2013_camera_specs/www.cambuy.com.au/',
         '2013_camera_specs/buy.net/',
         '2013_camera_specs/cammarkt.com/',
         '2013_camera_specs/www.buzzillions.com/',
         '2013_camera_specs/www.cambuy.com.au/',
         '2013_camera_specs/www.camerafarm.com.au/',
         '2013_camera_specs/www.canon-europe.com/',
         '2013_camera_specs/www.ebay.com/',
         '2013_camera_specs/www.eglobalcentral.co.uk/',
         '2013_camera_specs/www.flipkart.com/',
         '2013_camera_specs/www.garricks.com.au/',
         '2013_camera_specs/www.gosale.com/',
         '2013_camera_specs/www.henrys.com/',
         '2013_camera_specs/www.ilgs.net/',
         '2013_camera_specs/www.mypriceindia.com/',
         '2013_camera_specs/www.pcconnection.com/',
         '2013_camera_specs/www.price-hunt.com/',
         '2013_camera_specs/www.pricedekho.com/',
         '2013_camera_specs/www.priceme.co.nz/',
         '2013_camera_specs/www.shopbot.com.au/',
         '2013_camera_specs/www.shopmania.in/',
         '2013_camera_specs/www.ukdigitalcameras.co.uk/',
         '2013_camera_specs/www.walmart.com/',
         '2013_camera_specs/www.wexphotographic.com/']

with open('currated_data/sony-models.json') as f:
    sony_models = json.load(f)

notFound = []
found = []
for s in sites:
    for filename in os.listdir(s):
        with open(s + filename) as f:

            # load the data
            data = json.load(f)

            # get the value
            value = data['<page title>'].upper()

            # skip if not nikon
            if "SONY" not in value:
                continue

            match = True
            for model in sony_models:

                match = False
                for tag in model:
                    
                    tag1 =  tag + " "
                    if tag1 in value:
                        match = True
                        break
                    
                    tag2 =  tag + ","
                    if tag2 in value:
                        match = True
                        break
                    
                    tag3 =  tag + "/B"
                    if tag3 in value:
                        match = True
                        break
                    
                    tag4 =  tag + "B"
                    if tag4 in value:
                        match = True
                        break
                    
                

                if match:
                    found.append(value + str(model))
                    break

            if not match:

                print(value)
                notFound.append(value)

print("Not found : " + str(len(notFound)))
print("Found : " + str(len(found)))
print("Found : " +str(len(found)/(len(found)+len(notFound))))
