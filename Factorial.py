from math import factorial


Ending_Num = int(input("Enter the Ending Number:"))
Factorial = 1
for a in range(1, Ending_Num+1):
    Factorial = Factorial * a
print(f"Factorial of {a} is:{Factorial}")