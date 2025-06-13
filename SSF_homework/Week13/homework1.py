def check_pass(name, *args):
    sum = 0
    avg = 0
    for i in args :
        sum += i
    avg = sum / len(args)
    if avg >= 60 :
        script = "{0}님은 평균 {1:.2f}점으로 합격입니다.".format(name,avg)
        print(script)
    elif avg < 60 :
        script = "{0}님은 평균 {1:.2f}점으로 불합격입니다.".format(name,avg)
        print(script)

check_pass("보윤", 70, 80, 65)
check_pass("태규", 50, 40, 55)
