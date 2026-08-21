# function : 여러개의 수행문을 하나의 이름으로 묶은 실행 단위
# 함수 고유의 공간을 만든다.
# 자원의 재활용이 가능
# ...

# 내장함수 : 일부 체험 자동으로 제공
print(sum([1,2,3]))    
print(8,bin(8)) # 2진수로 표현 
print(eval('4+5'))
print(round(1.2), round(1.6)) # 반올림            
import math
print(math.ceil(1.2), ' ', math.ceil(1.6)) #올림 
print(math.floor(1.2), ' ', math.floor(1.6)) #내림

b_list= [True, 1, False]
print(all(b_list)) #false
print(any(b_list)) #True

data1 = [10,20,30]
data2 = ['a', 'b']
for i in zip(data1, data2):
    print(i)

#(10, 'a')
#(20, 'b')

# ...

import builtins # 자동 로딩 # 파일 명
builtins.print('자동로딩')
builtins.print(builtins.sum([2,5]))
# print = 7 (x)
# print("안녕") (x)



