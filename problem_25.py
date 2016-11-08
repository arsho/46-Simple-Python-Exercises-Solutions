'''
In English, the present participle is formed by adding the
suffix -ing to the infinite form: go -> going. A simple set
of heuristic rules can be given as follows:

a. If the verb ends in e, drop the e and add ing
(if not exception: be, see, flee, knee, etc.)
b. If the verb ends in ie, change ie to y and add ing
c. For words consisting of consonant-vowel-consonant, double the final
letter before adding ing
d. By default just add ing

Your task in this exercise is to define a function
make_ing_form()which given a verb in infinitive form
returns its present participle form. Test your function
with words such as lie, see, move and hug.
However, you must not expect such
simple rules to work for all cases
'''
import string
def make_ing_form(passed_string):
    passed_string = passed_string.lower()
    letter = list(string.ascii_lowercase)
    vowel = ['a','e','i','o','u']
    consonant = [c for c in letter if c not in vowel]
    exception = ['be', 'see', 'flee', 'knee', 'lie']
    if passed_string.endswith('e'):
        if passed_string in exception:
            return passed_string + 'ing'
        else:
            passed_string = passed_string[:-1]
            return passed_string + 'ing'

    elif passed_string.endswith('ie'):
        passed_string = passed_string[:-2]
        return passed_string + 'ying'

    elif passed_string[-1] in consonant and passed_string[-2] in vowel and passed_string[-3] in consonant:
        passed_string += passed_string[-1]
        return passed_string + 'ing'
    else:
        return passed_string + 'ing'

verb = ['lie', 'see', 'move', 'hug', 'study']
for item in verb:
    print(make_ing_form(item))
        
