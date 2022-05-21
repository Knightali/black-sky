
Num = int(input("Enter any Number: "))
Prime = True
for a in range(2, Num):
    if(Num%a==0):
        Prime = False
        break
if Prime== True:
    print( Num,"is prime number:")
else:
    print( Num,"is not prime number:")
