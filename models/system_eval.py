import json
import pandas as pd
from sklearn.metrics import confusion_matrix, precision_score, recall_score, accuracy_score
import numpy as np

## Going to use a one vs all strategy - create a confusion matrix for EACH class

def evaluate(actual, predicted):
    '''
    system evaluation - return confusion matrix, precision and recall \n
    Precision = TP / TP + FP (how much of our predictions was truthful) \n
    Recall = TP / TP + FN  (how much of the truth did we predict)
    '''
    labels = ['left', 'center', 'right']
    confusion_matrices = []
    precision_arr = []
    recall_arr = []

    for label in labels:
        actual_binary = np.where(actual == label, 1, 0)
        predicted_binary = np.where(predicted == label, 1, 0)
        conf_matrix = confusion_matrix(actual_binary, predicted_binary)
        true_positives = conf_matrix[0][0]
        false_negatives = conf_matrix[1][0]
        false_positives = conf_matrix[0][1]
        precision = true_positives / (true_positives + false_positives)

        recall = true_positives / (true_positives + false_negatives)

        confusion_matrices.append(conf_matrix)
        precision_arr.append(precision)
        recall_arr.append(recall)

    accuracy = accuracy_score(actual, predicted)
    
    return confusion_matrices, precision_arr, recall_arr, accuracy


def pretty_print(conf_matrix, classes):
    df = pd.DataFrame(conf_matrix, index=['Actual: ' + cls for cls in classes], columns=['Predicted: ' + cls for cls in classes])
    return df


def print_results(confusion_matrices, precision_arr, recall_arr, accuracy):
    formal_labels = ['Left', 'Center', 'Right'] 
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

    print("Overall Accuracy:", accuracy)
