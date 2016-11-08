'''
Represent a small bilingual lexicon as a Python dictionary
in the following fashion:

{"merry":"god", "christmas":"jul", "and":"och", "happy":gott",
"new":"nytt", "year":"år"}

and use it to translate your Christmas cards from
English into Swedish. Use the higher order function map()
to write a function translate()that takes a list of English
words and returns a list of Swedish words.
'''

# I added some modification for if there are words not in dic

def translate(list_a):
    dic = {"merry":"god", "christmas":"jul", "and":"och",\
           "happy":"gott","new":"nytt", "year":"år"}
    return list(map(lambda x:dic[x] if x in dic else False, list_a))
                # "if dict.get(x)" - would work just fine
                # map must return list of same number
                # That's why the else part is needed
            

ab = ['merry','and','new','sad']  # 'sad' not in the dictionary
print(translate(ab))
