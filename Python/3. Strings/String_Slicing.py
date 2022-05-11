from typing import Optional


Greeting = "Good Night, "
# Name = input("Enter your NAME: ")
# print(type(Name))
# print(type(Greeting))
        # Concatinate Two Strings 
# c= Greeting + Name
# print(c)
# print(Greeting + Name)
    # Slicing 
# print(Name[2])      # In computer Language Counting start from 0 Like ==> ahmad has 5 alphabats we count but in programming it has 0 to 4 alphabets 
# a is at 0th palce and h is at 1th place and so on and at 4th place there is d

        # >>> Main Point <<<

'''     The index in a string starts fron 0(lenght-1) in python. In order to slice a sentense we use the following Stntax:

        Variable Name[Index_Start : Index_End]
    NOTE: => Index_Start is Optional but Index_End is not Optional '''

# Name[3] = "d"  ==> Does Not work 

        # String Slicing 
# print(Name[0:3])  #  : => se le kar  means 0 to 3  
# print(Name[1:4])  #  : => se le kar  means 1 to 4  

        # ALSO 
Name="Aslamahmad"
# Print(Name[:4]) = print(Name[0:4])
# Print(Name[1:]) = print(Name[1:4])


        # Negative index can also be used. -1 crossponds to (lenght-1) index, -2 crossponds to (lenght-2);
print(Name[-1])
# Print(Name[-4:-1]) = print(Name[1:4])


            # SLICING WITH A SKIP VALUE 

'''    Variable Name[Index_Start : Index_End:Skip_Value]
    NOTE: => Index_Start is Optional but Index_End is not Optional  
    and Skip_Value is must need to write '''
print(Name[0:9:2])      # Skipping Vlaue is 2 means print alphabet by skiping 1 next alphabet
print(Name[0::3])      # Skipping Vlaue is 3 means print alphabet by skiping 2 next alphabet
