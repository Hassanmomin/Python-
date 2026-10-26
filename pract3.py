def dfs(x,y):
    if(x,y) in visited:
        return False
    visited.add((x,y))
    print("Jug 1:",x,"Jug 2:",y)
    if x == target or y == target:
        print("Goal Reched..!")
        return True
    
    if dfs(cap1,y):
        return True
    if dfs(x,cap2):
        return True
    if dfs(0,y):
        return True
    if dfs(x,0):
        return True
    
    transfer = min(x,cap2-y)
    if dfs(x-transfer,y+transfer):
        return True
    
    transfer = min(y,cap1-x)
    if dfs(x+transfer,y-transfer):
        return True
    
    return False


cap1 = 4
cap2 = 3
target = 2
visited = set()
print("DFS water Jug Problem:\n")
dfs(0,0)







