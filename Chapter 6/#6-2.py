"""
Chapter 6

Exercise 2:Movie Tickets
"""

#This exercise centers on setting fair prices based on age, ensuring equity across different age groups.
while True:
    age = input("\nPlease enter your age (or type 'quit' to exit): ")

    #the program asks the user for an input which later on help to determine as to how much the movie ticket's gonna be
    if age.lower() == 'quit':
        break  # Exit the loop if the user types 'quit'
    
    age = int(age)  # Convert user input to an integer
    
    # these are the conditions and basis for giving the price when the user puts an input
    if age < 3:
        print("\nYour ticket is free. Enjoy the movie!")
    elif 3 <= age <= 12:
        print("\nYour ticket is $10. Enjoy the movie!")
    else:
        print("\nYour ticket is $15. Enjoy the movie!")
    # the loop will only break if the user decided to quit 