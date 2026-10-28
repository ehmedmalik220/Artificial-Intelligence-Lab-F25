from collections import deque

g = {"A": ["B", "C"], "B": ["D", "E"], "C": ["F"], "D": [], "E": ["G"], "F": [], "G": []}

def bfs(g, s, t):
    q = deque([[s]])
    seen = {s}
    v = []
    while q:
        p = q.popleft()
        n = p[-1]
        v.append(n)
        if n == t:
            return p, v
        for x in g[n]:
            if x not in seen:
                seen.add(x)
                q.append(p + [x])
    return None, v

def dfs(g, s, t):
    st = [[s]]
    seen = set()
    v = []
    while st:
        p = st.pop()
        n = p[-1]
        if n in seen:
            continue
        seen.add(n)
        v.append(n)
        if n == t:
            return p, v
        for x in reversed(g[n]):
            st.append(p + [x])
    return None, v

def dls(n, t, l, p):
    if n == t:
        return "FOUND", p
    if l == 0:
        return ("CUTOFF", None) if g[n] else ("FAILURE", None)
    cut = False
    for x in g[n]:
        if x in p:
            continue
        s, r = dls(x, t, l - 1, p + [x])
        if s == "FOUND":
            return s, r
        if s == "CUTOFF":
            cut = True
    return ("CUTOFF", None) if cut else ("FAILURE", None)

w = {"A": [("B", 1), ("C", 6)], "B": [("D", 4), ("E", 1)], "C": [("F", 5), ("G", 6)], "D": [], "E": [("G", 1)], "F": [], "G": []}

def ucs(s, t):
    f = [(0, s, [s])]
    best = {s: 0}
    done = []
    while f:
        f.sort()
        cost, n, p = f.pop(0)
        if cost != best[n]:
            continue
        done.append(n)
        if n == t:
            return cost, p, done
        for x, d in w[n]:
            nc = cost + d
            if nc < best.get(x, 999):
                best[x] = nc
                f.append((nc, x, p + [x]))

uw = {k: [x for x, _ in v] for k, v in w.items()}

print("BFS:", bfs(g, "A", "G"))
print("DFS:", dfs(g, "A", "G"))
for l in [1, 2, 3, 4]:
    print("DLS", l, dls("A", "G", l, ["A"]))
for m in [1, 2, 3, 4]:
    for l in range(m + 1):
        s, p = dls("A", "G", l, ["A"])
        if s == "FOUND" or l == m:
            print("IDDFS", m, s, p)
            break
print("UCS:", ucs("A", "G"))
print("BFS weighted:", bfs(uw, "A", "G"))
print("Same start and goal:", bfs(g, "A", "A"))
