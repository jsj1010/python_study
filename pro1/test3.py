# 기본 자료형 : int, float, bool, complex
# 묶음 자료형 : str, list, tuple, dict

# str : 문자열 저장 단위, 순서0, 수정x
s = "sequence" #기준은 왼쪽부터 0.1,2,3... 우측 기준으로는  <- 반대쪽으로 0,-1,-2...
print("길이(크기)", len(s))
print("포함횟수 : ", s.count('e'))
print('검색위치 :', s.find("e"), s.find('e',3), s.rfind('e'))
print('첫글자 유무 : ', s.startswith('s'))

print()
ss = 'mbc'
print(ss, id(ss))
ss='abc'
print(ss, id(ss))

print('인덱싱 / 슬라이싱') # s = sequence 에서 찾아냄
print(s[0],s[5],s[-1]) # s, n, e <== 인덱싱
print(s[0:4],s[:4],s[-4:-1]) #sequ sequ enc <==
print(s[::2], s[0:8:3], s[0:len(s):1])  # 증가치를 부여하여 사용

print("*" * 10)


# list: 다양한 종류의 자료 묶음형, 순서0, 수정0, 중복0 []안에 있음
a = [1,2,3]
print(a, a[0], a[0:2])
b = [0, a, 20.5, True, '문자열']
print(b, b[0], b[1], b[1][1])
print()
family= ['엄마','아빠','나','여동생']
print(family, id(family))
family.append('남동생') # 남동생을 추가한다. (마지막에 추가)
print(family, id(family)) #주소가 같은 것을 보고 대체가 아닌 수정임을 알수있다.
family.remove('나') #나를 제거한다. (삭제)
print(family) 
family.insert(0,'할머니') # 특정 위치에 삽입
print(family)
family.extend(['삼촌', '고모', '조카']) # 집합을 추가,누적(1)
family += ['이모'] # 집합을 추가,누적(2)
print(family)
family.remove('아빠') # 값에 의한 삭제
del family[2] # 순서에 의한 삭제
print(family)

print()
kbs = ['123', '23', '234']
kbs.sort() # 문자열 정열
print(kbs) # ['123', '23', '234']

mbc = [123, 34, 234]
mbc.sort() # 오름차순(ancending) - 리스트 값 순서가 바뀜
print(mbc) # [34, 123, 234] 
kbs.sort(reverse=True) # 내림차순(descending)
print(kbs) # [234, 123, 34]

sbs =  [123, 34, 234]
ytn = sorted(sbs) #새 데이터가 할당되도 원본 데이터를 가져감
print(ytn)
print(sbs)


print("*"*10)


#tuple : 리스트와 유사, 읽기전용 -수정x ()안에 있음
t = (1,2,3,4)
t = 1,2,3,4 # 위와 동일
print(t, type(t)) #(1,2,3,4) <class 'tuple'>

k = (1,) # 주의 (1)로 하면 class int로 인식
print(k, type(k))

print(t[0], t[1:3]) # 1 (2,3)
# t[0] = 9 # 'tuple' object does not support item assignment  ---- 튜플은 수정불가니 중요한 데이터는 여기에 담는게 좋구 수정할거면 인덱싱과 슬라이싱

# 튜플 값 수정시 리스트로 형변환 사용
imsi = list(t) # type변환
print(type(imsi)) #<class 'list'>
imsi[0] = 9
t = tuple(imsi)
print(t, type)

print('--'*10)
# set : 순서x, 중복x, 수정0
ss = {1, 2, 3, 2} #{1,2,3}과 같다 중복된 건 없어짐
print(ss, type(ss))
ss2= {3, 4}
print(ss.union(ss2)) # 합집합
print(ss.intersection(ss2)) # 교집합
print(ss - ss2, ss | ss2, ss & ss2) # 차, 합, 교집합 {1,2} {1,2,3,4}

ss.update({6,7})
print(ss) 
ss.discard(7) # 값삭제
ss.discard(7) # 값삭제 : 해당값 없으면 통과
ss.remove(6) # 값삭제
# ss.remove(6)  # 값삭제 : 해당값 없으면 err
print(ss)

print()
li = ['aa','aa','bb','cc','aa']
print(li)
imsi = set(li)
li = list(imsi)
print(li) # ['aa','cc','bb']


print('--'*10)


# dict : 사전 자료형 {'키':값} 형태
# 방법1
mydic = dict(k1=1, k2='ok' , k3=1234)   # 나중에 json에 사용됨
print(mydic, type(mydic)) # {k1 :1, k2: ok k3:1234 }<class 'dic'>

# 방법2
dic = {'파이썬':'뱀', '자바':'커피', '번호':'123'}
print(dic, type(dic))
print(len(dic))
print(dic['자바']) #키로 값을 검색
print(dic.get('자바')) # 위와 같은 뜻
# print(dic[0]) #딕셔너리는 인덱싱 불가( 순서가 존재x)

dic['금요일'] = 'wow' # 추가
print(dic)

del dic['번호'] # 삭제
print(dic)

print(dic.keys()) # 앞에 있는 키값만 리스트로 뽑아냄
print(dic.values()) # 앞에 있는 벨류값만 리스트로 뽑아냄

