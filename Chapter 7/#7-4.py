"""
Chapter 7

Exercise 4: Large Shirts
"""
# A default value was set to the parameter
def make_shirt(size='large', message='I love Python'):
    """Summarize the shirt that's going to be made."""
    print("\nHello there! I'm all set to create your " + size + " t-shirt.")
    print('The message you chose, "' + message + '", will make your shirt stand out!')

#if in any instances the parameters were set to a default value and the user wants to change the certain size or message, the name of the parameter should be mentioned in the program 
# Ceating a T-shirt with the default message
make_shirt()

# changing the first parameter or the size of the shirt
make_shirt(size='medium')

# Changing both of the parameters or the size and message of the shirt
make_shirt(size='small', message='Assigned!')
