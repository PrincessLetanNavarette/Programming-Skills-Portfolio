"""
Chapter 5

Exercise 3: Glossary 2
"""
# every key presented in the glossary below are programming terms which associated with their own definition and meaning. these things are also called values of  the specific keys in the dictionary.
glossary = {
    'string': 'A sequence of characters, usually used to represent text in a program.',
    'integer': 'A whole number without a decimal point.',
    'loop': 'A control structure that repeats a block of code as long as a specified condition is met.',
    'list': 'A collection of items in a particular order.',
    'dictionary': 'A collection of key-value pairs.',
    'Float': 'A number with a decimal point.',
    'Boolean': 'A data type with only two possible values, usually "true" or "false."',
    'Comment': 'Text within the code that is not executed and is used for documentation.',
    'Algorithm': 'A step-by-step procedure for solving a problem or performing a task.',
    'Debugging': 'The process of identifying and fixing errors in your code.'}

# in this exercise, the task is to print every keys and values in the 'glossary' dictionary hence the use for 'for' helps to us to repeat the same instruction which is to print the definitions and word in the glossary. 
for word, definition in glossary.items(): 
    print("\n" + word.title() + ": " + definition)