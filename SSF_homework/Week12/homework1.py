info = {
    "이름":"양웅조",
    "직업":"군인",
    "국적":"대한민국",
    "나이":"22세",
    "출신":"전주"
}
query = ""
while(query != "그만") :
    query = input("조회할 항목을 입력하세요 (그만 입력 시 종료):")
    if(info.get(query)) :
        print(query+":",info[query])
    else :
        print("해당 정보 없음")