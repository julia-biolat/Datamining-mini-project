
import numpy as np
from copy import deepcopy, copy
import sys

graph = dict()
with open(sys.argv[1],'r') as file:
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


# 1-1 Find all cliques of size-2.
j = 0
cluster_i = []
close = set()
for j in range(len(key)):
    close.add(key[j])
    for i in range(len(value[j])):
        if value[j][i] not in close:
            temp = [key[j],value[j][i]]
            temp.sort()
            cluster_i.append(temp)


'''
df1 = [i for i in cluster_i[6] if i not in cluster_i[2]]
df2 = [i for i in cluster_i[2] if i not in cluster_i[6]]
print(df1)
print(df2)
print(list(graph.get(df1[0])))

if df2[0] in list(graph.get(df1[0])):
    print(df1[0])


'''
answer = []
while True :
    cluster = []
    for i in range(len(cluster_i)):
        for j in range(len(cluster_i)):
            if i >= j:
                continue
            temp = []
            df1 = [a for a in cluster_i[j] if a not in cluster_i[i]]
            df2 = [a for a in cluster_i[i] if a not in cluster_i[j]]
            if df1 == df2:
                continue
            #중복되지 않은 것들
            if df2[0] in list(graph.get(df1[0])) and len(df1) == 1 and len(df2) == 1:
                temp = list(set(cluster_i[i]+cluster_i[j]))
                temp.sort()
                if temp not in cluster:
                    cluster.append(temp)

    if len(cluster) == 0:
        break

    if len(cluster[1]) >= 8:
        answer.append(cluster)

    if len(cluster) == len(cluster_i):
        break
    cluster_i = []
    cluster_i = cluster
    #print("\n")
    #print(cluster_i)


for i in range(len(answer)):
    for j in range(len(answer[i])):
        print(len(answer[i][j]), ': ', end=' ')
        for k in range(len(answer[i][j])):
            print(answer[i][j][k], end=' ')
        print()

with open('assignment5_output.txt', 'w') as file:
    for i in range(len(answer)):
        for j in range(len(answer[i])):
            s = str(len(answer[i][j]))
            file.write(s + ': ')
            for k in range(len(answer[i][j])):
                s1 = str(answer[i][j][k])
                file.writelines(s1 + ' ')
            file.write('\n')
file.close()
