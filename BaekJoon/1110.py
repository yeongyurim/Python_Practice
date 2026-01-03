target = int(input())
tartget = target if target > 9 else target * 10
num = target
cycle = 0
while(True):
    sum = num // 10 + num % 10
    num = num % 10 * 10 + sum % 10
    cycle += 1
    if(target == num):
        break
print(cycle)
