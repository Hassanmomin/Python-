from collections import deque
def print_board(state):
    for i in range(0,9,3):
        print(state[i:i+3])
    print()

def bfs (start,goal):
    queue = deque([(start,[])])
    visited = []
    while queue:
        state,path = queue.popleft()
        if state == goal:
            return path
        if state not in visited:
            visited.append(state)
            pos = state.index(0)
            moves = []
        if pos > 2:
            moves.append(pos - 3)
        if pos < 6:
            moves.append(pos + 3)
        if pos%3 != 0:
            moves.append(pos - 1)
        if pos%3 != 2:
            moves.append(pos + 1)
        for move in moves:
            new_state = state[:]
            new_state[pos],new_state[move] = \
            new_state[move],new_state[pos]
            queue.append((new_state,path + [new_state]))
    return None
start = [1,2,3,
         4,0,6,
         7,5,8]
goal = [1,2,3,
        4,5,6,
        7,8,0]
solution = bfs(start,goal)
print("initial state:")
print_board(start)
if solution:
    print("steps")
    for step in solution:
        print_board(step)
else:
    print("no solution found")











                
