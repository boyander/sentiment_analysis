#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sklearn
import csv
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

# Read extracted twitts
twitts = []
with open('twitts.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in reader:
        twitts.append(unicode(row[1].decode('utf8')))
print twitts[0:5]


# Calculate TF-IDF

vectorizer = TfidfVectorizer(analyzer='word', ngram_range=(1,3), min_df = 0, stop_words = 'english')
X = vectorizer.fit_transform(twitts)
indices = np.argsort(vectorizer.idf_)[::-1]
features = vectorizer.get_feature_names()

top_n = 10
top_features = [features[i] for i in indices[:top_n]]
least_features = [features[i] for i in indices[-top_n:]]

print "=== TOP FEATURE VECTORS ==="
for term in top_features:
    print term
print "=== LEAST FEATURE VECTORS ==="
for term in least_features:
    print term
