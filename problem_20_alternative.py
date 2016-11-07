'''
Represent a small bilingual lexicon as a Python dictionary
in the following fashion {"merry":"god", "christmas":"jul",
"and":"och", "happy":gott", "new":"nytt", "year":"år"}
and use it to translate your Christmas cards from
English into Swedish. That is, write a function
translate()that takes a list of
English words and returns a list of Swedish words
'''

word_map = {"merry":"god", "christmas":"jul",\
"and":"och", "happy":"gott", "new":"nytt", "year":"år"}

def translate_to_swedish(english_word_list):
    return [word_map.get(k) if word_map.get(k)!=None else k for k in english_word_list]

english_word_list = ["merry","christmas","dear"]
print(translate_to_swedish(english_word_list))
