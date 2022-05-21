                # >>> MY CALCULATOR TO PERFORM SIMPLE OPERATION <<<

print("STARTING CALCULATOR: ")
operator = input("Enter Operator for Addition(+), Subtraction(-), Multiplication(*) and if you want to Quit press any other key: ")
Simple = 0
simple=1
if operator == '+' or operator == '-' or operator == '*':
    while(True):
        Value = input("Enter Number to Calculate and Enter 'q' to Quit:  ")
        if Value!='q':
            if operator=='+':
                Simple = Simple +int(Value)
            elif operator == '-':
                Simple = -Simple+int(Value)
            elif operator =='*':
                simple = simple*int(Value)
        else:
            print(f"Your Multiplication Total is {simple}: ")
            print(f"Your Sum or Subtraction total is {Simple}:")
            break 
else: 
    print("OPERATOR NOT FOUND, YOU ENTER WRONG OPERATOR:")
print(" ")
More_Operator =  input("More Operator: for Square(sq), for Division(/),  for cube(cu) and for Power(pow):  ")
More = 0
if More_Operator == 'sq' or More_Operator == 'cu' or More_Operator == 'pow':
    while(True):
        Value1 = input("Enter the Number to calculate and Enter 'q' to Qiut:  ")
        if Value1 != 'q':
            if More_Operator=='sq':
                # More = More + int(Value1*Value1)
                print(f"The Square of {Value1} is: ", int(Value1)*int(Value1))

            elif More_Operator  =='cu':
                # More = More + int(Value1*Value1*Value1)
                print(f"The Cube of {Value1} is: ", int(Value1)*int(Value1)*int(Value1))
            elif More_Operator =='pow':
                Power = int(input("Enter the Power of value: "))
                print(f"The {Power} Power of {Value1} is:  ", pow(int(Value1), Power))
        else:
            print("OPERATOR NOT FOUND, YOU ENTER WRONG OPERATOR:")
print(" ")
print ("FOR DIVISION: ")

Divide = (input("Enter 'div' for Division and 'q' for Quit:"))
while(True):
    if Divide=='div':   
        Divide0 = float(input("Enter first Value:"))
        Divide1 = float(input("Enter second Value:"))
    print(f"The Division of {Divide0} and {Divide1} is: ", Divide0/Divide1)
    
    break
print("THANKS FOR USING OUR CALCULATOR. HAVE A GOOD DAY.")
print("PLEASE COME AGAIN:")
        
   
    
    


            

                

