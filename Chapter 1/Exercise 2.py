"""
Chapter 1

Exercise 2: Print the Version of the Python
"""
#the purpose of this code is to provide the user their Python version, in case of needing debugging or checking compatibility with specific features.
import sys
#import sys provides access to few variables used or  maintained by the Python interpreter 
print("Python Version")
#it serves as a label to indicate that the following output will display the Python version information.
print(sys.version)
#this contains the version of the current Python interpreter
print("Version info")
#displays the detailed version information
print(sys.version_info)
#through this, the information about the version of the Python would be printed as a tuple