# 보스턴 주택 가격
# : 1978년에 발표된 데이터로 미국 보스턴 지역의 주택 가격에 영향을 미치는 요소들을 정리함

# CRIM	자치시(town)별 1인당 범죄율
# ZN	25,000 평방피트를 초과하는 거주 지역의 비율
# INDUS	비소매상업 지역이 차지하는 면적 비율
# CHAS	찰스강 찰스강 인접 여부 (강 경계에 위치하면 1, 아니면 0)
# NOX	일산화질소 농도 (1000만 분의 1 단위)
# RM	주택 1가구당 평균 방의 개수
# AGE	1940년 이전에 건축된 소유 주택의 비율
# DIS	보스턴 5대 고용 중심지까지의 가중 거리
# RAD	방사형 고속도로 접근성 지수
# TAX	$10,000당 재산세율
# PTRATIO	자치시별 학생-교사 비율
# B	1000(Bk - 0.63)² (Bk는 도시별 흑인 비율) ※ 윤리적 문제 지적 변수
# LSTAT	하위 계층 인구의 비율 (%)
# MEDV	[Target] 본인 소유 주택 가격의 중앙값 (단위: $1,000)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import koreanize_matplotlib

pd.set_option('display.max_columns', None)

df = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/housing.data", header=None, sep=r'\s+')
df.columns = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV']
print(df.head(2))
print(df.corr())  # LSTAT(저소득층 인구), MEDV(주택가격) : -0.737663

x = df[['LSTAT']].values
y = df['MEDV'].values
print(x[:3]) # [[4.98] [9.14] [4.03]]
print(y[:3]) # [24.  21.6 34.7]

# 단항을 통한 단순선형회귀 모델
model = LinearRegression()

# 다항 특성(변수) 
quad = PolynomialFeatures(degree=2)
cubic = PolynomialFeatures(degree=3)
x_quad = quad.fit_transform(x)
x_cubic = cubic.fit_transform(x)
print(x_quad[:3])
print(x_cubic[:3])

# 단순회귀
model.fit(x, y)
x_fit = np.arange(x.min(), x.max(), 1)[:, np.newaxis]
y_lin_fit = model.predict(x_fit) # 그래프에 표시용
# print('y_lin_fit:', y_lin_fit)
model_r2 = r2_score(y, model.predict(x))
print('model_r2 :', model_r2) # 0.544146297

# 다항(2차)
model.fit(x_quad, y)
y_quad_fit = model.predict(quad.fit_transform(x_fit))
q_r2 = r2_score(y, model.predict(x_quad))
print('q_r2 :', q_r2) # 0.64071689

# 다항(3차)
model.fit(x_cubic, y)
y_cubic_fit = model.predict(cubic.fit_transform(x_fit))
c_r2 = r2_score(y, model.predict(x_cubic))
print('c_r2 :', c_r2) # 0.65784764


# 시각화
plt.scatter(x,y,label='초기 데이터')
plt.plot(x_fit, y_lin_fit, linestyle=":",label="linear fit(d=1), $R^2=%.2f$"%model_r2, lw=3)
plt.plot(x_fit, y_quad_fit, linestyle=":",label="quad fit(d=2), $R^2=%.2f$"%q_r2, lw=3, c='r')
plt.plot(x_fit, y_cubic_fit, linestyle=":",label="cubic fit(d=3), $R^2=%.2f$"%c_r2, lw=3, c='k')
plt.xlabel('하위계층비율')
plt.ylabel('주택가격')
plt.legend()
plt.show()


