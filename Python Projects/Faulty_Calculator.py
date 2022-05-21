            # FAULTY CAlCULATOR
        # Design a Calculator which will correctly solve all the problems except the following ones with operators:   45+34 = 66 , 5*65=444,  78/10=6
        # A program take Operator and the Two Number as Input fronm user and return their result 

import random
while(True):
    Operator = input("Enter operator + * / -  to use one of them and Enter 'q' to Quit:  ")
    if Operator =='+':
        Num0=float(input("Enter First Number: "))
        Num1=float(input("Enter Second Number: "))
        sum = Num0 + Num1
        sum = random.randint(1, 1000)
        print(f"The sum of two number {Num0} and {Num1} is:  ", sum)
    elif Operator =='*':
        Num0=float(input("Enter First Number: "))
        Num1=float(input("Enter Second Number: "))
        Mul = Num0 * Num1
        Mul = random.randint(1, 1000)
        print(f"The Multiplication of two number {Num0} and {Num1} is:  ", Mul)
    elif Operator =='/':
        Num0=float(input("Enter First Number: "))
        Num1=float(input("Enter Second Number: "))
        Div = Num0 / Num1
        print(f"The Division of two number {Num0} and {Num1} is:  ", Div)
        Div = random.randint(1, 1000)
    elif Operator =='-':        # The answer will Correct in it  
        Num0=float(input("Enter First Number: "))
        Num1=float(input("Enter Second Number: "))
        Sub = Num0 - Num1
        print(f"The Subtraction of two number {Num0} and {Num1} is:  ", Sub)
    elif Operator=='q':
        print("WRONG OPERATOR:")
        break
print("THANKS FOR USING:")
