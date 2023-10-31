"""
Chapter 6

Exercise 5: No Pastrami
"""

#in this exercise 'pastrami' should be put int list but will not be show to the output
sandwich_orders = ['chicken', 'pastrami', 'club', 'pastrami', 'ham and cheese', 'pastrami']
finished_sandwiches = []

#informing the user that Pastrami is not available
print("Welcome to our Deli!\n\tUnfortunately, today our famous pastrami sandwiches are taking a break. Apologies for the inconvenience.\n")

#removing the occurances of 'pastrami' in the list
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

#preparing the sandwiches that were left in the list sandwich_orders and removing it and putting it to the empty list( finished_sandwiches)
print("\nNow cooking your:")
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("- " + current_sandwich.capitalize()+ " sandwich")
    finished_sandwiches.append(current_sandwich)

#informs the user that their sandwich is ready from the finished_sandwiches list with no 'pastrami' occurance.
print("\nSandwich made ready for you:")
for sandwich in finished_sandwiches:
   print("- " + sandwich.capitalize() + " sandwich")

print("\nEnjoy your meal!")