# [two-sample t 검정 : 문제1] 
# 다음 데이터는 동일한 상품의 포장지 색상에 따른 매출액에 대한 자료이다. 
# 포장지 색상에 따른 제품의 매출액에 차이가 존재하는지 검정하시오.
# 수집된 자료 :  
#    blue : 70 68 82 78 72 68 67 68 88 60 80
#    red : 60 65 55 58 67 59 61 68 77 66 66

from scipy import stats
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import koreanize_matplotlib
import seaborn as sns
import numpy as np

blue = [70, 68, 82, 78, 72, 68, 67, 68, 88, 60, 80]
red = [60, 65, 55, 58, 67, 59, 61, 68, 77, 66, 66]

print('파랑 평균:', np.mean(blue)) # 72.81818181818181
print('빨강 평균:', np.mean(red))  # 63.81818181818182

# 선행조건 : 두 집단의 정규성 만족, 등분산 만족 여부.
# 정규성 검정
print('파랑 정규성 : ', stats.shapiro(blue).pvalue) # 파랑 정규성 :  0.5102310071741448 > 0.05 만족
print('빨강 정규성 : ', stats.shapiro(red).pvalue) # 빨강 정규성 :  0.5347933238609744 > 0.05 만족

# 등분산성 검정
print(stats.levene(blue, red).pvalue) # 0.43916444685083794 > 0.05 만족


# 독립표본 t검정
print(stats.ttest_ind(blue, red, equal_var=True))
# statistic=2.9280203225212174 pvalue=0.008316545714784409
# 해석:정규성, 등분산성 조건은 충족 / 
# pvalue=0.008316545 < alpha 0.05이라 귀무가설 기각 
# 색에 따라 매출액의 평균에 차이가 있음. 파랑 > 빨강 (파랑이 좀 더 선호됨)




# ----------------------------------------------------------------------------------------
# [two-sample t 검정 : 문제2]  
# 아래와 같은 자료 중에서 남자와 여자를 각각 15명씩 무작위로 비복원 추출하여 혈관 내의 콜레스테롤 양에 차이가 있는지를 검정하시오.
# 수집된 자료 :  
#   남자 : 0.9 2.2 1.6 2.8 4.2 3.7 2.6 2.9 3.3 1.2 3.2 2.7 3.8 4.5 4 2.2 0.8 0.5 0.3 5.3 5.7 2.3 9.8
#   여자 : 1.4 2.7 2.1 1.8 3.3 3.2 1.6 1.9 2.3 2.5 2.3 1.4 2.6 3.5 2.1 6.6 7.7 8.8 6.6 6.4

from scipy import stats
import pandas as pd
import numpy as np

M = [0.9, 2.2, 1.6, 2.8, 4.2, 3.7, 2.6, 2.9, 3.3, 1.2, 3.2, 2.7, 3.8, 4.5, 4, 2.2, 0.8, 0.5, 0.3, 5.3, 5.7, 2.3, 9.8]
W = [1.4, 2.7, 2.1, 1.8, 3.3, 3.2, 1.6, 1.9, 2.3, 2.5, 2.3, 1.4, 2.6, 3.5, 2.1, 6.6, 7.7, 8.8, 6.6, 6.4]

m_choice = np.random.choice(M, size=15, replace=False)
w_choice = np.random.choice(W, size=15, replace=False)

# 평균
print('남자 평균 :', np.mean(m_choice))
print('여자 평균 :', np.mean(w_choice))

# 검정
print('남자 정규성 :', stats.shapiro(m_choice))
print('여자 정규성 :', stats.shapiro(w_choice))

# 남자 평균 : 3.620000
# 여자 평균 : 3.546666
# 남자 정규성 : statistic=0.86814582, pvalue=0.03169394
# 여자 정규성 : statistic=0.81628978, pvalue=0.00599543

# 남자 정규성 : pvalue=0.03169394 < alpha0.05   귀무가설 기각
# 여자 정규성 : pvalue=0.00599543 < alpha0.05   귀무가설 기각

# 등분산성 검정
print('등분산성 :', stats.levene(m_choice, w_choice).pvalue)    # 등분산성 : 0.9919066478011005

# 독립 표본 t검정
result = stats.ttest_ind(m_choice, w_choice, equal_var=True)
print(result)

if result.pvalue < 0.05:
    print('귀무가설 기각 : 남녀 평균 콜레스테롤 양에 차이가 있다')
else:
    print('귀무가설 채택 : 남녀 평균 콜레스테롤 양에 차이가 없다')

# ----------------------------------------------------------------------------------------------
# [two-sample t 검정 : 문제3]
# DB에 저장된 jikwon 테이블에서 총무부, 영업부 직원의 연봉의 평균에 차이가 존재하는지 검정하시오.
# 연봉이 없는 직원은 해당 부서의 평균연봉으로 채워준다.

import pymysql
from scipy import stats
import pandas as pd

alpha = 0.05

config = {
    'host':'127.0.0.1',
    'user':'root',
    'password':'123',
    'database' : 'test',
    'port' : 3306,
    'charset':'utf8'
}

sql = """
SELECT j.jikwonno 사번, j.jikwonname 이름, b.busername 부서, j.jikwonpay 연봉
from jikwon as j
INNER JOIN buser AS b
ON j.busernum = b.buserno
WHERE b.busername IN ('총무부', '영업부')
"""

conn = pymysql.connect(**config)

try:
    with conn.cursor() as cursor:
        cursor.execute(sql)

        rows = cursor.fetchall()

    df = pd.DataFrame(rows, columns=['사번', '이름', '부서', '연봉'])
finally:
    conn.close()

# print('조회결과')
# print(df)

df['연봉'] = pd.to_numeric(df['연봉'], errors='coerce')

# 부서별 직원 자료 분리
chongmu = df[df['부서'] == '총무부']
youngup = df[df['부서'] == '영업부']

# 각 부서에서 연봉 열만 선택
pay1 = chongmu['연봉']
pay2 = youngup['연봉']

print('\n총무부 현황')
print('전체 인원:', len(pay1))
print('연봉이 있는 인원:', pay1.count())
print('평균 연봉:', pay1.mean())
print('연봉 결측치 수:', pay1.isnull().sum())

print('\n영업부 현황')
print('전체 인원:', len(pay2))
print('연봉이 있는 인원:', pay2.count())
print('평균 연봉:', pay2.mean())
print('연봉 결측치 수:', pay2.isnull().sum())


pay1 = pay1.fillna(pay1.mean())
pay2 = pay2.fillna(pay2.mean())

# 정규성 확인
if len(pay1) >= 3 and len(pay2) >= 3:
    print('\n총무부 정규성 p값:', stats.shapiro(pay1).pvalue)
    print('영업부 정규성 p값:', stats.shapiro(pay2).pvalue)
else:
    print('\n정규성 검정은 각 부서에 자료가 최소 3개씩 필요합니다.')

# 등분산성 확인
levene_result = stats.levene(pay1, pay2)
print('등분산성 p값:', levene_result.pvalue)


# 기본값이 양측 검정, 평균이 서로 다른지 검정한다.
# 귀무 가설 : 두 부서의 연봉 분산은 같다
# 대립 가설 : 두 부서의 연봉 분산은 다르다
if levene_result.pvalue >= alpha:
    print('등분산 귀무가설을 기각 X: 등분산 가정한 t 검정')
    result = stats.ttest_ind(pay1, pay2, equal_var=True)
else:
    print('등분산을 가정하지 않는 Welch t 검정')
    result = stats.ttest_ind(pay1, pay2, equal_var=False)

print('\n독립표본 t 검정 결과')
print('총무부 평균 연봉:', pay1.mean())
print('영업부 평균 연봉:', pay2.mean())
print('t 통계량:', result.statistic)
print('p값:', result.pvalue)
print('유의수준:', alpha)

if result.pvalue < alpha:
    print('귀무가설 기각')
    print('총무부와 영업부의 평균 연봉에 통계적으로 유의한 차이가 있다.')
else:
    print('귀무가설 채택')