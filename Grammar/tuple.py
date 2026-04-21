t1 = (1,)
t2 = (1,2,3)
t3 = 1, 2, 3
t4 = (1, 2, (3, 4), ('Life','is'))
print(t4[0])
print(t4[3][::-1])
print(t4[0:3])
print(t1+t2)
#print(t1 + "hi~^^;") 같은 데이터 형만 더할 수 있음 tuple + tuple만 됌 상단처럼
print(t2 * 3)
#print(t2[2]=99) tuple은 초기화 이후 값을 바꿀 수 없다.