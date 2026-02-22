import re 

with open("task2.txt","r",encoding="utf-8") as f:
    text=f.read()

text=text.lower()
text=text.replace("’","'").replace("“",'"').replace("”",'"')  

contractions={
    "i'm":"i am",
    "it's":"it is",
    "don't":"do not",
    "didn't":"did not",
    "won't":"will not",
    "can't":"can not",
    "i'll":"i will",
    "he's":"he is",
    "she's":"she is",
    "they're":"they are",
    "we're":"we are",
    "wasn't":"was not",
    "weren't":"were not",
    "aren't":"are not",
    "isn't":"is not",
}

for short,long in contractions.items():
    text=text.replace(short,long)


numbers={
    "0":"zero","1":"one","2":"two","3":"three","4":"four","5":"five","6":"six","7":"seven","8":"eight","9":"nine"

}    

for digit,word in numbers.items():
    text.re.sub(r'\b' + digit + r'\b',word,text)

text=re.sub(r'[^a-z\s]',' ',text)
text=re.sub(r'\s+',' ',text).strip()

print(text)
