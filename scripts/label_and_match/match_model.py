import json
import os

os.chdir('../../')

cnt_brand_matches = 0
cnt_model_matches = 0

with open('extracted_data/manufacturers-with-models-shopmania.json') as shopmania_models, \
        open('extracted_data/ebay-manufacturers-with-models.json') as ebay_models, \
        open('extracted_data/manufacturers-cleaned.json') as brands:
    data_brands = json.load(brands)

    data_shopmania = json.load(shopmania_models)
    data_ebay = json.load(ebay_models)

    for brand in data_brands:
        if brand in data_ebay and brand in data_shopmania:
            cnt_brand_matches += 1
        else:
            continue

        for model in data_ebay[brand]:
            if model in data_shopmania[brand]:
                cnt_model_matches += 1

print('brand matches: ' + str(cnt_brand_matches))
print('model matches: ' + str(cnt_model_matches))
