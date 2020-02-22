import json
import os

os.chdir('../..')

with open('extracted_data/ebay-manufacturers-with-models.json') as f:
    data_ebay = json.load(f)

sites = ['2013_camera_specs/www.walmart.com/',
         '2013_camera_specs/buy.net/',
         '2013_camera_specs/www.buzzillions.com/',
         '2013_camera_specs/www.cambuy.com.au/']

# we put them here
tmp = []

for s in sites:

    # print the site
    print('For site ' + s)

    # open the file
    for filename in os.listdir(s):
        with open(s + filename) as f:

            assignedBrand = None
            assignedModel = None

            # load the data
            data = json.load(f)
            pageTitle = '<page title>'

            # get the value
            value = data[pageTitle].upper().replace(' ', '')

            # go through the labels
            for manufacturer in data_ebay.keys():
                if manufacturer in value:
                    for model in data_ebay[manufacturer]:
                        if model in value:
                            assignedBrand = manufacturer
                            assignedModel = model

                    if assignedModel is not None:
                        break

            if assignedModel is not None:
                tmp.append((assignedModel, assignedBrand, data[pageTitle]))

            print((assignedModel, assignedBrand, data[pageTitle]))


# do ebay
for filename in os.listdir('2013_camera_specs/www.ebay.com/'):
    with open('2013_camera_specs/www.ebay.com/' + filename) as f:
        data = json.load(f)

        # do we have a page title
        if '<page title>' not in data:
            continue

        # if we do get it
        pageTitle = data['<page title>']

        # do we have a brand
        if 'brand' not in data:
            continue

        # make sure it is not a list
        if isinstance(data['brand'], list):
            continue

        # process the brand
        brands = data['brand'].upper().replace(' ', '').split(',')
        if len(brands) > 1:
            continue

        for brand in brands:

            # make sure we don't have nonsense
            if 'DIGITALCAMERA' in brand:
                continue

            # do we have a model
            if 'model' not in data:
                continue

            # process the model
            model = data['model'].upper().replace(' ', '')

            # skip if there is nonsense in the model
            if 'DIGITALCAMERA' in model:
                continue

            # skip more nonsense
            if model == 'CAMERA' or model == 'DIGITAL' or len(model) == 1:
                continue

            tmp.append((model, brand, pageTitle))
            print((model, brand, pageTitle))

# do shop mania
for filename in os.listdir('2013_camera_specs/www.shopmania.in/'):
    with open('2013_camera_specs/www.shopmania.in/' + filename) as f:
        data = json.load(f)

        # do we have a page title
        if '<page title>' not in data:
            continue

        # if we do get it
        pageTitle = data['<page title>']

        if 'brand' in data:
            if isinstance(data['brand'], list):
                continue

            brands = data['brand'].upper().replace(' ', '').split(',')
            for brand in brands:
                if 'DIGITALCAMERA' in brand:
                    continue

                if 'product name' in data:

                    # make sure it is not a list
                    if isinstance(data['product name'], list):
                        continue

                    # get the model
                    model = data['product name'].upper().replace(brand, '').replace(' ', '')

                    # store the darn thing
                    tmp.append((model, brand, pageTitle))
                    print((model, brand, pageTitle))

with open('extracted_data/title_extraction_data.json', 'w') as outfile:
    json.dump(list(tmp), outfile, indent=2)
