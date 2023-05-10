
import copy
import sys
import datetime
import numpy as np
from copy import deepcopy

from pandas import DataFrame

start_time = datetime.datetime.now()

def Distance(a,b):
    distance = 0
    for i in range(len(a)):
        distance += (float(a[i]) - float(b[i]))**2
    return round(distance ** 0.5, 3) #소수점 3자리 반올림

def Single_Distance(distance,a,b):
    temp = []
    result = []
    for i in a:
        for j in b:
            temp.append(distance[i][j][1])
    temp.sort()
    return round(temp[0], 3)


def Complete_Distance(distance,a,b):
    temp = []
    for i in a:
        for j in b:
            temp.append(distance[i][j][1])
    temp.sort(reverse=True)
    return round(temp[0], 3)


x = []
data=[]

with open(sys.argv[1],'r') as file:
  for line in file:
       data = line.strip().split('\t')
       x.append(data)

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


#모든 점들 두개씩 거리 재서 distances[] 에 넣음
distance = []
distance_sort = []
for i in range(500):
    temp1 = []
    for j in range(500):
        dis = round(Distance(df[i], df[j]),3)
        temp1.append([j,dis])
    distance.append(temp1)
    distance_sort.append(temp1)


for i in range(500):
    distance_sort[i].sort(key=lambda x: x[1])



#하나의 object로 된 cluster를 만든다.
label_init = []
for i in range(500):
    label_init.append([i])



#2개씩 클러스터
label = []
close = []
close.append(distance_sort[0][1][0])
label.append([0,distance_sort[0][1][0]])
for i in range(1,500):
    temp = []
    temp.append(i)
    count = 1
    stop = 0
    m = distance_sort[i][count][0]
    close.sort()
    j = 0
    while j != len(close):
        if (i == close[j]):
            stop = 1
            break
        elif close[j] == m:
            count += 1
            m = distance_sort[i][count][0]
            j = 0

        else:
            j += 1

    if stop == 0 :
        if distance_sort[i][count][1] <= 5:
            temp.append(distance_sort[i][count][0])
            close.append(i)
            close.append(distance_sort[i][count][0])
            label.append(temp)
        else:
            close.append(i)
            label.append(temp)

#complte_distance에 사용할 리스트 저장
label_c = label

print("\nSingle Distance")
#n개씩 클러스팅(Single_Distance)
label_n = []
out = 1
while out != 0:
    label_n = []
    close = []
    for i in range(len(label)-1):
        temp = []
        count = 0
        stop = 0
        close.sort()
        for j in range(i+1,len(label)):
            dis = Single_Distance(distance, label[i], label[j])
            temp.append([j,dis])
            #print(temp)
            temp.sort(key=lambda x: x[1])
#            print(temp)

        #print(temp)
        m = temp[count][0]
        k = 0
        while k != len(close):
            if (i == close[k]):
                stop = 1
                break
            elif close[k] == m:
                count += 1
                m = temp[count][0]
                k = 0
            else:
                k += 1

        if stop == 0:
            if temp[0][1] <= 5:
                label_n.append(label[i] + label[temp[count][0]])
                close.append(temp[count][0])
                close.append(i)
            else:
                label_n.append(label[i])
                close.append(i)

    co = 1
    for p in close:
        if (len(label)-1) != p:
            co += 1
    if co != len(close):
        close.append(len(label))
        label_n.append(label[len(label)-1])


    if len(label) == len(label_n):
        out = 0
        break
    label = []
    label = copy.deepcopy(label_n)

#print(label_n)

for i in range(len(label_n)):
    print(len(label_n[i]),': ', end= ' ')
    for j in range(len(label_n[i])):
        print(label_n[i][j], end=' ')
    print()

with open('assignment4_output1.txt', 'w') as file:
    for i in range(len(label_n)):
        s = str(len(label_n[i]))
        file.write(s + ': ')
        for j in range(len(label_n[i])):
            s1 = str(label_n[i][j])
            file.writelines(s1 + ' ')
        file.write('\n')
file.close()


#n개씩 클러스팅(Complete_Distance)
label_n = []
out = 1
while out != 0:
    label_n = []
    close = []
    for i in range(len(label_c)-1):
        temp = []
        count = 0
        stop = 0
        close.sort()
        for j in range(i+1,len(label_c)):
            dis = Complete_Distance(distance, label_c[i], label_c[j])
            temp.append([j,dis])
            #print(temp)
            temp.sort(key=lambda x: x[1])
#            print(temp)

        #print(temp)
        m = temp[count][0]
        k = 0
        while k != len(close):
            if (i == close[k]):
                stop = 1
                break
            elif close[k] == m:
                count += 1
                m = temp[count][0]
                k = 0
            else:
                k += 1

        if stop == 0:
            if temp[0][1] <= 5:
                label_n.append(label_c[i] + label_c[temp[count][0]])
                close.append(temp[count][0])
                close.append(i)
            else:
                label_n.append(label_c[i])
                close.append(i)

    co = 1
    for p in close:
        if (len(label_c)-1) != p:
            co += 1
    if co != len(close):
        close.append(len(label_c))
        label_n.append(label_c[len(label_c)-1])

    if len(label_c) == len(label_n):
        out = 0
        break
    label_c = []
    label_c = copy.deepcopy(label_n)




print("\ncomplete Distance")
for i in range(len(label_n)):
    print(len(label_n[i]),': ', end= ' ')
    for j in range(len(label_n[i])):
        print(label_n[i][j], end=' ')
    print()

with open('assignment4_output2.txt', 'w') as file:
    for i in range(len(label_n)):
        s = str(len(label_n[i]))
        file.write(s + ': ')
        for j in range(len(label_n[i])):
            s1 = str(label_n[i][j])
            file.writelines(s1 + ' ')
        file.write('\n')
file.close()

end_time = datetime.datetime.now()
time_diff = (end_time - start_time)
execution_time = time_diff.total_seconds() * 1000

print(execution_time)





