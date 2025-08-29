import json

data = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data

    else:
        return "pugger your paw steps on wrong keys"


word = input("Enter the word you want to search: ")
output = translate(word)
print(output)
