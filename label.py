import json
import os

with open('./manufacturers-cleaned.json') as f:
    labels = json.load(f)

sites = [['2013_camera_specs/www.walmart.com/', ['<page title>']],
         ['2013_camera_specs/buy.net/', ['<page title>']],
         ['2013_camera_specs/www.buzzillions.com/', ['<page title>']],
         ['2013_camera_specs/www.cambuy.com.au/', ['<page title>']]
         ]

x = 0
for s in sites:

    # print the site
    print('For site ' + s[0])

    # open the file
    for filename in os.listdir(s[0]):
        with open(s[0] + filename) as f:

            assignedLabel = None

            # load the data
            data = json.load(f)
            for att in s[1]:

                # get the value
                value = data[att].upper().replace(' ', '')

                # go through the labels
                for label in labels:
                    if label in value:
                        assignedLabel = label

                if assignedLabel is not None:
                    break

            if assignedLabel is None:
                x += 1
            print(s[0] + filename + " " + str(assignedLabel))


print('not labeled ' + str(x))
