# 어떤 데이터와 그 데이터를 처리하는 기능이 서로 밀접하게 관련되어 있다면
# 하나로 묶어 처리할 수 있다. 이를 클래스로 구현 가능하다.

# 두 점의 거리를 계산하기
# 기울기 
# 로그 처리


# 1) 좌표의 거리와 기울기는 단순한 수학연습이 아니라 나중에 ML 작업시 등장하게 된다.
#    거리는 나중에 KNN, k-Means, Embedding 유사도 등과 연결되고,
# 2) 기울기느 선형회귀를 거쳐 미분-Gradient Descent, 딥러닝의 학습원리로 연결된다.
# 3) 첨도,왜도가 큰 (편차가 큰 데이터...) 데이터를 로그변환하면
#    분포개선,범위차이 축소등으로 인해 모델을 안정적으로 수행가능

import math

class CalcTest:
    def __init__(self,x1,y1,x2,y2,offset:float=1.0):    # 두 점의 좌표를 얻기  
        self.x1=x1
        self.y1=y1
        self.x2=x2
        self.y2=y2

        #로그는 0과 음수를 허용하지 않으므로 offset으로 여기에 대처한다. (나중에 offset을 더하고 역변환 시 뺀다)
        self.offset = offset

# 두 점 사이의 거리 (유클리드 거리 계산식) a² + b² = c²
# 피타고라스 정리에 따라 두 점 사이의 직선거리가 직각삼각형의 빗변이 된다.

    def distance(self):
        dx = self.x2 - self.x1
        dy = self.y2 - self.y1
    # return(dx**2 + dy**2) ** 0.5
        return math.sqrt(dx**2 + dy**2)

# 두 점 사이의 기울기 (y의 변화량 / x의 변화량)
    def slope(self):
        dx = self.x2 - self.x1
        dy = self.y2 - self.y1

        if dx == 0:
            return None

        return dy/dx

    # 수학 및 데이터 분석에서의 로그: 큰수를 작게 압축, 복잡한 연산 단순화, 데이터 정규성 확보 
    def transform(self, x_list:list[float]): # 로그변환
        return [math.log(x + self.offset) for x in x_list]

    def inverse_trans(self, x_list:list[float]): #역변환
        return [math.exp(x_log) - self.offset for x_log in x_list]

# 클래스가 클래스를 지정할 수 있다. has a (포함)관계와 is a (상속)관계가 있다.

def main():
    ctest = CalcTest(1,2,4,6)
    print('거리:', ctest.distance)
    print('거리:', ctest.distance)

    # 로그처리
    data = [10.0, 100.0, 1000.0, 10000.0] # dp:편차가 큰 자료들

    # 로그 변환 및 역변환
    data_log_scaled = ctest.transform(data)
    print('원본 자료:', data)
    print('로그변환 자료:', data_log_scaled)

    reversed_data = ctest.inverse_trans(data_log_scaled)
    reversed_data_round = [round(val, 1) for val in reversed_data] # 반올림
    print('역변환 자료:', reversed_data_round)

if __name__ == '__main__':
    main()


