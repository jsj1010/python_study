# 배열 연산
# 기본 수학함수는 배열의 요소별로 적용되고, 
# +,-,*,/나 또는 add, subtract, multiply , divide  함수를 사용
# 벡터화 연산을 하므로 for문을 사용하지 않고 바로 배열에 대한 연산 가능

import numpy as np

# x = np.array([[1, 2],[3, 4]],dtype=np.float32)
x = np.array([[1., 2],[3, 4]])
print(x, ' ', x.dtype)

# y= np.arange(5,9)    # [5 6 7 8] int64 1차원 배열 생성
y = np.arange(5,9).reshape(2, 2) # 구조 변경 (1차원 -> 2차원)
y = y.astype(np.float32) # type 변경
print(y, ' ', y.dtype) #[[5. 6.][7. 8.]] float32

print(x.ndim, ' ', y.ndim) # 2  2

print()
print(x+y)           # 파이썬 연산자 사용
print(np.add(x,y))   # 넘파이 함수(유니버셜 함수:내부적으로 벡터화 연산) - 위 보다 속도 빠름
print()
print(x-y)        
print(np.subtract(x,y))  
print()
print(x*y)      
print(np.multiply(x,y))  
print()
print(x/y)          
print(np.divide(x,y))  
print()
print(np.sqrt(x), ' ', np.exp(x), ' ', np.log(x), ' ', np.cos(x))