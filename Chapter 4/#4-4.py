"""
Chapter 5

Exercise 4: Stages of life
"""
#By putting my age, i will be able to determine which condition block my age category fall 
age = 19

#The age that will be given as an input will fall into one of these conditions. If the number falls into one of these conditions, that will be the output executed.
if age < 2:
    print("You're a baby")
elif age < 4:
    print("You're a toddler")
elif age < 13:
    print("You're a kid")
elif age < 20:
    print("You're a teenager")
elif age < 65:
    print("You're an adult")
else:
    print("You're an elder")