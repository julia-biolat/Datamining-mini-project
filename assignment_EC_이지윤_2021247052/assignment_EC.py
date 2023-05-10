#2021247052 이지윤 디지털헬스케어학부

import numpy as np
from copy import deepcopy
import sys


def JaccardSimilarity(inp1, inp2):
    union = 0
    inter = 0
    for i in range(517):
        mom = set(inp1[i]).union(set(inp2[i]))
        son = set(inp1[i]).intersection(set(inp2[i]))
        union += len(mom)
        inter += len(son)
    return inter/union


x = []
x2 = []
x3 = []
x4_1 =[]
x4_2 = []
data = []
data_t=[]
true_label = []
with open(sys.argv[1],'r') as file:
    for line in file:
        list = line.strip().split('\t')
        data_t.append(list)
data = []
for i in range(len(data_t)):
    x.append(data_t[i][1])


for i in range(10):
    temp = []
    for j in range(len(x)):
        if int(x[j])-1 == i:
            temp.append(j)
    true_label.append(temp)

outline = []
for j in range(len(x)):
    if x[j]== "-1":
        outline.append(j)

true_link = np.zeros((517, 517))
for i in range(len(true_label)):
    for j in range(len(true_label[i])):
        for k in range(i+1,len(true_label[i])):
            true_link[true_label[i][j]][true_label[i][k]] = '1'


data = []
data_t=[]
list = []
with open(sys.argv[2],'r') as file:
  for line in file:
       list = line.strip().split(' ')
       data_t.append(list)

for i in range(len(data_t)):
    temp = []
    for j in range(0, len(data_t[i])):
        temp.append(data_t[i][j])
    x2.append(temp)


mask_link = np.zeros((517, 517))
for i in range(len(x2)):
    for j in range(len(x2[i])):
        for k in range(i+1,len(x2[i])):
            mask_link[int(x2[i][j])][int(x2[i][k])] = '1'


result = JaccardSimilarity(true_link, mask_link)

print(result)

f = open('assignment_EC_output.txt', 'w')
Str = str(result)
f.write(Str)
f.close()

'''
data = []
data_t=[]
list = []
with open('assignment3_EC_output.txt','r') as file:
  for line in file:
       list = line.strip().split(' ')
       data_t.append(list)


  for i in range(len(data_t)):
      temp = []
      for j in range(len(data_t[i])):
          temp.append(data_t[i][j])
      x3.append(temp)
  print(x3)

mask_link = np.zeros((517, 517))
for i in range(len(x3)):
    for j in range(len(x3[i])):
        for k in range(i+1,len(x3[i])):
            mask_link[int(x3[i][j])][int(x3[i][k])] = '1'
print(mask_link)

print("assign3")
result = JaccardSimilarity(true_link, mask_link)

print(result)

data = []
data_t=[]
list = []
with open('assignment4_EC_output1.txt','r') as file:
  for line in file:
       list = line.strip().split(' ')
       data_t.append(list)

  for i in range(len(data_t)):
      temp = []
      for j in range(len(data_t[i])):
          temp.append(data_t[i][j])
      x4_1.append(temp)
  print(x4_1)

mask_link = np.zeros((517, 517))
for i in range(len(x4_1)):
    for j in range(len(x4_1[i])):
        for k in range(i+1,len(x4_1[i])):
            mask_link[int(x4_1[i][j])][int(x4_1[i][k])] = '1'
print(mask_link)

print("assign4_1")
result = JaccardSimilarity(true_link, mask_link)

print(result)

data = []
data_t=[]
list = []
with open('assignment4_EC_output2.txt','r') as file:
  for line in file:
       list = line.strip().split(' ')
       data_t.append(list)

  for i in range(len(data_t)):
      temp = []
      for j in range(len(data_t[i])):
          temp.append(data_t[i][j])
      x4_2.append(temp)
  print(x4_2)

mask_link = np.zeros((517, 517))
for i in range(len(x4_1)):
    for j in range(len(x4_2[i])):
        for k in range(i+1,len(x4_2[i])):
            mask_link[int(x4_2[i][j])][int(x4_2[i][k])] = '1'
print(mask_link)

print("assign4_2")
result = JaccardSimilarity(true_link, mask_link)

print(result)
'''

