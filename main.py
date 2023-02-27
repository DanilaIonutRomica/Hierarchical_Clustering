import math
import numpy as np
import matplotlib.pyplot as plt
import random

def calculate_distance(pointA,pointB):
    sum=0
    for i in range(0,len(pointA)):
        sum+=(pointA[i]-pointB[i]) **2
    return math.sqrt(sum)

def set_new_cluster(clusters):
    index_new_cluster=-10
    other_index=-10
    minm=1000000
    for i in range(0,len(clusters)):
        for ii in range(0,len(clusters)):
            for j in range(0,len(clusters[i])):
                for jj in range(0,len(clusters[ii])):
                    if calculate_distance(clusters[ii][jj],clusters[i][j]) < minm and i != ii and minm!=0:
                        if clusters[ii][jj]==clusters[i][j]:
                            pass
                        else:
                            minm=calculate_distance(clusters[ii][jj],clusters[i][j])
                            index_new_cluster=ii
                            other_index=i
    new_cluster=[]
    for i in range(0,len(clusters)):
        if i == min(other_index,index_new_cluster):
            other_list=[]
            for elem in clusters[index_new_cluster]:
                other_list.append(elem)
            for elem in clusters[other_index]:
                other_list.append(elem)
            new_cluster.append(other_list)
            # clusters.remove(clusters[other_index])
            # clusters.remove(clusters[index_new_cluster])
        else:
            if i == other_index or i == index_new_cluster:
                pass
            else:
                new_cluster.append(clusters[i])
    return new_cluster
    
points=[]
for i in range(0,10):
    x=random.randint(0,100)
    y=random.randint(0,100)
    points.append([x,y])
  
clusters=[]  
for elem in points:
    clusters.append([elem])


newc=clusters
print(newc)

for i in range(0, len(clusters) -1):
    newc=set_new_cluster(newc)
    x=[]
    y=[]
    xx=[]
    yy=[]
    for elem in newc:
        #plt.plot(elem,'o',color='black')
        print(elem)
        x.append(elem[0][0])
        y.append(elem[0][1])
        if len(elem) >1:
            for e in elem:
                xx.append(e[0])
                yy.append(e[1])
    plt.plot(x,y,'o',color='black')
    plt.plot(xx,yy,'o',color='red')
    plt.show()
    print(newc)