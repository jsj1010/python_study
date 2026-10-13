# 고수준의 자료구조(Series ,DataFrame)와 빠르고 쉬운 데이터 분석용 함수 제공
# 통합된 시계열 연산, 축약연산, 누락 데이터 처리, sql, 시간화... 등을 제공
# 데이터 랭글링(Data Wrangling), 데이터 먼징(Data Munging)을 효율적으로 처리 가능 
# 데이터 랭글링(Data Wrangling)과 데이터 먼징(Data Munging)은 분석이나 머신러닝에 활용하기 쉽도록 원자료(Raw Data)를 수집, 정제, 변환하는 과정

import pandas as pd
import numpy as np
from pandas import Series, DataFrame

# series: 일련의 객체를 담을 수 있는 1차원 배열과 같은 자료구조로 색인(index)을 갖는다
obj = pd.Series([3,7,-5,4]) #(3, 7, -5, 4) - 0, {3, 7, -5, 4} - X, dict - 0
# obj = pd.Series([3,7,-5,4,'일']) #요소 값 모두가 object type
print(obj,type(obj))

print()
obj2 =pd.Series([3, 7, -5, 4], index = ['a', 'b', 'c', 'd'])
print(obj2)
print(obj2.sum(), ' ', np.sum(obj2), ' ', sum(obj2))
print(obj2.std()) # 5.123475382979799 pandas의 함수는 numpy 기반

print(obj2.index) # 색인만 출력
print(obj2.values) # 값만 출력

# 인덱싱 / 슬라이싱
print(obj2['a']) # 'a' 인덱스의 값 : 3
print(obj2[['a']]) # a  3

print(obj2[['a','b']]) # a   3 b   7
print(obj2['a':'c']) # 

print()
# print(obj2[2]) #  keyError: 인덱스 순서 문자열을 사용 중 
print(obj2.iloc[2]) # iloc[위치번호] - Series 2번째 위치에 있는 값
print(obj2.loc['c']) # loc['인덱스 이름']

print()
print(obj2[1:3])
print(obj2.iloc[[2, 1]]) # 위치 기반 2번 1번 순서대로 출력
print(obj2.iloc[[1, 2]]) 

print()
print('a' in obj2) # 인덱스에 'a' 여부 확인 True
print('k' in obj2)

print('\n파이썬 dict 자료를 Series 객체로 생성')
names ={'mouse':5000, 'keyboard':35000, 'monitor':550000}
print(names, type(names))

obj3 = Series(names)
print(obj3,type(obj3)) # mouse 5000 ...
obj3.index = ['마우스','키보드','모니터']
print(obj3,type(obj3)) # 마우스 5000...

obj.name = '상품가격'
print(obj3) # ... 모니터 550000 NAME: 상품가격, dtype: int64 