from numpy import False_


Text = input("Enter Your Text:")
spam=False

if("make a lot of money" in Text):
    spam=True
elif "buy now" in Text :
    spam = True
elif "Click Here" in Text :
    spam = True
else:
    Spam= None
