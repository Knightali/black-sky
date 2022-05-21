def game():
    return 267
score = game()
f= open("High_Score.txt", "r")
HighScore = int(f.read())
if score>HighScore:
    f = open("High_Score.txt" ,"w")
    f.write(str(score))

