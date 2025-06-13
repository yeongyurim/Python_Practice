students = {
    "웅조" : "남자",
    "영희" : "여자",
    "학찬" : "남자",
    "지혜" : "여자",
    "현진" : "남자"
}

print("학생 명단")

boy = girl = 0
for name in students :
    gender = students[name]
    print(name,"-",gender)
    if (gender == "남자") :
        boy += 1
    else :
        girl += 1
        
print("전체 학생 수:"+str(len(students)))
print("남학생 수:"+str(boy))
print("여학생 수:"+str(girl))