from ctypes.wintypes import WORD


word = True
i =1
with open("log.txt","r") as f:
    while word:
        word = f.readline()

        if 'python' in word.lower():
            print(word)
            print(f"Python is Present in line {i}: ")
        i=i+1