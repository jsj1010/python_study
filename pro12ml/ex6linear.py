print('\n모델 작성 방법 3 : linregress 사용 - 모델 생성')
from scipy import stats
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# IQ에 따른 시험점수 예측
score_iq = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/score_iq.csv")
print(score_iq.head(3))
print(score_iq.info())
x= score_iq.iq
y= score_iq.score
print(x[:3])
print(y[:3])

print('상관계수 :', np.corrcoef(x,y)[0,1]) # 0.88222
print(score_iq[['iq','score']].corr())

# plt.scatter(x,y)
# plt.show()

# 단순선형회귀분석 모델 생성 - 인과관계가 있다는 가정 하에 진행
model = stats.linregress(x,y)
print(model)
# LinregressResult(slope=0.6514309, intercept=-2.85644712219760, rvalue=0.88222034, pvalue=2.84768952066, stderr=0.028577934409, intercept_stderr=3.546211918048529
# 단순선형회귀분석만 가능 (다중회귀 x), 예측함수 (predict) x
print('가중치 : ', model.slope)  # 0.6514309527270086
print('편향 : ', model.intercept) # -2.8564471221976078
print('p값 : ', model.pvalue) # 2.8476895206670203e-50 < 0.05 이므로 두 변수는 인과관계가 있다.

plt.scatter(x, y)
plt.plot(x, model.slope * x + model.intercept, c='r')
plt.show()
# predict() 지원안함

newdf = pd.DataFrame({'iq':[55, 66, 77, 88, 150]})
print('점수예측 :\n', np.polyval([model.slope, model.intercept], newdf).ravel().round())




