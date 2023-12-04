import json
import pandas as pd
from system_eval import evaluate, print_results

# Upper Bound Model Uses Article Source to Predict Bias


def source_to_bias(source):
    file_path = './models/upper_bound_model_data/upper_bound_model.json'   # note - may need to replace .. with . due to IDE issues - also, replace with training DS
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data.get(source, {}).get("mean bias")

def main():
    labeled_articles = pd.read_csv('./combined_data.csv')  # assumes training dataset is in parent directory - also, probably change format later

    labeled_articles['predicted_bias'] = labeled_articles['source'].apply(source_to_bias)
    actual_bias = labeled_articles['bias_text']
    predicted_bias = labeled_articles['predicted_bias']

    confusion_matrices, precision_arr, recall_arr, accuracy = evaluate(actual_bias, predicted_bias)
    print_results(confusion_matrices, precision_arr, recall_arr, accuracy)

if __name__ == "__main__":
    main()

'''
OUTPUT:
Left Precision: 0.999877795429549
Left Recall: 0.999877795429549

Center Precision: 0.9985414562997869
Center Recall: 0.9985414562997869

Right Precision: 1.0
Right Recall: 1.0

Left Confusion Matrix:
                   Predicted: Left  Predicted: Not Left
Actual: Left                24546                    3
Actual: Not Left               39                12966

Center Confusion Matrix:
                     Predicted: Center  Predicted: Not Center
Actual: Center                  26700                     39
Actual: Not Center                  3                  10812

Right Confusion Matrix:
                    Predicted: Right  Predicted: Not Right
Actual: Right                 23820                     0
Actual: Not Right                 0                 13734

Overall Accuracy: 0.9988816104809075
'''