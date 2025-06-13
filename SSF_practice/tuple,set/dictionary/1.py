scores = {
    '철수' : 85,
    '영희' : 92,
    '민수' : 78
}
print(scores['영희']) # 92 출력

word = 'hello'
count = {}
for ch in word :
    count[ch] = count.get(ch, 0) + 1
print(count)