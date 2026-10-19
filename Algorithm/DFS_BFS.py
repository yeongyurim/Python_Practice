def solution(numbers, target):
    answer = 0
    answer = recursion(numbers, -1, 0, target)
    return answer

def recursion(numbers, idx, num, target):
    if idx == (len(numbers)-1) :
        if num == target :
            return 1
        else :
            return 0
    else :
        return recursion(numbers, idx+1, num + numbers[idx], target) + recursion(numbers, idx+1, num - numbers[idx], target)
    
print(solution([1,1,1,1,1],3))