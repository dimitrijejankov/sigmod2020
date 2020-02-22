import json
import os

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

with open('currated_data/nikon-models.json') as f:
    nikon_models = json.load(f)

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
            if "NIKON" not in value:
                continue

            match = True
            for model in nikon_models:

                match = True
                for tag in model:

                    # for coolpix we can try three different versions
                    # COOLPIX, COOLPLIX, COOL PIX
                    if tag == "COOLPIX":

                        # check if exists
                        tag = " COOLPIX "
                        if tag in value:
                            continue

                        # check if exists
                        tag = " COOL PIX "
                        if tag in value:
                            continue

                        # check if exists
                        tag = " COOLPLIX "
                        if tag in value:
                            continue

                    tag = " " + tag + " "

                    if tag not in value:
                        match = False
                        break

                if match:
                    found.append(value + str(model))
                    #print(value + str(model))
                    break

            if not match:

                print(value)
                notFound.append(value)

print("Not found : " + str(len(notFound)))
print("Found : " + str(len(found)))

