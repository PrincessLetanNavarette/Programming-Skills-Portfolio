f"""
Chapter 3

Exercise 6: Shrinking Guest List
"""
saved_seats=['June', 'Kylie', 'Sam', 'Larry']
print("Dear", saved_seats[0], ", I hope this is a good time to invite you to my dinner party, at Yours Restobar. See you there!")
print("Dear", saved_seats[1], ", I hope this is a good time to invite you to my dinner party, at Yours Restobar. See you there!")
print("Dear", saved_seats[2], ", I hope this is a good time to invite you to my dinner party, at Yours Restobar. See you there!")
print("Dear", saved_seats[3], ", I hope this is a good time to invite you to my dinner party, at Yours Restobar. See you there!")

###June was out of town
saved_seats=[0]
saved_seats.insert(0, 'Grace')
print("\nUnfortunately,", saved_seats, "couldn't make it. He was out of town\n")

###Maybe Grace can fill June's seat
print("Dear", saved_seats[0], ", I hope this is a good time to invite you to my dinner party, at Yours Restobar. See you there!")
print("Dear", saved_seats[1], ", I hope this is a good time to invite you to my dinner party, at Yours Restobar. See you there!")
print("Dear", saved_seats[3], ", I hope this is a good time to invite you to my dinner party, at Yours Restobar. See you there!")
print("Dear", saved_seats[4], ", I hope this is a good time to invite you to my dinner party, at Yours Restobar. See you there!")


###You just found out that your new dinner table won’t arrive in time for the dinner, and you have space for only two guests.
print("\nOh dear! The Restobar just informed me that I can only bring 2 people. I apologize for the inconvience.")

###Apologize for cancelling dinner
saved_seats.pop(2)
print("\nHi,", saved_seats, "apologies but I am cancelling our dinner, there was an issue with the reservation but, I hope to see you next time! ")
saved_seats.pop(3)
print("Hi,", saved_seats, "apologies but I am cancelling our dinner, there was an issue with the reservation but, I hope to see you next time! ")

###Invite two people
print("\nDear", saved_seats[2], ", I just want to inform you that you are still invited to come to the dinner party. I hope to see you . Take care!")
print("Dear", saved_seats[3], ", I just want to inform you that you are still invited to come to the dinner party. I hope to see you . Take care!")

###Remove last two invites
del saved_seats
print(saved_seats)