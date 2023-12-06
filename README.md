# Final Project - NLP

Members:

Alex Ali
Corey Lee
Kelven Opoku
Zhinan Dong


## Model

Our model is a **partisan classification system** which seeks to take in the text content of a news article and classify it into one of three classes: left-biased, center-biased, or right-biased. 

The model is a fine-tuned version of RoBERTa. Specifically, it takes 'distil-roberta' and adds a dense hidden layer and a dense classification layer.

## Data 
The final version of the model was trained on 34,000 articles taken from https://github.com/ramybaly/Article-Bias-Prediction which we treated as ground truth. It was validated and tested on 1,500 articles as well which is about a 92-4-4 split. 

In order to pre-process the data, we took two large steps. 

First, we removed the article name from the content of the article. If a line such as "CNN Correspondent" appeared in the content, we would remove "CNN" to prevent the model from learning to just look at the source. This was vital as in the data set, the bias of the source of the news article was extremely highly correlated with the bias of the specific article itself. Our upper bound model was derived by using the article's source to predict the bias of the article itself and achieved ridiculously high accuracy, precision, and recall on all 3 classes. This suggests that the initial data set was not carefully tagged enough - for example, of the 2493 Politico Articles that showed up in the data set, every single one of them was tagged as having a left bias which is highly improbable.

Second, we cleaned the data by removing phrases such as "JUST WATCHED", "MUST WATCH", "Replay More Videos ...". This is important because we could only take the first 512 tokens of the title + article so we wanted a highly representative sample of text from each individual article. 

## Results

In our final training session, the model achieved the following results:

Accuracy: 0.8746666666666667 

metric:  precision    recall    f1-score    support 
left         0.85             0.91      0.88           550 
center   0.87             0.87      0.87           384 
right       0.91             0.84      0.88          566 

