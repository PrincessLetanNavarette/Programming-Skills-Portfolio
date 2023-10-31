"""
Chapter 2

Exercise 3: Stripping Names
"""

singer= "\tEd Sheeran\n"
print("Unmodified:")
print(singer)
#name of the person and print it with the whitespace characters
print("\nUsing lstrip():")
print(singer.lstrip())
print("\nUsing rstrip():")
print(singer.rstrip())
print("\nUsing lstrip():")
print(singer.strip())
#The code first prints the name with the surrounding whitespace.
#Then, it uses the lstrip(), rstrip(), and strip() functions to remove leading, trailing, and both leading and trailing whitespace, respectively, and prints the result for each function.