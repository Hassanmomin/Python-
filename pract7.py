from heapq import heappush,heappop
graph={
    "Arad" : [("sibies",140),("zerind",78),("timisoara",118)],
    "zerind" : [("Arad",75),("oradea",71)],
    "oradea" : [("zerind",71),("sibies",151)],
    "timisoara" : [("Arad",118),("lugoj",111)],
    "lugoj" : [("timisoara",111),("mehadia",70)],
    "mehadia" : [("lugoj",70),("drobeta",75)],
    "drobeta" : [("mehadia",75),("craiora",120)],
    "craiora" : [("drobeta",120),("pitesi",138)],
    "sibies" : [("Arad",140),("fagaras",99)],
    "fagaras" : [("sibies",99),("bucharset",211)],
    "pitesi" : [("Eraiova",128),("bucharset",111)],
    "bucharset" : []
    }

heuristic = {
    "Arad":366,"zerind":374,"oradea":380,
    "timisoara":329,"lugoj":244,"mehadia":241,
    "drobeta":242,"craiora":160,"sibies":253,
    "rimnicu":193,"fagaras":176,"pitesi":100,
    "bucharset":0
    }


def astar(start,goal):
    pq=[]
    heappush(pq,(heuristic[start],0,start,[start]))
    visited=set()
    while pq:
        f,g,city,path = heappop(pq)
        if city == goal:
            return path,g
        if city in visited:
            continue
        visited.add(city)
        for neighbor,cost in graph[city]:
            if neighbor not in visited:
                new_g = g + cost
                new_f = new_g + heuristic[neighbor]
                heappush(pq,(new_f,new_g,neighbor,path+[neighbor]))
    return None ,float("inf")


path,cost = astar("Arad","bucharset")
print("shortest path:")
for city in path:
    print(city)
print("total cost:",cost)




























