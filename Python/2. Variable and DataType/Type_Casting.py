        # Type Casting (Method to convert Datatype )

a= "4532"
print(type(a))
# print(a+45) ===>  # Produce error because we cannot add integer in a string 
        #  We need to use a Type casting method to it
a=int(a)    # It will try to convert a string to int if possible
    # Suppose 
b="ahmad234"    # It is a string 
# b= int(b) ===>    # It is Not valid because we cannot use any Char in Integer so it cannot be convert to int datatype
print(type(a))
print(a+45)

        # We can convert int datatype to string but we cannot convert string datatype int if it is invalid as discussed upper
        # We can convert int datatype to float and  we can convert float datatype int 
a=56.564
print(type(a))
print(a)
a=int(a)
print(type(a))
print(a)
        
