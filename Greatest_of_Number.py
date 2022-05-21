def Greatest(num1, num2, num3):
    if num1>num2 and num1>num3:
        return num1
    if num2>num1 and num2>num3:
        return num2
    if num3>num2 and num3>num1:
        return num3

Num1 = int(input("Enter First Number: "))
Num2 = int(input("Enter Second Number: "))
Num3 = int(input("Enter Third Number: "))
Maximun = Greatest(Num1, Num2, Num3)
print(Maximun,"is Maximun of all Number:")
    