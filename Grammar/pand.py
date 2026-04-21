# 데이터 분석(=엑셀, DB)과 처리를 위한 파이썬 라이브러리
import pandas as pd
print(pd.__version__)
data1 = [10,20,30,40,50]
print(data1)
data2=['1반','2반','3반','4반','5반']
print(data2)
sr1 = pd.Series(data1)
print(sr1)
sr2 = pd.Series(data2)
print(sr2)
sr5 = pd.Series(data1, index=[1000,1001,1002,1003,1004])
print(sr5)
sr6 = pd.Series(data1, index = data2)
print(sr6)
sr7 = pd.Series(data2, index = data1)
print(sr7)
print(sr6['1반'])
print(sr7.iloc[-1])
print(sr7[0:4])
print(sr6.values)
print(sr1+sr1)