"""
Chapter 3

Exercise 7: Seeing the world
"""
must_see=['Maldives','Greece','Barcelona','Japan','Switzerland']

###Print list in its original order
print("\nOriginal order:", must_see)

###Use sorted() to print list in alphabetical order
print("\nAlphabetical order:", sorted(must_see))

###Print list in its original order
print("\nOriginal order:", must_see)

###Use sorted() to print list in reverse alphabetical orde
print("\nReverse Alphabetical order:", sorted(must_see, reverse=True))

###Print list in its original order
print("\nOriginal order:", must_see)

###Use reverse() to change the order of the list
must_see.reverse()
print("\nReversed order:", must_see)

###Use reverse() to change the order of the list again. Print the list to show it’s back to its original order
must_see.reverse()
print("\nOriginal order:",must_see)

###Use sort() to change the list so it’s stored in alphabetical order.
must_see.sort()
print("\nAlphabetical order:", must_see)

###Use sort() to change the list so it’s stored in reverse alphabetical order
must_see.sort(reverse=True)
print("\nReverse Alphabetical order:", must_see)
