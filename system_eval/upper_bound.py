import json
import pandas as pd
from sklearn.metrics import confusion_matrix, precision_score, recall_score, accuracy_score
import numpy as np

## Going to use a one vs all strategy - create a confusion matrix for EACH class




labeled_articles = pd.read_csv('./combined_data.csv')  # assumes training dataset is in parent directory - also, probably change format later

def source_to_bias(source):
    file_path = './best_model/best_model.json'   # note - may need to replace .. with . due to IDE issues - also, replace with training DS
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data.get(source, {}).get("mean bias")

def pretty_print(conf_matrix, classes):
    df = pd.DataFrame(conf_matrix, index=['Actual: ' + cls for cls in classes], columns=['Predicted: ' + cls for cls in classes])
    return df

def evaluate(actual, predicted, positive_class):
    '''
    system evaluation - return confusion matrix, precision and recall \n
    Precision = TP / TP + FP (how much of our predictions was truthful) \n
    Recall = TP / TP + FN  (how much of the truth did we predict)
    '''
    actual_binary = np.where(actual == positive_class, 1, 0)
    predicted_binary = np.where(predicted == positive_class, 1, 0)
    conf_matrix = confusion_matrix(actual_binary, predicted_binary)
    true_positives = conf_matrix[0][0]
    false_negatives = conf_matrix[1][0]
    false_positives = conf_matrix[0][1]
    precision = true_positives / (true_positives + false_positives)

    recall = true_positives / (true_positives + false_negatives)
    return conf_matrix, precision, recall





labeled_articles['predicted_bias'] = labeled_articles['source'].apply(source_to_bias)
actual_bias = labeled_articles['bias_text']
predicted_bias = labeled_articles['predicted_bias']


labels = ['left', 'center', 'right']
confusion_matrices = []
precision_arr = []
recall_arr = []
formal_labels = ['Left', 'Center', 'Right']   ## pretty printing




## getting results
for label in labels:
    evaluation_stats = evaluate(actual_bias, predicted_bias, label)
    confusion_matrices.append(evaluation_stats[0])
    precision_arr.append(evaluation_stats[1])
    recall_arr.append(evaluation_stats[2])
    


## pretty printing

for i in range(3):
    print(f"{formal_labels[i]} Precision: {precision_arr[i]}")
    print(f"{formal_labels[i]} Recall: {precision_arr[i]}")
    print("\n")

pretty_matrix_left = pretty_print(confusion_matrices[0], ["Left", "Not Left"])
pretty_matrix_center = pretty_print(confusion_matrices[1], ["Center", "Not Center"])
pretty_matrix_right = pretty_print(confusion_matrices[2], ["Right", "Not Right"])

                               
print(f"Left Confusion Matrix:\n {pretty_matrix_left}\n")
print(f"Center Confusion Matrix:\n {pretty_matrix_center}\n")
print(f"Right Confusion Matrix:\n {pretty_matrix_right}\n")


accuracy = accuracy_score(actual_bias, predicted_bias)
print("Overall Accuracy:", accuracy)


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