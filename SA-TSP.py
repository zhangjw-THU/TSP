# -*- coding: utf-8 -*-
# 张嘉玮
# 20190503
# TSP:模拟退火算法求解

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 随机产生地图
Nodes = 10
# Nodes_map = np.random.randint(0,100,[2,Nodes])
Nodes_map = np.array([[32,79 ,14 ,17 ,80 ,69 ,52 , 3,87 ,38],
                      [9 ,14, 25 ,17, 51 ,29, 49, 57 ,65 ,72]])
print(Nodes_map)

#距离用邻接矩阵表示
Dis = np.zeros([Nodes,Nodes])
for i in range(Nodes):
    for j in range(i+1,Nodes):
        dis = np.sqrt(pow(Nodes_map[0][i]-Nodes_map[0][j],2)+pow(Nodes_map[1][i]-Nodes_map[1][j],2))
        Dis[i][j] = dis
        Dis[j][i] = dis

print(Dis)

def PlotMap(Path,nodes_map,NUM):
    num = len(Path)
    # plt.figure(NUM)
    for i in range(num):
        id1 = Path[i]
        id2 = Path[(i+1)%num]
        plt.plot([nodes_map[0,id1],nodes_map[0,id2]],[nodes_map[1,id1],nodes_map[1,id2]],'r')

    plt.plot(nodes_map[0, :], nodes_map[1, :], '*b')
    plt.show()


# 初始化路径
Init_Path = np.array(range(Nodes))
np.random.shuffle(Init_Path)


# 计算路长
def PathLngth(Path,DisMap):
    Len = 0
    for i in range(len(Path)):
        node1 = Path[i]
        node2 = Path[(i+1)%len(Path)]
        Len += DisMap[node1][node2]
    return Len

# 交换两个节点
def PathChange(Path):
    Node_id = np.random.randint(0,len(Path),2)
    New_Path = Path.copy()
    temp = New_Path[Node_id[0]]
    New_Path[Node_id[0]] = New_Path[Node_id[1]]
    New_Path[Node_id[1]] = temp
    return New_Path


# 模拟退火优化
T = 1000
min_T = 0.001
Path = Init_Path
r = 0.95
ii=1
PathCost = []
while T>=min_T:
    ii+=1
    if ii%30==0:
        PlotMap(Path, Nodes_map, 10)

    New_Path = PathChange(Path)
    dE = PathLngth(New_Path,Dis)-PathLngth(Path,Dis)

    if dE<=0:
        Path = New_Path.copy()
    else:
        if np.exp(-dE/T) >np.random.rand():
            Path = New_Path.copy()

    T = r*T
    PathCost.append(PathLngth(Path,Dis))
plt.figure(2)
plt.plot(PathCost)
plt.xlabel('Temperature')
plt.ylabel('RoadLength')
plt.show()

print(Nodes_map,Init_Path,Path)
# PlotMap(Init_Path,Nodes_map,10)
PlotMap(Path,Nodes_map,11)
print(round(PathLngth(Path,Dis),5))

