"""
Chapter 3

Exercise 5: Change Guest List
"""
saved_seats=['June', 'Kylie', 'Sam', 'Larry']

print("Dear", saved_seats[0], ", I hope this is a good time to invite you to my dinner party, at Yours Restobar. See you there!")
print("Dear", saved_seats[1], ", I hope this is a good time to invite you to my dinner party, at Yours Restobar. See you there!")
print("Dear", saved_seats[2], ", I hope this is a good time to invite you to my dinner party, at Yours Restobar. See you there!")
print("Dear", saved_seats[3], ", I hope this is a good time to invite you to my dinner party, at Yours Restobar. See you there!")

###June is out of town
print("\nUnfortunately,", saved_seats[0], "can't make it. He was out of town\n")
del(saved_seats[0])
saved_seats.insert(0, 'Grace')

###Maybe Grace can fill June's seat
print("Dear", saved_seats[0], ", I hope this is a good time to invite you to my dinner party, at Yours Restobar. See you there!")
print("Dear", saved_seats[1], ", I hope this is a good time to invite you to my dinner party, at Yours Restobar. See you there!")
print("Dear", saved_seats[2], ", I hope this is a good time to invite you to my dinner party, at Yours Restobar. See you there!")
print("Dear", saved_seats[3], ", I hope this is a good time to invite you to my dinner party, at Yours Restobar. See you there!")