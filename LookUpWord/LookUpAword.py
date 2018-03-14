import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        return "Did you mean %s instead?" % get_close_matches(word, data.keys())[0]
    else:
        return "The word doesn't exist. Please Try again"

word = input("Enter word: ")

print(translate(word))

while translate(word) !='quiiiit':
    
    word = input("Enter word: ")
    print(translate(word))

