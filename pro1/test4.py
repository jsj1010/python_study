# 정규표현식 : ...
import re # 정규표현식 지원 모듈 로딩


ss = "1234 abc가나다ABC_1234555실습중78입니다_6'python is fun"
print(ss)
# re.findall(패턴, 대상문자열)  
print(re.findall(r'123', ss)) # ['123','123'] #패턴 앞에는 r을 꼭 붙여줘야함
print(re.findall(r'가나', ss))
print(re.findall(r'[013]', ss))
print(re.findall(r'[0-9]', ss))
print(re.findall(r'[0-9]+', ss))
print(re.findall(r'[0-9]{2}', ss))
print(re.findall(r'[0-9]{2,3}', ss))

print(re.findall(r'[ab]', ss))
print(re.findall(r'[a-zA-Z]', ss))
print(re.findall(r'[a-zA-Z]+', ss))
print(re.findall(r'[가-핳]+', ss))

print(re.findall(r'\d',ss)) # 모든 숫자
print(re.findall(r'\d+',ss))
print(re.findall(r'\D+',ss)) # \d의 반대  숫자외에 모두

print(re.findall(r'\s',ss)) # 공백, 탭 문자와 매핑
print(re.findall(r'\s+',ss)) 
print(re.findall(r'\S+',ss))

# .....


