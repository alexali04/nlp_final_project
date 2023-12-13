import json
import pandas as pd
from sklearn.metrics import classification_report


def main():
    labeled_articles = pd.read_csv('./train.csv')  # labeled articles must be in 
    actual_bias = labeled_articles['bias']
    predicted_bias = pd.DataFrame([2] * len(actual_bias)) # lower-bound model predicts right for each prediction. 

    report = classification_report(actual_bias, predicted_bias, target_names=['left', 'center', 'right'])
    print(report)

if __name__ == "__main__":
    main()


'''
OUTPUT:
precision    recall  f1-score   support

        left       0.00      0.00      0.00     11747
      center       0.00      0.00      0.00      9823
       right       0.37      1.00      0.54     12430

    accuracy                           0.37     34000
   macro avg       0.12      0.33      0.18     34000
weighted avg       0.13      0.37      0.20     34000

'''
