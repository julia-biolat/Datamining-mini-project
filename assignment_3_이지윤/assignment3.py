# 이지윤_2021247052_디지털헬스케어학부_데이터마이닝

import numpy as np
from copy import deepcopy

import sys



def Distance(a,b):
    distance = 0
    for i in range(len(a)):
        distance += (float(a[i]) - float(b[i]))**2
    return round(distance ** 0.5, 3) #소수점 3자리 반올림



x = []
data=[]
with open(sys.argv[1],'r') as file:
  for line in file:
       data = line.strip().split('\t')
       x.append(data)
n = 0
i = 0
j = 0
total = 0
mean = []
temp = []
df = []
'''
with open('assignment2_input.txt','r') as file:
  for line in file:
       data = line.strip().split('\t')
       x.append(data)
'''
#input.txt string에서 float으로 바꿈
x1 = np.array(x)
df = np.zeros(x1.shape)
for i in range(500):
    for j in range (12):
        df[i][j] = float(x[i][j])


#모든 점들 두개씩 거리 재서 distances와[500] distances_temp[500]에 넣음
dis_temp = []
distance_sum = []
distance = np.zeros([500,500]) #두개의 사이 거리 저장
for i in range(500):
    total = 0
    for j in range(500):
        distance[i][j] = Distance(df[i], df[j])
        total += distance[i][j]
    distance_sum.append(round(total,3)) #distances값을 소수점 3로 제한
    dis_temp.append(total)


#거리합 가장 작은 10개의 점 좌표, 인덱스 추출
min_index = []
cluster_sum = []
min_point = np.zeros([10,12])
for i in range(10):
    s_index = dis_temp.index(min(dis_temp))
    min_index.append(s_index)
    cluster_sum.append(round(min(dis_temp),3))
    for j in range(12):
        min_point[i][j] = df[s_index][j]
    dis_temp[s_index] = 1000000


#초기 군집 설정
label = []
for i in range(500):
    temp = []
    for j in min_index:
        temp.append(distance[i][j])
    label.append(temp.index(min(temp)))


cluster = []
for i in range(10):
    point = []
    for j in range(500):
        if label[j] == i:
            point.append(j)
    cluster.append(point)


#Updata medoids
#각 군집에 대해 각 개체의 군집 내에서 거리 합계를 계산하고 거리 합계가 가장 작은 새 중위수를 선택
while True:
    cluster_sum_old = []
    cluster_sum_old = deepcopy(cluster_sum)
    cluster_sum = []
    min_index1 = []
    for i in range(10):
        point1 = []
        for j in cluster[i]:
            total = 0
            for k in cluster[i]:
                total += distance[j][k]
            point1.append(round(total,3))
        min_index1.append(cluster[i][point1.index(min(point1))])
        cluster_sum.append(min(point1))


    #군집 설정
    label = []
    for i in range(500):
        temp = []
        for j in min_index1:
            temp.append(distance[i][j])
        label.append(temp.index(min(temp)))

    #Updata medoids
    cluster = []
    for i in range(10):
        point = []
        for j in range(500):
            if label[j] == i:
                point.append(j)
        cluster.append(point)

    #계속 할지 안할지
    count = 0
    for i in range(10):
        if cluster_sum_old[i] <= cluster_sum[i]:
            count += 1

    if count == 10:
        break


for i in range(10):
    print(len(cluster[i]),': ', end= ' ')
    for j in range(len(cluster[i])):
        print(cluster[i][j], end=' ')
    print()

with open('assignment3_output.txt', 'w') as file:
    for i in range(10):
        s = str(len(cluster[i]))
        file.write(s + ': ')
        for j in range(len(cluster[i])):
            s1 = str(cluster[i][j])
            file.writelines(s1 + ' ')
        file.write('\n')
file.close()