def solution(answers):
    dic = {'score1':0, 'score2':0, 'score3':0}
    for i in range(len(answers)):
        if isCorrect1(i,answers[i]):
            dic['score1'] += 1
        if isCorrect2(i,answers[i]):
            dic['score2'] += 1
        if isCorrect3(i,answers[i]):
            dic['score3'] += 1
    for key in dic.keys():
        print(dic[key])
    answer = []
    return answer

def isCorrect1(i, answer):
    no = i % 5
    li = [1,2,3,4,5]
    return True if li[no] == answer else False

def isCorrect2(i, answer):
    no = i % 8
    li = [2, 1, 2, 3, 2, 4, 2, 5, 2, 1]
    return True if li[no] == answer else False

def isCorrect3(i, answer):
    no = i % 10
    li = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    return True if li[no] == answer else False
    