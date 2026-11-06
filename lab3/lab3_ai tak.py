from collections import deque

graph = {"A": ["B", "C"], "B": ["D", "E"], "C": ["F"], "D": [], "E": ["G"], "F": [], "G": []}
def bfs(graph, start, goal):
    queue = deque([[start]])
    seen = {start}
    visit_order = []
    while queue:
        path = queue.popleft()
        node = path[-1]
        visit_order.append(node)
        if node == goal:
            return path, visit_order
        for next_node in graph[node]:
            if next_node not in seen:
                seen.add(next_node)
                queue.append(path + [next_node])
    return None, visit_order

def dfs(graph, start, goal):
    stack = [[start]]
    seen = set()
    visit_order = []
    while stack:
        path = stack.pop()
        node = path[-1]
        if node in seen:
            continue
        seen.add(node)
        visit_order.append(node)
        if node == goal:
            return path, visit_order
        for next_node in reversed(graph[node]):
            stack.append(path + [next_node])
    return None, visit_order

def dls(node, goal, limit, path):
    if node == goal:
        return "FOUND", path
    if limit == 0:
        if graph[node]:
            return "CUTOFF", None
        return "FAILURE", None
    cutoff_seen = False
    for next_node in graph[node]:
        if next_node in path:
            continue
        status, found_path = dls(next_node, goal, limit - 1, path + [next_node])
        if status == "FOUND":
            return status, found_path
        if status == "CUTOFF":
            cutoff_seen = True
    if cutoff_seen:
        return "CUTOFF", None
    return "FAILURE", None

weighted = {"A": [("B", 1), ("C", 6)], "B": [("D", 4), ("E", 1)], "C": [("F", 5), ("G", 6)], "D": [], "E": [("G", 1)], "F": [], "G": []}

def ucs(start, goal):
    frontier = [(0, start, [start])]
    best_cost = {start: 0}
    visit_order = []
    while frontier:
        frontier.sort()
        cost, node, path = frontier.pop(0)
        if cost != best_cost[node]:
            continue
        visit_order.append(node)
        if node == goal:
            return cost, path, visit_order
        for next_node, step_cost in weighted[node]:
            new_cost = cost + step_cost
            if new_cost < best_cost.get(next_node, 999):
                best_cost[next_node] = new_cost
                frontier.append((new_cost, next_node, path + [next_node]))

print("BFS:", bfs(graph, "A", "G"))
print("DFS:", dfs(graph, "A", "G"))
for limit in [1, 2, 3, 4]:
    print("DLS", limit, dls("A", "G", limit, ["A"]))
for max_depth in [1, 2, 3, 4]:
    for limit in range(max_depth + 1):
        status, path = dls("A", "G", limit, ["A"])
        if status == "FOUND" or limit == max_depth:
            print("IDDFS", max_depth, status, path)
            break
print("UCS:", ucs("A", "G"))
unweighted = {room: [next_room for next_room, cost in edges] for room, edges in weighted.items()}
print("BFS weighted:", bfs(unweighted, "A", "G"))
print("Same start and goal:", bfs(graph, "A", "A"))
