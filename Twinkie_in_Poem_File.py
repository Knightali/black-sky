F = open("Poem.txt","r")
Poem = F.read()
if "Twinkle" in Poem:
    print("Twinkle is Persent")
else:
    print("Twinkle is Not Persent")
F.close()