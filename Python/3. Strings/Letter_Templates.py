Letter = '''Dear <|NAME|>
You are Selected
            Date: <|Date|>'''
print(Letter)
Name = input("Enter your Name:")
Date = input("Enter Date:")

Letter= Letter.replace("<|NAME|>", Name)
Letter= Letter.replace("<|Date|>", Date)
print(Letter)