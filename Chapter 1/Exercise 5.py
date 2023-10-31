"""
Chapter 1

Exercise 5: Compute area of a Circle
"""

from math import pi
#this line imports the value of 'pi' fom the 'math'  module which is equal to 3.14
r = float(input("radius of the circle:"))
#'input' requires the user to give an input and 'float()'converts the input into a float  since the radious can be in a decimal value 
print("The area of the circle with radius" +str(r)+"is:"+str(pi*r**2))
#finally, It then prints the result in a sentence format, indicating the radius provided and the calculated area of the circle.




 