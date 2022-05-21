S1 = int(input("Enter Number of subject 1: "))
S2 = int(input("Enter Number of subject 2: "))
S3 = int(input("Enter Number of subject 3: "))
sum = S1 +S2 +S3
perc = (sum*100)/300
if(S1>=33 and S2>=33 and S3>=33 ):
    print("You are Pass")
if(perc<40):
    print("You are fail")
if(perc>=40):
    print("You are Pass")