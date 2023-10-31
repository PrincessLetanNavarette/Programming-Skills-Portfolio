"""
Chapter 4
Exercise 3: Alien Colors (if-elifelse chain)

"""
 # if-eliselse is use to execute certain block which provides the output that makes the condition true

# The player's input  
alien_color = 'green'

#This block will be executed if the player's input is true with the if condition
if alien_color == 'red':
    print("You just earned 5 points!")
    
#This block will be executed if the player's input is true with the other condition
elif alien_color == 'yellow':
    print("You just earned 10 points!")

#This block will be executed if the player's input didn't meet the conditions given before this block
else:
    print("You just earned 15 points!")
    
