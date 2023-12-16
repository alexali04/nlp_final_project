import pandas as pd
from sklearn.metrics import accuracy_score, precision_recall_fscore_support


train_file = 'train_full.csv'
test_file = 'test_full.csv'

train_data = pd.read_csv(train_file)
test_data = pd.read_csv(test_file)



most_common_bias_per_source = train_data.groupby('source')['bias'].agg(lambda x: x.value_counts().idxmax())

model = most_common_bias_per_source.to_dict()

test_data['predicted_bias'] = test_data['source'].map(model)

test_data['predicted_bias'].fillna((test_data['bias'] + 1) % 3, inplace=True) ## it will be wrong for sources unseen


y_true = test_data['bias']
y_pred = test_data['predicted_bias']

accuracy = accuracy_score(y_true, y_pred)

precision, recall, f1_score, _ = precision_recall_fscore_support(y_true, y_pred, average='macro')

print(f"Accuracy: {accuracy}")
print(f"Precision: {precision}")
print(f"Recall: {recall}")
print(f"Macro F1 Score: {f1_score}")



'''
Accuracy: 0.9946666666666667
Precision: 0.9944633431443565
Recall: 0.9938415404040404
Macro F1 Score: 0.9941412891021301
'''