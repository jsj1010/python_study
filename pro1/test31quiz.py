# 2. 클래스의 상속관계 연습문제 - 다양성

# class ElecProduct:

#     volume = 0

#     def volumeControl(self, volume):
#         pass

# class ElecTv(ElecProduct):
#     def nugusori1(self):
#         print("테레비 소리!!")

#     def volumeControl(self, volume):
#         self.volume = volume
#         print('찌리리리', volume)

# class ElecRadio(ElecProduct):
#     def nugusori2(self):
#             print("라디오 소리!!")

#     def volumeControl(self, volume):
#         radio_volume = volume
#         print('우와아아앙', radio_volume)

# tv = ElecTv()
# tv.volumeControl(10)
# tv.nugusori1()

# radio = ElecRadio()
# radio.volumeControl(20)
# radio.nugusori2()

# -----------------------------------------------------다른방법

class ElecProduct:  #부모 클래스
    voulume = 0
    def volumeControl(self, volume):
        print(f"{volume}을 조절한다")
        # pass


class ElecTv(ElecProduct): #자식클래스
    def volumeControl(self, volume): #오버라이딩
        print('나는 TV')
        print(f"{volume}을 리모컨으로 조절한다")

class ElecRadio(ElecProduct): #자식클래스
    def volumeControl(self, volume): #오버라이딩
        print('나는 radio')
        sori = volume
        print(f"{sori}을 주파수로 조절한다")

if __name__ == "__main__":
    electro_product = ElecProduct()
    electro_product.volumeControl(1)

    print()
    tv = ElecTv()
    tv.volumeControl(3)
    print()
    radio = ElecRadio()
    radio.volumeControl(5)
    print("-----다형성1------")
    product = tv
    product.volumeControl(2)
    print()
    product = radio
    product.volumeControl(2)

    print('----다형성2------')
    group = [ElecTv(),ElecRadio()]
    for g in group:
        g.volumeControl(3)
        print()






# 3. 다중상속 연습문제

# class Animal:

#     def move(self):
#         print("짐승같이 달리기!!!")

# class Dog(Animal):
#     name = "개"
#     def move(self):
#         print("개처럼 달리기 !!!")

# class Cat(Animal):
#     name = "고양이"
#     def move(self):
#         print("고양이처럼 달리기 !!!")

# class wolf(Dog, Cat):
#     pass

# class Fox(Dog, Cat):

#     def move(self):
#         print("여우처럼 달리기 !!!")
#     def foxMethod(self):
#         super().move()

# dogi = Dog()
# dogi.move()

# cati = Cat()
# cati.move()

# foxi = Fox()
# foxi.move()
# foxi.foxMethod()

#----------------------- 다른방법


class Animal: #최상위 클래스
    def move(self):
        print("동물은 움직인다")
        print()

class Dog(Animal): 
    name = "개" 
    
    def move(self): # Animal() 클래스의 move()메서드와 이름만 갖고 기능은 다른 오버라이딩
        print(f"{self.name}는 기분 좋으면 꼬리를 흔든다")



class Cat(Animal): #Animal에서 move() 받아오기

    name = "고양이"

    def move(self):
        print(f"{self.name}는 그루밍을 한다")

class Wolf(Dog, Cat):
    pass

class Fox(Cat,Dog):
    def foxMethod(self):
        print("아리는 꼬리가 9개")
        
    def move(self):
        print("여우의 움직임")
        
if __name__ =="__main__":

    #각 객체 생성완료
    Animal().move()

    print()
    d=Dog()
    d.move()
    print()
    c=Cat()
    c.move()
    print()
    w=Wolf()
    w.move()
    print()
    f=Fox()
    f.move()

    # 다형성

    print('------다형성--------')
    ani = [d,c,w,f]
    for a in ani:
        print(id(a))
        a.move()
        print()