#2021247052 이지윤 디지털헬스케어학부

import numpy as np
from copy import deepcopy, copy
import sys

def FindCluster(cluster,key):
    new = list()
    old = cluster

    for i in range(len(key)):
        set1=set()
        set2 = set()
        j=0
        while j < len(old):
            if key[i] in old[j]:
                set1.update(old[j])
                del old[j]
                j=j-1
            j=j+1
        if len(set1)!=0:
            new.append(set1)
        j=0
        while j < len(new):
            if key[i] in new[j]:
                set2.update(new[j])
                del new[j]
                j = j-1
            j = j+1
        new.append(set2)

    cluster=[]
    for i in range(len(new)):
        if(len(list(new[i]))>1):
            cluster.append(list(new[i]))
    return cluster

# graph 가 disconnect인지 connect인지 판단
def FindValue(k, closed, store):
    t = []
    t = list(graph.get(k))
    store.add(k)
    closed.add(k)
    #print(set(t))
    store.update(graph.get(k))
    #print(store)
    for i in range(len(t)):
        if t[i] in closed:
            return
        else:
            FindValue(t[i], closed, store)
    return store, closed

graph = dict()
with open('assignment5_input.txt','r') as file:
    for line in file:
        n1, n2 = line.strip().split('\t')
        try:
            graph[n1].add(n2)
        except KeyError:
            graph[n1] = {n2}
        try:
            graph[n2].add(n1)
        except KeyError:
            graph[n2] = {n1}



# key, value 값 list로 저장
key = list(graph)
value = []
for k in key:
    value.append(list(graph.get(k)))


#disconnect 이기 때문에 cluster에 저장
closed = set()
cluster = []
for i in range(len(key)):
    store = set()
    if key[i] not in closed:
        FindValue(key[i],closed, store)
        closed.update(store)
        cluster.append(list(store))
        #print(closed)


#print(cluster)


#threshold가 0.4 이하면, cluster 끝 아니면 돌리기
cluster_n = []
cluster_g = []
for i in range(len(cluster)):
    temp = 0
    density = 0
    for j in range(len(cluster[i])):
        temp += len(graph.get(cluster[i][j]))/2
    density = (temp / ((len(cluster[i]) * (len(cluster[i])-1))/2))
    #print(density)
    if density < 0.4:
        cluster_g.append(cluster[i])
    else:
        cluster_n.append(cluster[i])




#cluster_g에서 남은것들만 있는 key, value 설정하기
value = []
key = []
for i in range(len(cluster_g)):
    for j in range(len(cluster_g[i])):
        key.append(cluster_g[i][j])
        value.append(list(graph.get(cluster_g[i][j])))

# print(value)
jaccard = []
for i in range(len(key)):
    for j in range(len(key)):
        if i == j:
            continue
        if key[i] in value[j] and key[j] in value[i]:
            jaccard.append([len(set(value[i]).intersection(set(value[j]))) / len(set(value[i]).union(set(value[j]))),
                            key[i], i, key[j], j])
t = 0
while t < 3:
    n = 0
    jaccard.sort(key=lambda x: (-x[0], x[1], x[3]), reverse=True)
    for i in value[jaccard[n][4]]:
        if jaccard[n][1] in i:
            value[jaccard[n][4]].remove(jaccard[n][1])

    for j in value[jaccard[n][2]]:
        if jaccard[n][3] in j:
            value[jaccard[n][2]].remove(jaccard[n][3])



    cluster = []
    for i in range(len(key)):
        tem = set()
        tem.add(key[i])
        tem.update(value[i])
        cluster.append(list(tem))

    cluster = FindCluster(cluster, key)
    t +=1

cluster_n.append(cluster[0])

cluster_n.sort(key = len)

for i in range(len(cluster_n)):
    print(len(cluster_n[i]),': ', end= ' ')
    for j in range(len(cluster_n[i])):
        print(cluster_n[i][j], end=' ')
    print()

with open('assignment6_output.txt', 'w') as file:
    for i in range(len(cluster_n)):
        s = str(len(cluster_n[i]))
        file.write(s + ': ')
        for j in range(len(cluster_n[i])):
            s1 = str(cluster_n[i][j])
            file.writelines(s1 + ' ')
        file.write('\n')
file.close()


'''
count = 0
jaccard = []
for i in range(len(cluster_g)):
    temp = []
    check = set()
    for j in range(len(cluster_g[i])):
        v = list(graph.get(cluster_g[i][j]))
        for v in range(len(v)):
            a = cluster[i][j]
            if a < v[i]:
                temp.append([len(a.intersection(v[i])) / len(a.union(v[i])), a, v[i]])
            else:
                temp.append([len(a.intersection(v[i])) / len(a.union(v[i])), v[i], a])
            jaccard.append(temp)

        for k in range(len(cluster_g[i])):
            if j == k:
                continue
            else:
                a = set(graph.get(cluster_g[i][j]))
                b = set(graph.get(cluster_g[i][k]))
                if cluster_g[i][j] < cluster_g[i][k]:
                    temp.append([len(a.intersection(b)) / (len(a) + len(b)), cluster_g[i][j], cluster_g[i][k]])
                else:
                    temp.append([len(a.intersection(b)) / (len(a) + len(b)), cluster_g[i][k], cluster_g[i][j]])
                jaccard.append(temp)

for i in range(len(jaccard)):
    jaccard[i].sort(key=lambda x: (-x[0], x[1]), reverse=True)
    graph[jaccard[i][0][1]].remove(jaccard[i][0][2])
    graph[jaccard[i][0][2]].remove(jaccard[i][0][1])

cluster = FindValue(key, cluster_g)

# threshold가 0.4 이하면, cluster 끝 아니면 돌리기
cluster_n = []
cluster_g = []
for i in range(len(cluster)):
    temp = 0
    density = 0
    for j in range(len(cluster[i])):
        temp += len(graph.get(cluster[i][j])) / 2
    density = (temp / ((len(cluster[i]) * (len(cluster[i]) - 1)) / 2))
    # print(density)
    if density < 0.4:
        cluster_g.append(cluster[i])
    else:
        cluster_n.append(cluster[i])
print(cluster_g)


while len(cluster_g) != 0:
    # cluster 다시 돌려야할것들 cluster 마다 jaccard 구함 [숫자, 문자]
    jaccard = []
    for i in range(len(cluster_g)):
        temp = []
        for j in range(len(cluster_g[i])):
            for k in range(len(cluster_g[i])):
                if j == k:
                    continue
                else:
                    a = set(graph.get(cluster_g[i][j]))
                    b = set(graph.get(cluster_g[i][k]))
                    if cluster_g[i][j] < cluster_g[i][k]:
                        temp.append([len(a.intersection(b)) / (len(a) + len(b)), cluster_g[i][j], cluster_g[i][k]])
                    else:
                        temp.append([len(a.intersection(b)) / (len(a) + len(b)), cluster_g[i][k], cluster_g[i][j]])
                    jaccard.append(temp)


    for i in range(len(jaccard)):
        jaccard[i].sort(key=lambda x: (-x[0], x[1], x[2]), reverse=True)
        graph[jaccard[i][0][1]].remove(jaccard[i][0][2])
        graph[jaccard[i][0][2]].remove(jaccard[i][0][1])

    cluster = FindValue(key, cluster_g)

    #threshold가 0.4 이하면, cluster 끝 아니면 돌리기
    cluster_n = []
    cluster_g = []
    for i in range(len(cluster)):
        temp = 0
        density = 0
        for j in range(len(cluster[i])):
            temp += len(graph.get(cluster[i][j]))/2
        density = (temp / ((len(cluster[i]) * (len(cluster[i])-1))/2))
        #print(density)
        if density < 0.4:
            cluster_g.append(cluster[i])
        else:
            cluster_n.append(cluster[i])
    print(cluster_g)

'''

