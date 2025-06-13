st1 = input("문자열을 입력하세요 :").split(",")
st2 = []
for i in st1:
    st = i.strip()
    if(st[::-1]==st) :
        st2.append(st)
print("회문인 단어:"," ".join(st2))