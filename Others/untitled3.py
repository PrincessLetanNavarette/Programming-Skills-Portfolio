"""
Chapter 5
 
Exercise 5: Pets
"""

pets_0={'Cat':'Charlie','Dog':'Jack','Fish':'Best'}
pets_1={'Cat':'Manny','Dog':'Alex','Fish':'Betta'}
pets_2={'Cat':'Duti','Dog':'Sam','Fish':'Tim'}
pets_3={'Cat':'Will','Dog':'Ken','Fish':'Larry'}
all_pets=[pets_0,pets_1,pets_2,pets_3]
for std in all_pets:
    print(std)

#Store infor about the pets
pets={
    'Cat':'Charlie',
    'Children':['2 female kittens'],
}

##Summarize the details
print(f"The Cat's name is {pets_0['Cat']}, and he has")
for Children in pets['Children']:
  print(Children)

pets_0={
'Dog':'Jack',
'Children':['5 puppies'],
}
birth={
       'Birth':2020
}
#update dictionary
#
print(pets_0)
