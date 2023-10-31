"""
Chapter 6

Exercise 4: Deli
"""

#in this exercise a list that contains different kinds of sandwiches should be provided
sandwich_orders = ['chicken', 'club', 'ham and cheese', 'pastrami']
finished_sandwiches = [] #this list contains nothin

#this section shows how to let the user know that their sandwich is being prepared while terminating each one
while sandwich_orders: #the while loop will continue to run if there's order coming in from the list of sandwich_orders as one order
    current_sandwich = sandwich_orders.pop() #that sandwich will then be removed from the sandwich_order list
    print("\nYour " + current_sandwich + " sandwich is being prepared.")#shows an output that your sandwich is being prepared until the sandwich_order list runs out
    finished_sandwiches.append(current_sandwich) #this line show that as the outputs show, the sandwich order they bought will be put in the other empty list 

#here will see that the used list was the finished_sandwiches, because it was filled with the values, that were once in the sandiwch_orders list.
print("\n")
for sandwich in finished_sandwiches:
    print("Enjoy your " + sandwich + " sandwich. Thank you ordering!\n")