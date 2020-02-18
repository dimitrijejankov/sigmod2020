import json
import os

cnt = 0
# the found manufactures
manufactures = set()
for filename in os.listdir('2013_camera_specs/www.ebay.com'):
    with open('2013_camera_specs/www.ebay.com/' + filename) as f:
        data = json.load(f)

        if "brand" in data:

            if isinstance(data["brand"], list):
                for x in data["brand"]:
                    brand = x.upper().replace(' ', '')
                    manufactures.add(brand)
                continue

            brand = data["brand"].upper().replace(' ', '')
            manufactures.add(brand)
        else:
            cnt += 1

with open('manufacturers.json', 'w') as outfile:
    json.dump(list(manufactures), outfile)

print("did not have manufacturer " + str(cnt))