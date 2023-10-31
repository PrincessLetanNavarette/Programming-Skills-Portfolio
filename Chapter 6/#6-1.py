"""
Chapter 6

Exercise 1: Pizza Toppings ?(breaking loop)
"""

# This empty list will serve as a container for storing the pizza toppings entered by the customer.
pizza_toppings = []


# The program prompts the user to input either "add" or "quit." Based on this input, a loop is executed repeatedly, maintaining the same condition. 
while True:
    topping = input("\nEnter a pizza topping (or 'quit' to finish): ")
    
    # If the user chooses to either quit or add toppings, the loop will be broken.
    if topping.lower() == 'quit': 
        break  
    
    # iCertainly! When the user decides to add a topping, a confirmation statement will be displayed, ensuring their choice has been acknowledged. The selected topping will then be  stored in the list.
    else:
        pizza_toppings.append(topping)
        print(f"Adding {topping} to your pizza.")

# finally, an output will be shown acknowledging the user's choices and showing the list of toppings they have input.
print("\nYour pizza toppings:")
for topping in pizza_toppings:
    print("- " + topping)
print("\nYour pizza is being prepared, thank you for waiting!")
#