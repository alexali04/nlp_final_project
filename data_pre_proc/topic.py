import os
import json

directory = './data_pre_proc/data_1/jsons'

topics = {}
for json_file in os.listdir(directory):
    if json_file.endswith('.json'):
        with open(os.path.join(directory, json_file)) as f:
            article = json.load(f)

            topic = article['topic']
            bias = article['bias']
            if topic not in topics.keys():
                topics[topic] = {'count': 0, 0: 0, 1: 0, 2: 0}
            
            topics[topic][bias] += 1
            topics[topic]['count'] += 1


sorted_topics = dict(sorted(topics.items(), key=lambda item: item[1]['count'], reverse=True))


with open('topics_bias.json', 'w') as f:
    json.dump(sorted_topics, f, indent=4)

