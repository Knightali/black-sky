# ADDITION OF  TWO NUMBER
# Simple Method
# a=12
# b=34
# print("The Sum of a and b is: ",a+b)

# By Using Class 

class Number():
    def sum(self):
        return self.a +self.b  

num = Number()
num.a = 12
num.b = 34
s = num.sum()
print(s)

