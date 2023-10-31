"""
elif

"""
##0=No
1#-5= 5
#6-10= 10
#11-15= 15
#above=membership canel

day=int(input("Enter your days"))
if day== 0:#ifthe conditions are not mesnt at the first "if" then the program will run the elif for other condition or option
    print("No fine")
elif day>=1 and day<=5:
    print("fine amount=",day*5, 3
          "dhs")
elif day>=6 and day<=10:
    print("fine amount=",day*10)
elif day>=11 and day<=15:
    print("fine amount=",day*15)
else:
    print("membership cancel")