gender, age = input("입력:").split(' ')
age = int(age)
print("출력:")
if(gender == "M") :
    if(age < 18) :
        print("BOY")
    else :
        print("MAN")
else :
    if(age < 18) :
        print("GIRL")
    else :
        print("WOMAN")