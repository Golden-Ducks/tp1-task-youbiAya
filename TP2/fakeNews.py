import pandas as pd
import re
import nltk
from nltk.corpus import stopwords

nltk.download("stopwords")
stop_words=set(stopwords.words("english"))

fake=pd.read_csv(r"C:\Users\youbi\archive\News _dataset\Fake.csv")
true=pd.read_csv(r"C:\Users\youbi\archive\News _dataset\True.csv")

docs=fake["text"][:5].tolist()+true["text"][:5].tolist()
labels=[0]*5+[1]*5

def clean(text):
    text=text.lower()
    text=re.sub(r'[.,!?;:"()\[\]]','',text)
    numbers={"0":"zero","1":"one","2":"two","3":"three","4":"four","5":"five","6":"six","7":"seven","8":"eight","9":"nine"}
    
    for digit,word in numbers.items():
        text=re.sub(r'\b'+ digit + r'\b', word,text)

    text=re.sub(r'\s+',' ',text).strip()

def preprocess(all_docs):
    processed=[]
    for doc in all_docs:
        words=clean(doc).split()
        words=[w for w in words if w not in stop_words]
        processed.append(words)

    return processed

def get_vocab(docs):
    vocab=[]
    for doc in docs:
        for word in doc:
            if word not in vocab:
                vocab.append(word)
    return vocab

def make_vec(docs,vocab):
    vectors=[]
    for doc in docs:
        vec=[1 if word in doc else 0 for word in vocab]
        vectors.append(vec)
    return vectors

processed_docs=preprocess(docs)
vocab=get_vocab(processed_docs)
vectors=make_vec(processed_docs,vocab)
print("Vocabulary size:",len(vocab))
print("First 5 words:",vocab[:5])
print("labels sample:",labels[:3])

for i,doc in enumerate(processed_docs[:1]):
    print("First 5 words in doc:",doc[:5])
    print("First 5 entries in vec:",vectors[i][:5])
