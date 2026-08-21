# 사용자 정의 함수
"""
def 함수명(가인수,,,): # dummy argument, 매개변수(parameter)
    #...
    return 반환값 # 1개만 반환, return 이 없으면 return None

함수명(실인수,,,) # 함수 호출 # actual argument 
"""

print('뭔가를 실행 ...')

# 함수 선언
def doFunc1():
    print('doFunc 수행')
    return None # 생략가능

def doFunc2(name):
    print('name:', name)

def doFunc3(arg1, arg2):
    res = arg1 + arg2
    return res

def doFunc4(a1, a2):
    imsi = a1 + a2
    if imsi % 2 == 1:
        return  # 함수내에 return은 무조건 탈출
    else:
        return imsi

    # kbs = 9 쓰지마~~~~

# 함수 호출
doFunc1()
print('어떤 작업 처리')
doFunc1()
print('함수 주소는', doFunc1)
print('함수 주소는', id(doFunc1))
imsi = doFunc1   # 함수의 주소 치환
imsi()   # 함수의 실행 가능
imsi2 = doFunc1 # 함수 실행 결과를 기억
print(imsi2)  # 실행 결과를 출력  
print(doFunc1())
print('----------------')
#doFunc2() #TypeError: doFunc2() missing 1 required positional argument: 'name'
doFunc2(7)
doFunc2('홍길동')
print('----------------')
doFunc3("대한","민국") #합쳐지기만 하고 출력안함
print(doFunc3(3,4)) # 3+'사'처럼 타입이 다르면 안됨
result = doFunc3("3" , "4")
print('result :', result)
print('----------------')
print(doFunc4(3,4)) # None
print(doFunc4(3,5)) # 8

print('**'*30)

def triArea(a , b):
    c = a*b/2
    triAreaPrint(c)

def triAreaPrint(arg):
    print('삼각형의 면적은', arg)

triArea(20,30)

print()

def passResult(kor, eng):
    ss = kor + eng
    if ss >= 50:
        return True
    else:
        return False

if passResult(20, 40):
    print("합격")
else:
    print("불합격")

print()
def swapFunc(a, b):
    return {b, a}  # return (b,a) # 반환값은 반드시 1개

a=10; b=20
print(a,'',b)
print(swapFunc(a, b))

print()
def funcTest():
    print('funcTest 멤버 처리')
    def funcInner():
        print('내부함수 funncinner 실행')
    funcInner()
funcTest()

print()
# if 조건식 안에 함수 적용
def isOdd(para):
    return para % 2 == 1 #홀수이면 True반환

mydict = { x:x for x in range(11) if isOdd(x)}
print(mydict)

print('\n변수의 생존 범위(scope rule)')
# 변수가 저장되는 이름공간은 변수가 어디에 선언되었는가에 따라 생존 시간이 다르다.
# 전역 변수, 지역 변수
# local > Enclosing function > global > built-in
player = '전국대표' # 전역변수 (현재파일(모듈) 어디서든 호출 가능)
name = '신기해'

def funcsoccer():
    name = '이기자' #지역변수 (현재함수 내에서만 유효)
    city = '서울'
    print(f'이름은 {name} 수준은 {player}')
    print(f'지역은 {city}')
funcsoccer()
print(f'이름은 {name} 수준은 {player}')
# print(f'지역은 {city}') # NameError: name 'city' is not defined
print()
a = 10; b = 20; c = 30  # 전역 변수 global

def foo():
    a = 7 # 지역 변수 local
    b = 100

    def bar():
        global c  # bar의 멤버가 아니라 모듈의 멤버가 된다.(전역)
        nonlocal b  # ---> foo수준으로 감
        b = 8 # 지역 변수  
        print(f'bar수행 중 a:{a}, b:{b}, c:{c}')
        c = 9
        # b = 200 # bar 수준의 지역 변수
        b = 200  # foo수준의 지역변수
    bar()
    print(f'bar수행 후 a:{a}, b:{b}, c:{c}')
foo()
print(f'foo수행 후 a:{a}, b:{b}, c:{c}')

print()
g = 1
print('g :', g)
def func():
    global g  # 글로벌 없이 그냥하면 오류남
    a = g
    g = 2
    return a
print(func())
print('g :', g)
print('작업종료')
