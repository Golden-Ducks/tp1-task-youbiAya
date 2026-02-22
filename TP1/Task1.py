with open("task1.txt","r",encoding="utf-8") as f:
    text=f.read()


text=text.lower()

punctuation=".,;:!?\"'()[]{}<>"
symbols="@#$%^&*_+=|\\/~"
noise="-"
cleaned_text=""

for char in text:
    if char.isalpha() or char.isspace():
        cleaned_text+=char

    elif char not in punctuation and char not in symbols and char !=noise and not char.isdigit():
        cleaned_text+=" "   


cleaned_text= " ".join(cleaned_text.split())
print(cleaned_text)

