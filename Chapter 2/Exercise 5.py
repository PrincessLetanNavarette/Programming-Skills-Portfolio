"""
Chapter 2

Exercise 5:USB Shopper
Arithmetic Operator

Write a programme that calculates 
how many USB sticks she can buy and 
how many pounds she will have left.
"""

###Number of USB sticks she can buy.
money=int("50")
stick=int("6")
print('If USB Sticks cost',int(stick),'pounds, how many can be bought with',int(money),'pounds?')

###program/computation
b_girl=int("50") #("girl's budget for USB Stick")
u_cost=int("6")  #("cost of one USB Stick")
pieces=(b_girl//u_cost)
print(pieces,"pieces")

###Her change from buying 8 pieces of USB Sticks.
total=int("48")
budget=int("50")
print('\n',int(pieces),'pieces of USB Sticks cost',int(total),'pounds, how much pounds was left from',int(budget),'pounds?')

###program/computation
b_girl=int("50")
_left=int("48")  
u_cost=int("6") 
change=(b_girl%_left)
print(change,'pounds')

###Answer
conclusion=f"\nTherefore, If the girl decided to buy USB Sticks with her {b_girl} pounds she could have {pieces} pieces of it and still have {change} pounds of change left."
print(conclusion)



