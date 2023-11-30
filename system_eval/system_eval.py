import json
import pandas as pd
from sklearn.metrics import confusion_matrix, precision_score, recall_score, accuracy_score


def source_to_bias(source):
    file_path = 'best_model/best_model.json'
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data.get(source, {}).get("mean bias")

labeled_articles['predicted_bias'] = labeled_articles['source'].apply(source_to_bias)

actual = labeled_articles['bias_text']
predicted = labeled_articles['predicted_bias']

precision = precision_score(actual, predicted, average='weighted')
recall = recall_score(actual, predicted, average='weighted')
accuracy = accuracy_score(actual, predicted)

conf_matrix = confusion_matrix(actual, predicted, labels=["left", "right", "center"])

print(f"Precision: {precision}")
print(f"Recall: {recall}")
print(f"Accuracy: {accuracy}")

print(conf_matrix)