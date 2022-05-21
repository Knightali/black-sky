age= int(input("Enter your age:"))

        # AND OPERATOR 
if(age>=20 and age<=40):
    print("You are selected:")
else:
    print("Your are not selected:")
        # OR OPERATOR 
if(age>=20 or age<=40):
    print("You are selected:")
else:
    print("Your are not selected:")
        # NOT OPERATOR 
if not(age>=20 or age<=40) :
    print("You are selected:")
else:
    print("Your are not selected:")