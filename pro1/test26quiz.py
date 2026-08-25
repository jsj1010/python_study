# 1) 커피 자판기 

# class CoinIn:
#     coin = 0
#     change = 0

#     def culc(self, Count):
#         price = 200

#         self.Count = self.coin // price
#         self.change = self.coin % price

#         if self.Count == 0:
#             print('금액이 부족합니다.')
#         else:
#             print(f"몇잔을 원하냐: {self.Count}")
#             print(f"커피 {self.Count}잔과 잔돈{self.change}원")

# class Machine:
#     cupCount  = 1

#     def showData(self):
#         coin = int(input("동전을 넣으세요:"))

#         coinIn = CoinIn()
#         coinIn.coin = coin
#         coinIn.culc(self.cupCount)


# if __name__ == '__main__':
#     Machine = Machine()
#     Machine.showData()


# 다른 방법 

# class Machine:
#     def __init__(self):
#         self.coin_input = CoinIn(self) # 포함 

#     def showData(self):
#         coin = input('동전 입력')
#         count = input('몇 잔 입력')
#         self.coin_input.coin = int(coin) 
#         self.coin_input.calc(int(count))
#         change = self.coin_input.change

#         if (change >= 0) :
#             print("커피", count, "잔과 돈", change, "원")
#         else:
#             print("잔액이 부족합니다")

# class CoinIn:
#     def __init__(self, coin = 0, change = 0):
#         self.price = 200
#         self.coin = coin
#         self.change = change

#     def calc(self, cupCount):
#         total = cupCount * self.price
#         self.change = self.coin - total

# machine = Machine()
# machine.showData()



# 교수님 방식

class CoinIn():
    def __init__(self):
        self.cupPrice = 200

    def calc(self, coin, cupCount):
        totalPrice = self.cupPrice * cupCount

        if coin < totalPrice:
            return None
        else:
            change = coin - totalPrice
            return cupCount, change

class Machine():
    def __init__(self):
        self.coinIn = CoinIn() #포함

    def showData(self):
        while True:
            coin = int(input("동전을 입력하세요:"))
            cup = int(input("몇 잔을 원하세요:"))
            cupCount, change = self.coinIn.calc(coin, cup)

            if cupCount is None:
                print("요금이 부족합니다.")
            else:
                print(f"커피 {cupCount}잔과 잔돈{change}원")

            # 계속 실행 여부
            answer = input("계속할까요?(Y/N):")
            if answer.lower == 'n':
                print("종료합니다.")
                break
            

if __name__ == "__main__":

    # machine=Machine()
    # machine.showData()

    Machine().showData()