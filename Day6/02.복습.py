graph = {
    1: [2, 3, 4],
    2: [5],
    3: [5],
    4: [],
    5: [6, 7],
    6: [],
    7: [3],
}

def i_dfs(start_v):
    stack = [start_v]    # 탐색을 할 것
    discovered = []      # 탐색완료
    while stack:
        v = stack.pop()
        if v not in discovered:
            discovered.append(v)
            for w in graph[v]:
                stack.append(w)
    return discovered

print(f'{i_dfs(1)=}')            
