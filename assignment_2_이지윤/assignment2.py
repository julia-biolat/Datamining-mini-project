# 이지윤_2021247052_디지털헬스케어학부_데이터마이닝

import numpy as np
from copy import deepcopy

import sys


distances=[]

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

#각 데이터 그룹화 0~10개로
labels = np.zeros(len(x))

#50개씩 나누기
while(n+50<=500):
    for j in range(12):
        total = 0
        for i in range(n,n+50):
            total = total + float(x[i][j])
        temp.append(round(total / 50.0, 3)) #평균 소수점 3자리 반올림
    mean.append(temp)
    n = n + 50
    temp = []

m = 0
k = 0
#label 50개씩 차례대로 0~9넣음
for k in range(10):
    for i in range(50*k, 50*(k+1)):
        labels[i] = k

for i in range(len(x)):
    distances = np.zeros(10)
    for j in range(10):
        distances[j] = Distance(mean[j], x[i])
    cluster = np.argmin(distances)
    labels[i] = cluster

x1 = np.array(x)
df = np.zeros(x1.shape)
for i in range(500):
    for j in range (12):
        df[i][j] = float(x[i][j])


mean_old = deepcopy(mean)
for i in range(10):
  points = [df[j][0:12] for j in range(len(x)) if labels[j] == i]
  mean[i] = np.mean(points, axis=0)


gap = np.zeros(10)
mean1 = np.array(mean)
mean_old = np.zeros(mean1.shape)

for i in range(10):
    gap[i] = Distance(mean[i], mean_old[i])


#gap가 0일때까지
while gap.all() != 0:

    for i in range(500):
        distances = np.zeros(10)

        for j in range(10):
            distances[j] = Distance(mean[j][0:12], df[i][0:12])
        cluster = np.argmin(distances)
        labels[i] = cluster

    mean_old = deepcopy(mean)
    for i in range(10):
        points = [df[j][0:12] for j in range(len(x)) if labels[j] == i]
        mean[i] = np.mean(points, axis=0)


    for i in range(10):
        gap[i] = Distance(mean_old[i] , mean[i])


result = []
n = 0
for i in range(10):
    temp1 = []
    for j in range(500):
        if labels[j] == i:
            n += 1
            temp1.append((j))
    result.append(temp1)

for i in range(10):
    print(len(result[i]),': ', end= ' ')
    for j in range(len(result[i])):
        print(result[i][j], end=' ')
    print()

with open('assignment2_output.txt', 'w') as file:
    for i in range(10):
        s = str(len(result[i]))
        file.write(s + ': ')
        for j in range(len(result[i])):
            s1 = str(result[i][j])
            file.writelines(s1 + ' ')
        file.write('\n')
file.close()