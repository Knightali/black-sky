class Number():
    def Multiplication(self):
        return self.a*self.b*self.c
num = Number()
num.a=int(input("Enter First Number: "))
num.b=int(input("Enter Second Number: "))
num.c=int(input("Enter Third Number: "))
s= num.Multiplication()
print(s)
