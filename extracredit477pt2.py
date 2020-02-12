import networkx as nx
import matplotlib.pyplot as plt
from random import sample
#edges = formatEdges("C:\\Users\\Akolam\\Desktop\\DATA\\Edges.csv")
#nodes = formatNodes("C:\\Users\\Akolam\\Desktop\\DATA\\Nodes.csv", edges)
def formatEdges(file):
    edges = []
    f = open(file,'r')
    if f.mode == 'r':
        contents = f.readlines()
    for i in contents:
        comma = i.find(',')
        u = i[0:comma]
        v = i[comma+1:]
        edges.append((u,v))
    del edges[0]
    return edges
        
def formatNodes(file):
    nodes = {}
    f = open(file,'r')
    if f.mode == 'r':
        contents = f.readlines()
    for i in contents:
        comma1 = i.find(',')
        comma2 = i.rfind(',')
        ids = i[0:comma1]
        gender = i[comma1+1:comma2]
        age = i[comma2+1:]
        nodes[ids] = [gender,age[:-1]]
    nodes.pop("ID")
    return nodes

def friends(edges, seed, limit):
    arr = []
    end = limit
    for (u,v) in edges:
        if (u == seed):
            arr.append(v)
        else:
            pass
        
    if (len(arr) < 5):
        return arr
    else:
        zone = sample(arr,5)
        return zone

'''
Add checking to see if adding the entirety of zone would make the sample size of friends added be over 200
'''
    
def main():
    boy = formatEdges("C:\\Users\\Akolam\\Desktop\\DATA\\Edges.csv")
    girl = formatNodes("C:\\Users\\Akolam\\Desktop\\DATA\\Nodes.csv")
    seed = '2150\n'
    times = 200
    data = [seed]
    arrTotalFem = []
    arrTotalMale = []
    arrTotalChild = []
    arrTotalAdult = []
    for i in girl:
        if(girl[i][0] == 'female'):
            arrTotalFem.append(girl[i][0])
        if(girl[i][0] == 'male'):
            arrTotalMale.append(girl[i][0])
        if(girl[i][1] == 'adult'):
            arrTotalAdult.append(girl[i][1])
        if(girl[i][1] == 'childl'):
            arrTotalChild.append(girl[i][1])

    numTotalFem, numTotalMale, numTotalChild, numTotalAdult = len(arrTotalFem), len(arrTotalMale), len(arrTotalChild), len(arrTotalAdult)
    percTotalFem, percTotalMale, percTotalChild, percTotalAdult = format((numTotalFem/3360) * 100, '.2f'), format((numTotalMale/3360) * 100, '.2f'), format((numTotalChild/3360) * 100, '.2f'), format((numTotalAdult/3360) * 100, '.2f')
    print(percTotalFem, percTotalMale, percTotalChild, percTotalAdult)

    counter = 1
    test1 = 0
    test2 = 0
    test3 = 0
    test4 = 0
    test5 = 0
    for i in range(100):
        numFem = 0
        numMale = 0
        numChild = 0
        numAdult = 0
        data = [seed]
        for i in data:
            print(girl[i[:-1]], counter)
        for node in data:
            if (len(data) >= times):
                break
            else:
                number = friends(boy, node[:-1], times)
                if(len(number) + len(data) > 200):
                    check = 200 - len(data)
                    add = sample(number, check)
                    data += add
                    
                else:
                    data += number
                   
        for i in data:
            key = i[:-1]
            x = girl[key]
            numFem += x.count('female')
            numMale += x.count('male')
            numChild += x.count('childl')
            numAdult += x.count('adult')
        percFem, percMale, percChild, percAdult = ((numFem/len(data)) * 100), ((numMale/len(data)) * 100), ((numChild/len(data)) * 100), ((numAdult/len(data)) * 100)            
        test1 += percFem
        test2 += percMale
        test3 += percChild
        test4 += percAdult
        test5 += len(data)
        counter += 1
    finalpercFem = test1 / 100
    finalpercMale = test2 / 100
    finalpercChild = test3 / 100
    finalpercAdult = test4 / 100
    finalnodes = test5/100
    print(finalpercFem, finalpercMale, finalpercChild, finalpercAdult, finalnodes)
    

    
    
    
        
    

    
main()