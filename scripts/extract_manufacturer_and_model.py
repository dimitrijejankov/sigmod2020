import json
import os
from collections import defaultdict


class SetEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, set):
            return list(obj)
        return json.JSONEncoder.default(self, obj)


cnt_no_manufacturer = 0

cnt_successfully_obtained_model = 0
cnt_no_model = 0

# the found manufactures
manufacturers_dict = defaultdict(set)

for filename in os.listdir('../2013_camera_specs/www.ebay.com'):
    with open('../2013_camera_specs/www.ebay.com/' + filename) as f:
        data = json.load(f)

        if "brand" in data:

            if isinstance(data["brand"], list):
                continue

            brands = data["brand"].upper().replace(' ', '').split(',')
            for brand in brands:
                if 'DIGITALCAMERA' in brand:
                    continue

                if "model" in data:
                    model = data["model"].upper().replace(' ', '')
                    manufacturers_dict[brand].add(model)

                    cnt_successfully_obtained_model += 1
                else:
                    cnt_no_model += 1
        else:
            cnt_no_manufacturer += 1

with open('../extracted_data/manufacturers-with-models.json', 'w') as outfile:
    json.dump(manufacturers_dict, outfile, indent=2, cls=SetEncoder)

print("did not have manufacturer " + str(cnt_no_manufacturer))

print("successfully obtained model " + str(cnt_successfully_obtained_model))
print("did not have model " + str(cnt_no_model))
