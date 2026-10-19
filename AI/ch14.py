import pandas as pd
import numpy as np
import FinanceDataReader as fdr

# 설정할 변수들
ticker = "GOOG"  # 구글 종목 코드
start_date = "2022-05-01" #4년치만 해보자
end_date = "2026-05-01"

try:
    # 1. 주가 데이터 다운로드하여 바로 stock 변수에 저장
    stock = fdr.DataReader(ticker, start=start_date, end=end_date)

    # 2. 날짜 오름차순 정렬 및 결측치 제거
    stock = stock.sort_index()
    stock = stock.dropna()

    print("Download success!")
    print(stock.head())  # 데이터 앞부분 5줄 출력

except Exception as e:
    print("Download failed")
    print(e)
    stock = None
    
stock2 = pd.DataFrame(stock['Close'])
print(stock2.head())
stock2.to_csv('ticker.csv')


stock2.reset_index()
stock_values = stock2.values
print(stock_values[0])        # 작업 확인용 출력

# ----- In [8]: MinMaxScaler 임포트 -----
from sklearn.preprocessing import MinMaxScaler

# ----- In [9]: 스케일링 정규화 수행 -----
scaler = MinMaxScaler(feature_range=(0, 1))
stock_values_scaled = scaler.fit_transform(stock_values)

stock_values_scaled[0]        # 작업 확인용 출력


# ----- In [10]: 학습/평가 데이터 분할 -----
n_train = int(len(stock_values) * 0.8)   # 학습용 데이터 개수
n_test  = len(stock_values) - n_train    # 평가용 데이터 개수

print(n_train, n_test)        # 작업 확인용 출력

# ----- In [11]: 학습 데이터 X_train / Y_train 구성 -----
X_train, Y_train = [], []

# 20일 구간의 주가를 x값으로 하고, 그다음 날 값을 y값으로 정리
for i in range(20, n_train):
    X_train.append(stock_values_scaled[i-20:i, 0])
    Y_train.append(stock_values_scaled[i, 0])

X_train[0]                    # 작업 확인용 출력

# ----- In [12]: LSTM 입력 형태로 reshape -----
X_train1, Y_train1 = np.array(X_train), np.array(Y_train)
X_train2 = np.reshape(X_train1, (X_train1.shape[0], X_train1.shape[1], 1))

print(X_train2.shape)         # 작업 확인용 출력
X_train2[0]                   # 작업 확인용 출력


# ----- In [13]: LSTM 모델 관련 모듈 임포트 -----
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense, LSTM, Dropout

# ----- In [14]: LSTM 모델 구축 -----
lstm_stock = Sequential()

lstm_stock.add(LSTM(units=20, return_sequences=True,
                    input_shape=(X_train2.shape[1], 1)))
lstm_stock.add(LSTM(units=20, return_sequences=False))
lstm_stock.add(Dense(1))

# ----- In [15]: 학습 수행 -----
# 학습 매개변수 설정
lstm_stock.compile(loss='mean_squared_error', optimizer='adam')

# 학습 수행
lstm_stock.fit(X_train2, Y_train1, epochs=10, batch_size=1, verbose=2)

# ----- In [16]: 평가 데이터 X_test 구성 -----
stock_test = stock_values_scaled[n_train-20:]
X_test = []
for i in range(20, len(stock_test)):
    X_test.append(stock_test[i-20:i, 0])
X_test[0]                     # 작업 확인용 출력


# ----- In [17]: X_test reshape -----
X_test = np.array(X_test)
X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))

print(X_test.shape)           # 작업 확인용 출력
print(X_test[0])              # 작업 확인용 출력

# ----- In [18]: 예측 수행 -----
predicted_value = lstm_stock.predict(X_test)

predicted_value[0]            # 작업 확인용 출력

# ----- In [19]: 역정규화 -----
predicted_value = scaler.inverse_transform(predicted_value)

predicted_value[0]            # 작업 확인용 출력

# ----- In [20]: 시각화용 데이터 정리 -----
stock_train_vis = stock[:n_train]
stock_test_vis  = stock[n_train:]
stock_test_vis['Predictions'] = predicted_value


# ----- In [21]: matplotlib 임포트 -----
import matplotlib.pyplot as plt

# ----- In [22]: 그래프 그리기 -----
plt.figure(figsize=(12, 8))
plt.plot(stock_train_vis['Close'],          label='Train')
plt.plot(stock_test_vis['Close'],           label='Test')
plt.plot(stock_test_vis['Predictions'],     label='Prediction')
plt.legend()
plt.title(ticker + ' (' + start_date + ' ~ ' + end_date + ' )')
plt.show()
