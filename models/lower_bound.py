import json
import pandas as pd
from system_eval import evaluate, print_results


def main():
    labeled_articles = pd.read_csv('./combined_data.csv')  # labeled articles must be in 
    actual_bias = labeled_articles['bias_text']
    predicted_bias = pd.DataFrame(["right"] * len(actual_bias)) # lower-bound model predicts right for each prediction. 

    confusion_matrices, precision_arr, recall_arr, accuracy = evaluate(actual_bias, predicted_bias)
    print_results(confusion_matrices, precision_arr, recall_arr, accuracy)

if __name__ == "__main__":
    main()


'''
OUTPUT:
Left Precision: 1.0
Left Recall: 1.0


Center Precision: 1.0
Center Recall: 1.0


Right Precision: 0.0
Right Recall: 0.0


Left Confusion Matrix:
                   Predicted: Left  Predicted: Not Left
Actual: Left                24549                    0
Actual: Not Left            13005                    0

Center Confusion Matrix:
                     Predicted: Center  Predicted: Not Center
Actual: Center                  26739                      0
Actual: Not Center              10815                      0

Right Confusion Matrix:
                    Predicted: Right  Predicted: Not Right
Actual: Right                     0                 23820
Actual: Not Right                 0                 13734

Overall Accuracy: 0.3657133727432497
'''
