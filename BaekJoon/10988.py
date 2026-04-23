word = input()
wordStack = []
mid = len(word)//2
pal = True
for i in range(mid) :
    wordStack.append(word[i])
if len(word) % 2 == 1 :
    mid += 1    
for i in range(mid, len(word)) :
    if(word[i] != wordStack.pop()) :
        pal = False
        break
print("1" if pal else "0")