numbers={"0":"zero","1":"one","2":"two","3":"three","4":"four","5":"five","6":"six","7":"seven","8":"eight","9":"nine"}

docs={
    "D1":"Today she cooked 4 bourek. Later , she added two chamiyya and 1 pizza.",
    "D2":"Five pizza were ready, but 3 bourek burned!",
    "D3":"We only had 8 chamiyya, no pizza, and one tea.",
    "D4":"Is 6 too much? I ate nine bourek lol."

}

def normalize(text):
    text=text.lower()
    cleaned_text=""
    for char in text:
        if char.isalnum() or char.isspace():
            cleaned_text+=char
        else:
            cleaned_text+=" "

    tokens=cleaned_text.split()
    normal_tokens=[]
    for token in tokens:
        if token in numbers:
            normal_tokens.append(numbers[token])

        else:
            normal_tokens.append(token)

    return " ".join(normal_tokens)


for name,doc in docs.items():
    print(name+": ",normalize(doc))
    print("______________________")