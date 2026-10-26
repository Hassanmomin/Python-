import heapq

graph = {
    "arad" : [("sibies",140),("zerind",78),("timisoara",118)],
    "zerind" : [("arad",75),("oradea",71)],
    "oradea" : [("zerind",71),("sibies",151)],
    "timisoara" : [("arad",118),("lugoj",111)],
    "lugoj" : [("timisoara",111),("mehadia",70)],
    "drobeta" : [("mehadia",75),("craiora",120)],
    "mehadia" : [("lugoj",70),("drobeta",75)],
    "craiora" : [("drobeta",120),("pitesi",138)],
    "sibies" : [("arad",140),("fagaras",99)],
    "fagaras" : [("sibies",99),("buchaslest",211)],
    "pitesi" : [("erapova",128),("buchaslest",101)],
    "buchaslest" : []
    }
def ucs(start,goal):
    queue = [(0,start,[start])]
    visited = set()
    while queue:
        cost,node,path = heapq.heappop(queue)
        if node == goal:
            return cost,path
        if node in visited:
            continue
        visited.add(node)
        for neighbor,weight in graph[node]:
            new_cost = cost + weight
            heapq.heappush(queue,(new_cost,neighbor,path+[neighbor]))
    return None

result = ucs("arad","buchaslest")
print("least cost path :")
print("->".join(result[1]))
print("total cost",result[0])



        
