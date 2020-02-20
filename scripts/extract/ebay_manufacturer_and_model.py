import json
import os
from collections import defaultdict


class SetEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, set):
            return list(obj)
        return json.JSONEncoder.default(self, obj)


os.chdir('../../')

cnt_no_manufacturer = 0
cnt_successfully_obtained_model = 0
cnt_no_model = 0

# the found manufactures with their set of models
manufacturers_dict = defaultdict(set)

sites = [
    ['2013_camera_specs/www.ebay.com/', ['brand', 'model']]
    # odradi shopmania sledece, imas 'brand' i 'product name' iz kog moras obrisati brend
    # ['../2013_camera_specs/www.walmart.com/', ['<page title>']],
    # ['../2013_camera_specs/buy.net/', ['<page title>']],
    # ['../2013_camera_specs/www.buzzillions.com/', ['<page title>']],
    # ['../2013_camera_specs/www.cambuy.com.au/', ['<page title>']]
]

for s in sites:
    for filename in os.listdir(s[0]):
        with open(s[0] + filename) as f:
            data = json.load(f)

            if s[1][0] in data:

                if isinstance(data[s[1][0]], list):
                    continue

                brands = data[s[1][0]].upper().replace(' ', '').split(',')
                for brand in brands:
                    if 'DIGITALCAMERA' in brand:
                        continue

                    if s[1][1] in data:
                        model = data[s[1][1]].upper().replace(' ', '')
                        manufacturers_dict[brand].add(model)

                        cnt_successfully_obtained_model += 1
                    else:
                        cnt_no_model += 1

            else:
                cnt_no_manufacturer += 1

with open('extracted_data/manufacturers-with-models.json', 'w') as outfile:
    json.dump(manufacturers_dict, outfile, indent=2, cls=SetEncoder)

print("did not have manufacturer " + str(cnt_no_manufacturer))

print("successfully obtained model " + str(cnt_successfully_obtained_model))
print("did not have model " + str(cnt_no_model))
