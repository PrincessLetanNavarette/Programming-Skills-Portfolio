"""
Chapter 5
 
Exercise 5: Pets
"""
# this exercise requires us to make use the loop to print every dictionary including its keys and values in a same format with which keys.

#These are four dictioaries that have diffecnt keys and values
pet1 = {'animal_type': 'dog', 'pet_name': 'Buddy', 'owner_name': 'Alice'}
pet2 = {'animal_type': 'cat', 'pet_name': 'Whiskers', 'owner_name': 'Bob'}
pet3 = {'animal_type': 'parrot', 'pet_name': 'Polly', 'owner_name': 'Charlie'}
pet4 = {'animal_type': 'rabbit', 'pet_name': 'Fluffy', 'owner_name': 'David'}

# this is where the 4 dictionaries was stored as a list, through this list using for loop would be possible and effective
pets = [pet1, pet2, pet3, pet4]

# Using the variable assigned to the list simplifies the process by accessing the dictionary, allowing simultaneous looping through each dictionary in the list.
for pet in pets:
    animal_type = pet['animal_type']
    pet_name = pet['pet_name']
    owner_name = pet['owner_name']
    print(f"\nThe pet is a {animal_type} named {pet_name} and the owner's name is {owner_name}.")