# 고성능 과학연산(다차원 벡터 연산)을 위한 파이썬 라이브러리
import numpy as np
print(np.__version__)
ar1 = np.array([1,2,3,4,5])
print(ar1)
print(type(ar1))
ar2 = np.array([[10, 20, 30], [40, 50, 60]])
print(ar2)
ar3 = np.arange(1,11,2)
print(ar3)
ar4 = np.array([1,2,3,4,5,6]).reshape((3,2))
print(ar4) # 순서대로 3행 2열로 자름
ar5 = np.zeros((2, 3))
print(ar5) # 2행 3열치 0 행렬
ar6 = ar2[0:2, 0:2]
print(ar6)
ar7 = ar2[0,:]
print(ar7)
ar8 = ar1 + 10
print(ar8)
print(ar1 + ar8)
print(ar8 - ar1)
print(ar1 * 2)
print(ar1 / 2)
ar9 = np.dot(ar2,ar4) #행렬 곱셈
print(ar9)