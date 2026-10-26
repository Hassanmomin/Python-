from heapq import heappop,heappush

goal = [
    [1,2,3],[4,5,6],[7,8,0]
    ]

def heuristic(state):
    h =0
    for i in range(3):
        for j in range(3):
            val = state[i][j]
            if val != 0:
                x = (val - 1) // 3
                y = (val - 1) % 3
                h += abs(
    return h

def blank(state):
    for i in range(3):
        forj in range(3):
            if state[i][j] == 0:
                return i,j

def get_neighbors(state):
    result = []
    x,y = blank(state)
    
    moves = [(-1,0),(1,0),(0,-1),(0,1)]
    
    for dx,dy in moves:
        nx,ny = x+dx,y+dy
        
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [row[:] for row in state]
            new_state[x][y],new_state[nx][ny] =new_state[nx][ny],new_state[x][y]
            result.append(new_state)
    return result

def aster(start):
    pq = []
    heappush(pq,(heuristic(start),0,start[]))
    visited = []
    while pq:
        p,g,state,path = heappop(pq)
        if state == goal:
            return path+[state]
        if state in visited:
            continue
        visited.append(state)
        for child in neighbor(state):
            heappush(pq,(g+1+heauristic(child),g+1,child,path+([state])))
    return None


start = [[1,2,3],[4,5,6],[1,5,8]]










            
