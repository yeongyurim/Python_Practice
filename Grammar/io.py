f = open("D:/new_file.txt","w")
print(f)
f.close()
f = open("D:/new_file.txt","w")
for i in range(1, 6) :
    data = "%d번째 줄입니다. \n"%i
    f.write(data)
f.close()

f = open("D:/new_file.txt","a")
for i in range(6, 11) :
    data = "%d번째 줄 추가입니다. \n"%i
    f.write(data)
f.close()

f = open("D:/new_file.txt","r")
print(f.readline())
while True:
    line = f.readline()
    if not line: break
    print(line)
f.close()

f = open("D:/new_file.txt","r")
print(f.readlines())
f.close()

f = open("D:/new_file.txt","r")
lines = f.readlines()
for line in lines :
    print(line,end='')
f.close()