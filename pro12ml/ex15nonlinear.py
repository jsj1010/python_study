# 비선형회귀분석(Non-linear Regression)
# 직선의 회귀선을 곡선으로 변환해 더 정확하게 데이터 변화를 예측가능
# 선형 가정이 어긋날 때(비 정규성) 대처할 수 있는 방법 으로 
# 다항식 항을 추가해 다항회귀모델을 작성

import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

x = np.array([1,2,3,4,5])
y = np.array([4,2,1,3,7])

print(np.corrcoef(x,y)[0, 1]) # 0.480761

plt.scatter(x,y)
plt.show()

# 선형회귀 모델을 적용
from sklearn.linear_model import LinearRegression
x = x[:, np.newaxis] # 차원 확대. 1차원을 -> 2차원으로 바꿈
print(x) # [[1] ... ]

model = LinearRegression().fit(x,y)
ypred = model.predict(x)
print('예측값 y : ', ypred) # [2.  2.7 3.4 4.1 4.8]
print('결정계수 : ',r2_score(y, ypred)) #  0.23113207547169834

plt.scatter(x , y)
plt.plot(x, ypred, c='red')
plt.show()

print("---------------------------------------------------")
# 비선형 모델 작성
# 여러 방법 중 가장 일반적인 방법을 사용(PolynomialFeatures, log변환, curve_fit...)
from sklearn.preprocessing import PolynomialFeatures # 다형식 특정(변수)을 추가 가능
poly = PolynomialFeatures(degree=3, include_bias=False) # degree = 열의 갯수 / 항이 올라갈수록 오버피팅
x2 = poly.fit_transform(x)
print(x)  # 5 by 1
print(x2) # 5 by 2

model2 = LinearRegression().fit(x2, y) # 추가된 특징 행렬값으로 모델 생성
ypred2 = model2.predict(x2)
print('예측값 y : ', ypred2) # [4.14285714 1.62857143 1.25714286 3.02857143 6.94285714]
print('결정계수 : ',r2_score(y, ypred2)) #  0.9892183288409704

plt.scatter(x,y)
plt.plot(x, ypred2, c='red')
plt.show()