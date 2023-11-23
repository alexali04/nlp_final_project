'''
This file will go through /data/jsons and count the number of times a source appears and sum the numerical bias of each source.
Left is represented as 0, center is 1, and right is 2. 

How this is done is by averaging the political bias of the articles over the entire dataset.

So if NYT has 3 center articles, 2 left articles, and 1 right article
'''

import os  # stdlib
import json

sum_bias = {}
num_bias = {}

mode_bias = {}

directory = '../data_1/jsons'

counter = 0
politico_counter = 0
for json_file in os.listdir(directory):
    if json_file.endswith('.json'):
        counter += 1
        
        with open(os.path.join(directory, json_file)) as f:

            #  getting aggregate 

            article = json.load(f)
            source = article['source']
            bias = article['bias']
            bias_text = article['bias_text']




            # if source == 'Politico':
            #     politico_counter += 1
            #     print(directory + json_file + " " + str(article['bias']))

            sum_bias[source] = sum_bias[source] + bias if source in sum_bias.keys() else bias
            num_bias[source] = num_bias[source] + 1 if source in num_bias.keys() else 1

            if source not in mode_bias.keys():
                mode_bias[source] = {}
                mode_bias[source]['left'] = 0
                mode_bias[source]['right'] = 0
                mode_bias[source]['center'] = 0
                mode_bias[source][bias_text] = 1
            else:
                mode_bias[source][bias_text] += 1





ouput_files = ['num_bias.json', 'sum_bias.json', 'mode_bias.json']
relevant_dicts = [num_bias, sum_bias, mode_bias]

for i in range(len(relevant_dicts)):
    with open(ouput_files[i], 'w') as output:
        json.dump(relevant_dicts[i], output, indent=4)
        



