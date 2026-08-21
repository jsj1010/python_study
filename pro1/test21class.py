kor = 100 # 모듈의 멤버 : 전역변수

def abc():
    kor = 0 # 함수내의 지역변수
    print('모듈의 멤버 함수')

class My:
    kor = 80 # My클래스 멤버 변수(My type 객체 공유 지원)

    # def __init__(self): - 초기화 작업이 없는 경우 생성자는 생략 가능
    #     pass

    def abc(self):
        print('My 클래스 멤버 메소드')

    def show(self):
        # kor = 77 # 메소드 내의 지역변수
        print(kor)
        print()
        print(self.kor)
        abc() 
        self.abc

myobj = My() # 생성자 호출 
myobj.show() 
print('-------------------')

myobj2 = My()
print(myobj2.kor)
myobj2.kor = 99
print(myobj2.kor)

print('~~~~~~~~~')
myobj3 = My()
print(myobj3.kor)