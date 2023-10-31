bio={'Id': '8','Name':'Princess','Age':'19','City':'Sharjah'}
print(bio['Id'])
print(bio['Name'])
print(bio['Age'])
print(bio['City'])
bio['Course']='CC'### adding a new value to the dictionary
print(bio)
print('\nBio details before altering the value:\n', bio)
bio['Course']='BM'### changing into a new value
print('\nBio Details after altering the value:\n', bio)
print('Bio details before deleting the value\n', bio)
del bio['Course']### delete a value
print('\nBio details after deleting the value\n',bio)