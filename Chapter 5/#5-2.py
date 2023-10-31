"""
Chapter 5

Exercise 2: Glossary
"""

#d ictionary that contions five keys of words with their own definition as their value.
glossary = {
    'string': 'A sequence of characters, usually used to represent text in a program.',
    'integer': 'A whole number without a decimal point.',
    'loop': 'A control structure that repeats a block of code as long as a specified condition is met.',
    'list': 'A collection of items in a particular order.',
    'dictionary': 'A collection of key-value pairs.'}

# whichever key or word you put from the glossary will be printed together with its meaning. 
word = 'string'
print("\n" + word.title() + ": " + glossary[word])

word = 'integer'
print("\n" + word.title() + ": " + glossary[word])

word = 'loop'
print("\n" + word.title() + ": " + glossary[word])

word = 'list'
print("\n" + word.title() + ": " + glossary[word])

word = 'dictionary'
print("\n" + word.title() + ": " + glossary[word])
#in this exercise, the task is to print every word in the glossary, therefore every key  in the glossary was input.
