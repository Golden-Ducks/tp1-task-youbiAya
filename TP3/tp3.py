import numpy as np
import spacy
import contractions
from sklearn.cluster import KMeans
from sklearn.metrics import accuracy_score, precision_score

nlp = spacy.load("en_core_web_sm")

print("_______  task1 ________")


docs1 = [
    "The gold medal price is high effort",
    "Winning a gold medal needs a high jump",
    "Market for a gold medal is a trade of sweat",
    "The athlete will trade all for a gold medal"
]

docs2 = [
    "The gold bars price is high today",
    "Investing in gold bars needs a high rate",
    "Market for gold bars is a trade of money",
    "The bank will trade all for gold bars"
]

all_docs = docs1 + docs2
y_true = [0,0,0,0,1,1,1,1]


def preprocess(text):
    text = text.lower()
    text = contractions.fix(text)
    doc = nlp(text)

    words = []
    for t in doc:
        if not t.is_stop and not t.is_punct:
            words.append(t.lemma_)
    return words


def build_vectors(docs, n):
    tokenized = []
    for d in docs:
        tokenized.append(preprocess(d))

    
    vocab = []
    for tokens in tokenized:
        for i in range(len(tokens)-n+1):
            ng = " ".join(tokens[i:i+n])
            if ng not in vocab:
                vocab.append(ng)

    vocab = sorted(vocab)

    
    X = []
    for tokens in tokenized:
        doc_ngrams = []
        for i in range(len(tokens)-n+1):
            doc_ngrams.append(" ".join(tokens[i:i+n]))

        vec = []
        for v in vocab:
            if v in doc_ngrams:
                vec.append(1)
            else:
                vec.append(0)

        X.append(vec)

    return X


for n in [1, 2]:
    X = build_vectors(all_docs, n)

    km = KMeans(n_clusters=2, random_state=42, n_init=10)
    km.fit(X)

    labels = km.labels_

    print(f"\n{n}-gram clusters:", labels)
    print("Accuracy :", round(accuracy_score(y_true, labels), 2))
    print("Precision:", round(precision_score(y_true, labels, zero_division=0), 2))


print("\n______task2__________")

D1 = "I love cats"
D2 = "Cats are chill"
D3 = "I am late"

docs = [D1, D2, D3]

def pad(tokens):
    return ["<s>"] + tokens + ["</s>"]

def get_windows(tokens):
    res = []
    for i in range(len(tokens)-2):
        res.append(tokens[i] + " " + tokens[i+1] + " " + tokens[i+2])
    return res


all_windows = []

for d in docs:
    t = preprocess(d)
    t = pad(t)
    w = get_windows(t)
    all_windows.append(w)

vocab = []
for wlist in all_windows:
    for w in wlist:
        if w not in vocab:
            vocab.append(w)

vocab = sorted(vocab)

print("\n sorted vocab:")
for i in range(len(vocab)):
    print(i, ":", '"' + vocab[i] + '"')

print()

for d, wlist in zip(docs, all_windows):
    vec = []
    for v in vocab:
        if v in wlist:
            vec.append(1)
        else:
            vec.append(0)

    print(f"{d:20s} -> {vec}")