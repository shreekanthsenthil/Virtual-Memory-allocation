import random
from random import choice,shuffle,randint
import collections
def second(a):
    return a[1]
vm = []
n = 20
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
l=[]
for i in range(0,10):
    w.append([randomgen()])
    w[i].append(fitness(w[i][0]))
    l.append(w[i][1])

for i in range(10):
    w[i].append([])

def relation(w2):
    w2.sort(reverse=True,key=second)
    sea=w2[0]
    rivers=w2[1:4]
    streams=w2[4:10]
    '''for i in range(len(rivers)):
        rivers[i][2]=sea[0]'''
    for i in range(len(streams)):
        temp=choice(rivers)
        streams[i][2]=rivers.index(temp)
    #streams[-1][2]=-999
    return sea,rivers,streams

def willfit(a,index,new):
    server=[]
    for i in range(0,n):
        server.append([90,90])
    for i in range(0,n):
        for j in range(0,n):
            if(a[j] == i):
                server[i][0] -= vm[j][0]
                server[i][1] -= vm[j][1]
    if(server[new][0] >= vm[index][0] and server[new][1] >= vm[index][1]):
        return True
    else :
        return False


sea,rivers,streams=relation(w)
t=10
for _ in range(t):
    for j in range(len(rivers)):
        bfitindex = 999
        bfit = 0
        for k in range(len(streams)):
            if(streams[k][2] == j):
                l=[]
                for i in range(n):
                    if(streams[k][0][i]!=rivers[j][0][i]):
                        l.append(i)
                q=True
                count = 0
                fail = 0
                while(q == True):

                    c=choice(l)
                    if(willfit(streams[k][0],c,rivers[j][0][c])):
                        streams[k][0][c]=rivers[j][0][c]
                        count +=1
                    else:
                        fail +=1
                    if(count==2 or fail == 20):
                        q=False
                fit = fitness(streams[k][0])
                streams[k][1] = fit
                if(fit > bfit):
                    bfitindex = k
                    bfit = fit
        if(bfit > rivers[j][1]):
            rivers[j][0],streams[bfitindex][0] = streams[bfitindex][0],rivers[j][0]
            rivers[j][1], streams[bfitindex][1] = streams[bfitindex][1], rivers[j][1]

    bfitindex = 999
    bfit = 0
    for j in range(len(rivers)):
        l=[]
        for i in range(n):
            if(sea[0][i] != rivers[j][0][i]):
                l.append(i)
        a = True
        count = 0
        fail = 0
        while (a == True):

            c = choice(l)
            if (willfit(rivers[j][0], c, sea[0][c])):
                rivers[j][0][c] = sea[0][c]
                count += 1
            else :
                fail +=1
            if (count == 2 or fail ==20):
                a = False

        fit = fitness(rivers[j][0])
        rivers[j][1] = fit
        if (fit > bfit):
            bfitindex = j
            bfit = fit
    if (bfit > sea[1]):
        sea[0], rivers[bfitindex][0] = rivers[bfitindex][0], sea[0]
        sea[1], rivers[bfitindex][1] = rivers[bfitindex][1], sea[1]


print("VMs in Server : " , sea[0])
server=[]
notused=[]
for i in range(0,n):
    if(i in sea[0]):
        server.append(i)
    else :
        notused.append(i)
print("Servers used : ",server)
print("Servers not used : ",notused)