"""
Chapter 5

Exercise 4: Rivers (loop)
"""
#The 'rivers' dictionary is structured with keys representing each river and their corresponding values indicating the main locations where these rivers flow. 
rivers = {
    'volga': 'russia',
    'amazon': 'brazil',
    'congo': 'democratic Republic of the Congo',
    'murray-Darling': 'australia',
    'yangtze': 'china'}

#this exercise requires us to us the loop as we print a statement and values about each keys or rivers, therefore the 'for' is needed to print every keys in the 'rivers' without having any trouble
#prints the information about the keys 
for river, country in rivers.items():
    print("The " + river.title() + " streaming through " + country.title() + ".")

#prints the keys from the 'rives'
print("\nThese are the rivers given in the data set:")
for river in rivers.keys():
    print("- " + river.title())

#prints the location of the rivers from the keys or 'rivers' 
print("\nThese are the following countries of the rivers in the data set:")
for country in rivers.values():
    print("- " + country.title())