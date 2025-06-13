st = input("입력: ").split(" ")
st1 = ""
for i in st :
    st2 = i[0] + i[len(i)-1]
    st1 += st2
print(st1)