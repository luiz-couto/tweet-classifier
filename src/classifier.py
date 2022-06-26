from datetime import datetime
import pandas as pd
import numpy as np
import pickle
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

VERSION = "v0.0.2"

def main():
    training = pd.read_csv("../datasets/training.csv", sep=";", usecols=["text", "country_code"])
    tweets = []
    targets = []

    for _, row in training.iterrows():
        tweets.append(row["text"])
        if row["country_code"] == "US":
            targets.append(1)
        else:
            targets.append(0)

    text_clf = Pipeline([
        ('vect', CountVectorizer()),
        ('tfidf', TfidfTransformer()),
        ('clf', MultinomialNB()),
    ])

    text_clf.fit(tweets, targets)

    data = { 'model': text_clf, 'model_date': datetime.now().timestamp() }

    pickle.dump(data, open(VERSION, "wb" ))

    # Now begins the performance test

    data = pickle.load(open(VERSION, "rb" ))

    clf = data["model"]

    test = pd.read_csv("../datasets/test.csv", sep=";", usecols=["text", "country_code"])
    test_tweets = []
    expected = []
    for _, row in test.iterrows():
        test_tweets.append(row["text"])
        if row["country_code"] == "US":
            expected.append(1)
        else:
            expected.append(0)
    
    predicted = clf.predict(test_tweets)
    acc = np.mean(predicted == expected)
    print(acc)



if __name__ == "__main__":
    main()