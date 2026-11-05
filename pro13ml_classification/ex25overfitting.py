# 과적합 방지 방법 이해
# train / test split : 일반화 성능 향상
# k-Fold : 안정적 평가
# GridSearchCV : 최적의 하이퍼파라미터 검색

# iris dataset 사용

from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

iris = load_iris()
print(iris.keys())

train_data = iris.data
train_label = iris.target
print(train_data[:3])
print(train_label[:3])

# 분류모델 
df_clf = DecisionTreeClassifier()
df_clf.fit(train_data, train_label)
pred = df_clf.predict(train_data) # 학습 데이터로 검증
print('예측값 :', pred)
print('실제값 :', train_label)
print('분류 정확도 :', accuracy_score(train_label,pred)) # 1.0 과적합 의심

print('\n 과적합 방지 목적 처음 1 : train / test split')
from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(
    iris.data, iris.target, test_size=0.3, random_state=12
)
df_clf.fit(x_train, y_train)   # train data로 학습
pred2 = df_clf.predict(x_test) # test data로 학습
print('예측값 :', pred2)
print('실제값 :', y_test)
print('분류 정확도(split) :', accuracy_score(y_test, pred2)) # 0.9777777777777777

print('\n과적합방지 목적 처리2 : 교차검증(k-fold cross validation)')
# K-폴드 교차 검증(K-fold cross validation)은 머신러닝 모델의 일반화 성능을 객관적으로 평가하기 위해 
# 데이터를 K개의 부분집합(폴드, Fold)으로 나누어 학습과 검증을 반복하는 방법
# train dataset = train + validation dataset으로 나누어 모델을 학습

from sklearn.model_selection import KFold
import numpy as np

features = iris.data
label = iris.target
df_clf2 = DecisionTreeClassifier(criterion='gini', max_depth=3, random_state=12)

Kfold = KFold(n_splits=5) # k:5회 접기
cv_acc = [] # 각 1회 마다 정확도 저장용
print('irsis shape :', features.shape) # (150, 4)
# KFold 학습 시 전체 150행이 학습데이터(4/5, 120개), 검증데이터(1/5, 30개)로 검증데이터로 학습을 한다.

n_iter = 0

for train_index, test_index in Kfold.split(features): 
    print('n_iter(반복수):', n_iter)
    print('train_index:', train_index)
    print('test_index:', test_index)
    n_iter += 1
