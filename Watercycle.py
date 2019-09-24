import random
from random import choice,shuffle,randint
import collections
def second(a):
    return a[1]
vm = []
n = 10
rp = 25
rm = 25
p=0.25
pmax = 4932
e=random.random()
for i in range(0,n):
    rpi=random.randint(0,2*rp)
    rmi=random.randint(0,rm)
    r=random.random()
    if((r < (p**rpi) <=rp) or (r >= (p**rpi) < rp)):
        rmi = rmi + rm
    vm.append([rpi,rmi])

def randomgen():
    raindrop = []
    server=[]
    for i in range(0,n):
        server.append([90,90])
    for i in range(0,n):
        a=True
        while(a==True):
            s=random.randint(0,n-1)
            if(vm[i][0] <= server[s][0] and vm[i][1] <= server[s][1]):
                a=False
                raindrop.append(s)
                server[s][0] -= vm[i][0]
                server[s][1] -= vm[i][1]
    return raindrop

def fitness(r):
    server = []
    for i in range(0, n):
        server.append([0,0])
    for i in range(0,n):
        for j in range(0,n):
            if(r[j] == i):
                server[i][0] += vm[j][0]
                server[i][1] += vm[j][1]
    P=[]
    W=[]
    for i in range(0,n):
        if(server[i] == [0,0]):
            P.append(0)
            W.append(0)
        else :
            pj = 53 * server[i][0] + 162
            wj = (abs(( 90 - server[i][0] )-(90 - server[i][1]))+e)/(server[i][0]+server[i][1])
            P.append(pj)
            W.append(wj)

    for i in range(0,n):
        P[i] = P[i]/pmax
    fit = 1/(e+sum(P)) + 1/(e+sum(W))
    return fit


w=[]
for i in range(0,10):
    w.append([randomgen()])
    w[i].append(fitness(w[i][0]))

for i in range(n):
    w[i].append([])

def relation(w2):
    w2.sort(reverse=True,key=second)
    sea=w2[0]
    rivers=w2[1:4]
    streams=w2[4:10]
    for i in range(len(rivers)):
        rivers[i][2]=sea[0]
    for i in range(len(streams)):
        temp=choice(rivers)
        streams[i][2]=temp[0]
    return sea,rivers,streams
sea,rivers,streams=relation(w)
print(sea)
print(rivers[0])
print(streams)

