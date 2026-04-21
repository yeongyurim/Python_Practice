dic = {"name":"hong","phone":"010-7556-9552"}
dic[1]='a'
print(dic)
dic['pet'] = 'dog'
print(dic)
del dic[1]
print(dic)
print(dic.keys()) # 키들만 나옴
print(list(dic.keys())) # 키들만 리스트로 뺌 
print(dic.values()) # 값들만 나옴
print(list(dic.values())) # 값들만 리스트로 뺌
print(dic.items())
dic.clear()
print(dic)