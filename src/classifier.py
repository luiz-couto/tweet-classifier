import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

def extractFeatures(text):
    count_vect = CountVectorizer()
    tfidf_transformer = TfidfTransformer()
    X_new_counts = count_vect.fit_transform(["text"])
    X_new_tfidf = tfidf_transformer.transform(X_new_counts)
    return X_new_tfidf



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

    # Now begins the performance test

    test = pd.read_csv("../datasets/test.csv", sep=";", usecols=["text", "country_code"])
    test_tweets = []
    expected = []
    for _, row in test.iterrows():
        test_tweets.append(row["text"])
        if row["country_code"] == "US":
            expected.append(1)
        else:
            expected.append(0)
    
    predicted = text_clf.predict(test_tweets)
    acc = np.mean(predicted == expected)
    print(acc)



if __name__ == "__main__":
    main()