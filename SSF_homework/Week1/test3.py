print("예제 입력 : ")
first = input()
second = input()
third = input()
msg = False
if first > second and first > third:
    msg = True
elif first == second == third:
    msg = True
else:
    msg = False
    
print("예제 출력 : ")
print(msg)