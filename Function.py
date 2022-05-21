        # A Simply Way To Write  

from asyncio import tasks


Marks = [34, 56, 78, 56, 44, 32, 99, 44]
# Percent = (sum(Marks)/800)*100
        # WE can Also Write Like that 
Percent = ((Marks[0] + Marks[1] + Marks[2] + Marks[3] + Marks[4] + Marks[5] + Marks[6] + Marks[7])/800)*100

Marks1 = [45, 56, 65, 57, 78, 99, 89, 99,]
Percent1 = (sum(Marks1)/800)*100
print(Percent, Percent1)

                # By Using Function Method 
def percent(marks):
    return  ((Marks[0] + Marks[1] + Marks[2] + Marks[3] + Marks[4] + Marks[5] + Marks[6] + Marks[7])/800)*100
Marks1 = [34, 56, 78, 56, 44, 32, 99, 44]
Percent = percent(Marks1)
Marks2 = [45, 56, 65, 57, 78, 99, 89, 99,]
Percent = percent(Marks2)
print(Percent, Percent1)

            # FUNCTION ==> A group of Statements performing a specific tasks
            # def =>  Defines a function 
            # Where To Use Function => When a Program gets Bigger in size and its complexities grows up,  it get  difficult for programmer to keep trac kthat the which code is doing what 
            # A Function can be Reused  by the programmer in the program

            # FUNCTION CALL ==>  func()  whenever we call a function we put the name of function in parenthesis
            # FUNCTION DEFFINATION ==> The part Containing the exact set of Instruction that are executed during  Function Call
            

