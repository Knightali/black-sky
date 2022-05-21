            # *
           # ***
         #  *****
n = 3 
for i in range(3):
    print(" " * (n-i-1), end="")        # end="" is used to stop compiler to print new line
    print("*" * (2*i+1), end="")
    print(" " * (n-i-1))
