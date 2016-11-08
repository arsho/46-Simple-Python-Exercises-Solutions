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

word_map = {"merry":"god", "christmas":"jul", "and":"och",\
       "happy":"gott","new":"nytt", "year":"år"}

def translate(word_list):
    return list(map(lambda x:word_map.get(x) if word_map.get(x)!=None else x,word_list))
            

word_list = ['merry','and','new','nothing']  # 'nothing' not in the dictionary
print(translate(word_list))
