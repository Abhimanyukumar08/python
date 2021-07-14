import json
from difflib import get_close_matches
 #............DICTIONARY.............#

data = json.load(open("C:\Desktop\Desktop\program file\python course\Python projects\data.json"))

def change(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    
    elif len(get_close_matches(word,data.keys()))>0:
        print("Did you mean %s instead" %get_close_matches(word,data.keys())[0])
        decide = input("press y for yes or n for no :")
        if decide == "y":
            return data[get_close_matches(word,data.keys())[0]]
    else:
        print("You have enter the worng word , please try again ")




    

        

word = input("enter the word :")
output = change(word)

if type(output)==list:
    for item in output:
        print(item)
else:
    print(output)