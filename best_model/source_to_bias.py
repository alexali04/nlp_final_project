import json
import math

'''
here we will find the mean, the median, and the mode of the article biases
'''

source_bias = {}
num_to_bias = {0: 'left', 1: 'center', 2: 'right'}

with open("num_bias.json") as count, open("sum_bias.json") as s2b, open("mode_bias.json") as mode:
    num_bias = json.load(count)  # total number of times source shows up in data set
    sum_bias = json.load(s2b)  # aggregate sum of bias
    mode_bias = json.load(mode)  # number of left, right, and center articles
    
    for source, bias in sum_bias.items():
        source_bias[source] = {}
        bias /= num_bias[source]
        num = int(math.floor(bias + 0.5))
        source_bias[source]['mean bias'] = num_to_bias[num]
        sorted_source_bias = list(sorted(mode_bias[source].items(), key = lambda x: (x[1], x)))
        source_bias[source]['mode bias'] = sorted_source_bias[2][0]
        # mode_bias[source].setdefault(0)
        num_appearances = num_bias[source]

        if num_appearances <= mode_bias[source]['left']:
            source_bias[source]['median'] = 'left'
        elif num_appearances <= mode_bias[source]['left'] + mode_bias[source]['center']:
            source_bias[source]['median'] = 'center'                     
        else:
            source_bias[source]['median'] = 'right'


with open('basline_model.json', 'w') as output:
    json.dump(source_bias, output, indent=4)
    
