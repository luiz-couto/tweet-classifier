import pandas as pd
import numpy as np
import pickle
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

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

    pickle.dump(text_clf, open("clf.p", "wb" ))

    # Now begins the performance test

    clf = pickle.load(open("clf.p", "rb" ))

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