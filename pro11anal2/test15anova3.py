# 어느 음식점의 매출과 날씨 자료를 이용해 온도에 따른 매출액 평균의 차이 검정 -------------------------

# 세 집단 : 추움, 보통, 더움

# 매출 데이터 : tsales.csv
# 날씨 데이터 : tweather.csv

# 귀우 : 온도에 따라 매출액의 평균에 차이가 없다.
# 대립 : 온도에 따라 매출액의 평균에 차이가 있다.

from scipy import stats
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import koreanize_matplotlib
import numpy as np

pd.set_option('display.max_columns', None)

# 매출 데이터 읽기
sales_data = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/tsales.csv", dtype={'YMD':'object'}) # int => object로 변환해 읽기
print(sales_data.head(2))
print(sales_data.info()) # 328 * 3

# 날씨 데이터 읽기
wt_data = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/tweather.csv")
print(wt_data.head(2))
print(wt_data.info()) # 702 * 9

print()
# tsales.csv : YMD 20190514, wt_data: tm 2018-06-01 이므로 병합을 위해 변환
wt_data.tm = wt_data.tm.map(lambda x:x.replace("-", ""))
print(wt_data.head(2))
#    stnId        tm  avgTa  minTa  maxTa  sumRn  maxWs  avgWs  ddMes
# 0    108  20180601   23.8   17.5   30.2    0.0    4.3    1.9    0.0

print()
# 두 데이터가 병합
frame = sales_data.merge(wt_data, how='left', left_on='YMD', right_on='tm')
print(frame.columns) 
# [ YMD    AMT  CNT  stnId  tm  avgTa  minTa  maxTa  sumRn  maxWs  ]
print(frame.head(3), ' ', len(frame)) # 328

data = frame.iloc[:, [0, 1, 7, 8]]
print(data.head())
print('결측치 확인 :', data.isnull().sum())

plt.boxplot(data.maxTa)
plt.show()
print(data['maxTa'].describe()) # min:4.90, mean:18.59, max:36.80

# 온도를 세 그룹으로 분리 (연속형 -> 범주형)
data['ta_gubun'] = pd.cut(data['maxTa'], bins=[-5, 8, 24, 37], labels=[0, 1, 2])
print(data.head(3), ' ',data['ta_gubun'].unique())
# 요인1개(온도) : 그룹3개(0,1,2)

# 정규성 / 등분산성 확인
x1 =np.array(data[data['ta_gubun']==0].AMT) # 추움 그룹 매출
x2 =np.array(data[data['ta_gubun']==1].AMT) # 보통 그룹 매출
x3 =np.array(data[data['ta_gubun']==2].AMT) # 더움 그룹 매출
print(x1[:5])

print()
print(stats.shapiro(x1).pvalue) # 추움 그룹 정규성 검정
print(stats.shapiro(x2).pvalue) # 보통 그룹 정규성 검정
print(stats.shapiro(x3).pvalue) # 더움 그룹 정규성 검정

print(stats.levene(x1, x2, x3).pvalue) # 등분산성 검정

print("\n온도별 매출액 평균")
# pandas 지수 표기법 해제
pd.set_option('display.float_format', '{:,.2f}'.format)

spp = data.loc[:, ['AMT', 'ta_gubun']]
print(spp.groupby('ta_gubun').mean())
print(f'{np.mean(x1):.2f}') # 1032362.32
print(f'{np.mean(x2):.2f}') # 818106.87
print(f'{np.mean(x3):.2f}') # 553710.94

group1, group2, group3 = x1, x2, x3
print(stats.f_oneway(group1,group2,group3))
# F_onewayResult(statistic=np.float64(99.1908012029983), pvalue=np.float64(2.3607371010895207e-34))ㄴ
# 해석 : pvalue=2.3607371010895207e-34 < alpha 0.05 이므로 귀무 기각
# 해당 음식점은 온도에 따라 매출액의 평균에 차이가 있다.라는 의견을 수렴한다.
print()
# 정규성이 꺠지면 stats.kruskal() 사용, 등분선성이 깨지면 welch's ANOVA
print(stats.f_oneway(group1,group2,group2))

print()
# wlch's ANOVA 검정 - 등분산 가정 불필요
print(stats.f_oneway(group1,group2,group3, equal_var=False))

# 검정방법을 제공하는 라이브러리는 다양하다
# 예를 들어 다른 라이브러리로 welch's ANOVA 검정 수행
# pip install pingouin
from pingouin import welch_anova
print(welch_anova(dv='AMT', between='ta_gubun', data=data))

print()
# 사후검정
from statsmodels.stats.multicomp import pairwise_tukeyhsd
# tukResult = pairwise_tukeyhsd(endog=df.pay, groups=df.group)
tukResult = pairwise_tukeyhsd(endog=spp['AMT'], groups=spp['ta_gubun'])
print(tukResult)

# 시각화
tukResult.plot_simultaneous(xlabel='매출액 평균', ylabel='온도')
plt.show()
