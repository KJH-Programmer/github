from collections import deque
graph = {
    1: [2, 3, 4],
    2: [5],
    3: [5],
    4: [],
    5: [6, 7],
    6: [],
    7: [3],
}

def iterative_bfs(start_v):
    discovered = [start_v]
    #queue = [start_v]
    queue = deque([start_v])
    while queue:
        #v = queue.pop(0)
        v = queue.popleft()
        for w in graph[v]:
            if w not in discovered:
                discovered.append(w)
                queue.append(w)
    return discovered
    
print(f'{iterative_bfs(1)=}')   # iterative_bfs(1)=[1, 2, 3, 4, 5, 6, 7]