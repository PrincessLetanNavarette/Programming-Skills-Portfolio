"""
Chapter 7

Exercise 3: T-shirt
"""
#in this exercise the program greets and informs the user that their shirt are ready to be made.
def make_shirt(size, message):
    """Summarize the shirt that's going to be made."""
    print("\nHello there! I'm all set to create your " + size + " t-shirt.")
    print('Your chosen message, "' + message + '", will add a touch of uniqueness to your shirt!')

#These are the sizes and messages that the user wants to put in their shirt
make_shirt('small', 'Awakened!') #since the two parameters of size and message wer already present, we dont need to put it again.
make_shirt(message="Aligned.", size='medium')