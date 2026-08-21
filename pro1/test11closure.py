# closure : Scope에 재약을 받지 않는 변수들을 포함하고 있는 코드블럭이다.
# 내부 함수의 주소를 반환해 함수 밖에서 함수 내의 멤버를 참조하기

def funcTimes(a , b):
    c = a*b
    print('c:', c)
    return c

print(funcTimes(2,3))
#print('c:',c) #NameError: name 'c' is not defined

kbs = funcTimes(2,3)
print(kbs)
kbs = funcTimes # 주소가 찍힌다.
print(kbs)
print(2,3)
print(id(funcTimes),id(kbs)) #두 개의 주소는 같다.

mbc = sbs = kbs #세 개의 주소가 같다.
del funcTimes # funcTimes 함수명 삭제 (참조 변수 삭제)
# print(funcTimes(2,3)) #NameError: name 'funcTimes' is not defined
print(mbc(3,4))
print(sbs(3,4))
print(kbs(3,4))

# 클로저란? 어떤 함수의 내부 함수가 외부 함수의 변수를 참조할 때, 외부 함수가 종료된 후에도 내부 함수가 외부 함수의 변수를 참조할 수 있도록 어딘가에 저장하는 함수
print('\n-----클로저를 사용하지 않은 경우------')
def out():
    count = 0
    def inn():
        nonlocal count
        count += 1
        return count
    print(inn())

#print(count) #err
out()
out()

print('\n-----클로저를 사용한 경우------')
def outer():
    count = 0
    def inner():
        nonlocal count
        count += 1
        return count
    return inner # 요것이 클로저 : 배부 함수의 주소를 반환함

var1 = outer()
print('var1 주소:', var1) #<function outer at 0x000001B8FD31F950>
print('count:', var1())
print('count:', var1())
#print(var1.count) #외부에서 직접접근은 불가 , 참조만 가능
print('클로저 내부 확인:', var1.__closure__) #__명령__: 파이썬 고유 명령
myvar = var1()
print(myvar)
print()
var2 = outer() # 새로운 객제(inner 함수) 생성
print(var2)
print(var2)


print('\n수량 * 단가 * 세금한 결과를 출력허가 ---')
def outer2(tax):  # tax는 지역 변수
    def inner2(su, dan):
        amount = su * dan * tax
        return amount
    return inner2

# 1분기에는 su * dan에 대한 tax는 0.1 부과
q1 = outer2(0.1)
result1 = q1(5,50000)
print('result1: ', result1)
result2 = q1(2,10000)
print('result2: ', result2)

# 2분기에는 su * dan에 대한 tax는 0.05 부과
q2 = outer2(0.05)
result3 = q2(5,50000)
print('result1: ', result3)
result4 = q2(2,10000)
print('result2: ', result4)

print('\n\n일급함수(객체): 함수안에 변수나 상수 전달, 함수 안에 함수, 인자로 함수 전달, 반환값이 함수')  # 일급함수:프로그래밍 언어에서 함수를 일반적인 값이나 변수처럼 다루는 것을 말한다.
def func1(a, b):
    return a + b
func2 = func1 #함수를 변수나 상수를 저장
print(func1(3,4))
print(func2(3,4))

print()

def func3(fu): # 인자로 함수를 전달
    def func4(): # 함수 안에 함수
        print('나는 내부 함수야')
    func4
    return fu # 빈환 값이 함수
mbc = func3(func1) #인자로 함수 전달함
print(mbc(6,7))

print('\n축약함수(lamda function) : 여러 줄의 함수 정의를 한줄로 간단하게 줄여쓰는 함수 ')
# 형식  -- lambda 매개변수,... : 표현식  <--- return 없이 결과 반환

def hapFunc(x,y):  # 프로그램 종료시까지 메모리를 유지
    return x + y

print(hapFunc(1,2))
#위 코드를 람다로 표현하면
print((lambda x , y:x + y)(1, 2)) # 단발성(휘발성) - 실행과 동시에 메모리 사라짐

gg = lambda x, y:x + y
print(gg) #<function <lambda> at 0x000001425D953A00>
print(gg(1, 2))

gg2 = lambda x,y:x + y
print(id(gg), id(gg2))
print((lambda x,y:x + y) is (lambda x,y:x + y)) # 다른 객체이기 떄문에 false가 나옴

print()
kbs = lambda a, su = 10: a + su
print(kbs(5))
print(kbs(5, 6)) # 6이 su에 들어감

print()
sbs = lambda a, *tu, **di : print(a, tu, di)
sbs(1,2,3,var1=4, var2=5) # 1 (2,3) {'var1': 4, 'var2': 5}

print('\n임의의 함수에서 람다 사용하기')
# filter() : 반복가능한 객체 (리스트 등) 특정조건에 맞는 요소만 골라낼 때 사용
# 기본구조는 filter(함수, 반복가능한 객체)
print(list(filter(lambda a:a < 5, range(10)))) # [0, 1, 2, 3, 4] []:list
print(list(filter(lambda a:a % 2, range(10)))) # [1, 3, 5, 7, 9]
# print(bool(0), bool(1)) # False True

# filter를 이용해 1~100 사이의 정수 중 5의 배수이거나 7의 배수만 출력(리스트)
print(list(filter(lambda a:a % 5 == 0  or a % 7 == 0, range(1, 101))))

