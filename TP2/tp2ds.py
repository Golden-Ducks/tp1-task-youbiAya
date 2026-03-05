import csv
import spacy
import re

nlp=spacy.load("en_core_web_sm")

fake_path = r'C:\Users\youbi\archive\News _dataset\Fake.csv'
true_path = r'C:\Users\youbi\archive\News _dataset\True.csv'

def load_ds(fake_path,true_path):
    texts=[]
    labels=[]

    with open(fake_path,encoding="utf-8") as f:
        reader=csv.DictReader(f)
        for row in reader:
            texts.append(row["text"])
            labels.append(0)

    with open(true_path,encoding="utf-8") as f:
        reader=csv.DictReader(f)
        for row in reader:
            texts.append(row["text"])
            labels.append(1)   

    return texts,labels



texts,labels=load_ds(fake_path,true_path)
texts=texts[:2000]
labels=labels[:2000]

def normalize(text):
    text = text.lower()
    text = re.sub(r"[^\w\s]", "", text)
    tokens = text.split()
    return tokens

processed_texts=[]
for text in texts:
    tokens=normalize(text)
    processed_texts.append(tokens)

vocab_set=set()
for tokens in processed_texts:
    for word in tokens:
        vocab_set.add(word)

vocab=list(vocab_set)
def bow(tokens,vocab):
    token_set=set(tokens)
    vector=[]
    for word in vocab:
        if word in token_set:
            vector.append(1)
        else:
            vector.append(0)
    return vector

X=[]
for tokens in processed_texts:
    vector=bow(tokens,vocab)
    X.append(vector)

print(" ORIGINAL TEXT :")
print(texts[0][:300])

print("\n AFTER NORMALIZATION :")
print(processed_texts[0][:20])

print("\nVocabulary size:", len(vocab))
print("First 20 words in vocabulary:")
print(vocab[:20])

print("\n BOOLEAN BOW VECTOR (1st doc)")
print(X[0][:20])


for word in processed_texts[0][:10]:
    index = vocab.index(word)
    print(word, "->", X[0][index])


