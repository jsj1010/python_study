# sigmoid function 적용 연습
# LogisticRegression 모델은 wx + b를 logic변환한 값에 sigmoid function 처리한 값을 사용
# log(p/(1-p)) = wx + b라고 정의 됨
# 그러므로 z = wx + b --> sigmoid(z) --> p(0 ~ 1) : 이항 분류

# sigmoid function 수식에 의해 변환된 값 확인
import math

def MysigmoidFunc(num):    # num: logit 변환한 값이라 가정
    return 1 / (1+ math.exp(-num))
print(MysigmoidFunc(3))
print(MysigmoidFunc(1.5))
print(MysigmoidFunc(-5.0))
print(MysigmoidFunc(-10))
# 0.9525741268224334
# 0.8175744761936437
# 0.0066928509242848554
# 4.5397868702434395e-05

import numpy as np
import matplotlib.pyplot as plt
import koreanize_matplotlib

print('\n로짓(logit) 변환된(가정) 값으로 시그모이드 함수 통과 후 결과 시각화')
x = np.linspace(-10, 10, 50) # 입력자료 (연속형)
print(x)


# 선형결합(이미 logit된 값)
w = 1.5
b = -2
z = w * x + b

def OurSigmoidFunc(z):   
    return 1 / (1+ np.exp(-z))

p = OurSigmoidFunc(z)
print('p: \n', p)

# 일부만 보기
print('x[:3] : ', np.round(x[:3], 3))  # [-10.     -9.592  -9.184]
print('z[:3](logit) :', np.round(z[:3], 3)) # [-17.    -16.388 -15.776]
print('p[:3](확률) : ', p[:3]) # [4.13993755e-08 7.63639448e-08 1.40858451e-07]

# 시각화
plt.figure(figsize=(8, 5))
plt.plot(x, p, label='sigmoid(z)', color='blue')
plt.axhline(0.5, color = 'red', linestyle = '--')
plt.title('z=wx + b --> sigmoid --> 확률(이항)')
plt.xlabel('x(입력값)')
plt.ylabel('p(확률값)')
plt.grid(True)
plt.legend()
plt.show()