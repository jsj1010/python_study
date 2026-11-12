# DBSCAN (노이즈가 포함된 응용의 밀도 기반 공간 클러스터링).
# k-means와 같은 전통적인 클러스터링 방법과 달리, DBSCAN은 클러스터 수를
# 미리 지정할 필요가 없으며, 불규칙한 형태와 다양한 밀도를 가진 데이터셋에
# 특히 적합하다.
# DBSCAN은 밀도가 다양하거나 모양이 불규칙한 클러스터가 있는 데이터와 같이 모양이
# 잘 정의되지 않고 이상치가 많은 데이터를 처리 할때 유용하게 사용 가능하다.'

import matplotlib.pyplot as plt
from matplotlib import style
from sklearn.datasets import make_moons
from sklearn.cluster import DBSCAN, KMeans


# data 생성
x, y = make_moons(n_samples=200, noise=0.05, shuffle=True, random_state=0)
print(x[:5], x.shape)
plt.scatter(x[:, 0], x[:, 1], c=y)
plt.show()

print('KMeans로 군집화')
km = kMeans(n_clusters=2, init='random', random_state=0)
pred1 = km.fit_predict(x)
print('km 예측 군집 id:', pred1[:10])

# km 시각화
def plotresult(x, pred, title):
    plt.scatter(x[pred == 0, 0], x[pred == 0, 1], c='blue', marker='o', s=40, label='cluster')
    plt.scatter(x[pred == 1, 0], x[pred == 1, 1], c='red', marker='s', s=40, label='cluster')
    plt.scatter(km.cluster_centers_[:, 0], km.cluster_centers_[:, 1], \
                c='black', marker='+', s=100, label='centroid')
    plt.title(title)
    plt.show()

plotresult(x, pred1)
dbs = DBSCAN(eps=0.2, min_samples=5, metric='euclidean')
# eps : 샘플 간 최대거리, min_samples : 점에 대한 이웃 샘플 수 (반경 포인트들의 최소 갯수)
pred2 = dbs.fit_predict(x)
print('DBSCAN 군집 id:', pred2[:10])
print('군집 종류:', set(pred2))

plotresult(x, pred2) # 분류가 제대로 됨. 모양에 따라 군집 생성
# Kmeans는 k개에 군집의 갯수를 맞추고, DBSCAN은 데이터의 밀도에 의해 군집형태를 구성함.