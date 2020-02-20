import json
import os

os.chdir('../../')

cnt = 0
# the found manufactures
manufactures = set()
for filename in os.listdir('2013_camera_specs/www.ebay.com'):
    with open('2013_camera_specs/www.ebay.com/' + filename) as f:
        data = json.load(f)

        if "brand" in data:

            if isinstance(data["brand"], list):
                continue

            brands = data["brand"].upper().replace(' ', '').split(',')
            for brand in brands:
                if 'DIGITALCAMERA' in brand:
                    continue

                manufactures.add(brand)
        else:
            cnt += 1

with open('extracted_data/manufacturers-cleaned.json', 'w') as outfile:
    json.dump(list(manufactures), outfile, indent=2)

print("did not have manufacturer " + str(cnt))
