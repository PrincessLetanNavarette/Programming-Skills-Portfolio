"""
nested if
"""
###Marks(variable), total(+),avg(total/3)
###if(variable_marks1>=, and variable_marks2>=and, variable_marks1>= )
###print("pass") 

_1score=int(input("first score"))
_2score=int(input("second score"))
_3score=int(input("third score"))
total= _1score+_2score+_3score
avg=(total/3)
print("total=",total)
if _1score>=70 and _2score>=70 and _3score>= 70:
    print("Pass")
if avg>= 90 and avg<=100:
    print("Grade A")
elif avg>=80 and avg<=89:
    print("Grade B")
elif avg>=70 and avg<=79:
    print("Grade C")
else:
    print("result:Fail")
    