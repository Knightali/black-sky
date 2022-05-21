a=int(input("Enter any number: "))
if(a>300):
    print("Number is greater than 300:")
elif a>=100:
    print("Number is Greater or Equal than 100:")
elif a==300:
    print("Number is less or equal than 300:")
elif a<100 and a>10:
    print("Number is less than 100:")
else:
    print("Not valid Number:")
