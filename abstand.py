#! /usr/bin/env python3
from collections import deque


def abstand(s,t, dateiname="labyrinth.dat"):
    """
    
    @param:
    @param:
    @param:
    @return: 
    """

    
    #Fetch maze
    Laby = list()
    file_in = open(dateiname, 'r')
    

    for line in file_in:
        if line!="":
            Laby.append(list(line.strip()))

        
    #Check anomalities
    if Laby == []:
        #print('leer')
        return -1

    for line in Laby:
        #if len(line) * len(Laby) > 999:
        #        return -1
        for anotherline in Laby:
            if len(line) != len(anotherline):
                #print('laenge')
                return -1
    

    if Laby[s[0]][s[1]] == 'U' or Laby[t[0]][t[1]] == 'U':
        return -1

    if s[0]<0 or s[1]<0 or t[0]<0 or t[1]<0 or s[0]>len(Laby) or s[1]>len(Laby[0]) or t[0]>len(Laby) or t[1]>len(Laby[0]):
        return -1
    
    for line in Laby:
        for pos in line:
            if pos != 'U' and pos != 'P':
                #print('pos')
                return -1

    nurP = True
    for line in Laby:
        for pos in line:
            if pos != 'P':
                nurP = False
    if nurP:
        return abs(s[0]-t[0]) + abs(s[1] - t[1])


    #Find the SHORTEST path
    weglaenge = breitensuche(Laby,s,t)
    
    if weglaenge != 0:
        return weglaenge

    return -1


def breitensuche(Laby,s,t):
    Q = deque([(s,0)])

    Laby[s[0]][s[1]] == 'U'

    while Q:
        v,dist = Q.popleft()
        if v == t:
            return dist

        #for k,l in [()]
        
        if v[0] > 0 and Laby[v[0]-1][v[1]] == 'P':
            Laby[v[0]-1][v[1]] = 'U'
            oben = (v[0]-1,v[1])
            Q.append((oben,dist+1))  

        if v[0] < len(Laby)-1 and Laby[v[0]+1][v[1]] == 'P':
            Laby[v[0]+1][v[1]] = 'U'
            unten = (v[0]+1,v[1])
            Q.append((unten,dist+1))

        if v[1] > 0 and Laby[v[0]][v[1]-1] == 'P':
            Laby[v[0]][v[1]-1] = 'U'
            links = (v[0],v[1]-1)
            Q.append((links,dist+1))

        if v[1] < len(Laby[s[0]])-1 and Laby[v[0]][v[1]+1] == 'P':
            Laby[v[0]][v[1]+1] = 'U'
            rechts = (v[0],v[1]+1)
            Q.append((rechts,dist+1))

    return -1