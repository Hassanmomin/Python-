from heapq import heappush,heappop

GOAL = [[1,2,3],[4,5,6],[7,8,0]]

def manhatton(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            value = state[i][j]
            if value != 0:
                goal_x = (value-1) // 3
                goal_y = (value-1) % 3
                distance += abs(i - goal_x) + abs(j-goal_y)
    return distance

def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i,j

def get_neighbors(state):
    neighbors = []
    x,y = find_blank(state)
    
    moves = [(-1,0),(1,0),(0,-1),(0,1)]
    
    for dx,dy in moves:
        nx,ny = x+dx,y+dy
        
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [row[:] for row in state]
            new_state[x][y],new_state[nx][ny] =new_state[nx][ny],new_state[x][y]
            neighbors.append(new_state)
    return neighbors

def state_to_tuple(state):
    return tuple(tuple(row) for row in state)

def greedy_best_first_search(start):
    pq = []
    heappush(pq,(manhatton(start),0,start,[start]))
    visited = set()
    while pq:
        f,g,current,path = heappop(pq)
        if current == GOAL:
            return path
        state_key = state_to_tuple(current)
        if state_key in visited:
            continue
        visited.add(state_key)
        for neighbor in get_neighbors(current):
            if state_to_tuple(neighbor) not in visited:
                heappush(
                    pq,
                    (
                        g+1+manhatton(neighbor),
                        g+1,
                        neighbor,
                        path + [neighbor]

                        )
                    )
    return None


def print_state(state):
    for row in state:
        print(row)
    print()

start_state = [[1,2,3],[4,0,6],[7,5,8]]

solution = greedy_best_first_search(start_state)

if solution:
    print("solution found //n")

    for step,state in enumerate(solution):
        print(f"step {step}:")
        print_state(state)
        print("total move :",len(solution) - 1)

else:
    print("no solution found..")







































            
