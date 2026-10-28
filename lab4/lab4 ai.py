g = {"S": [("A", 1), ("B", 4)], "A": [("C", 2)], "B": [("G", 5)], "C": [("G", 3)], "G": []}
h = {"S": 5, "A": 4, "B": 4, "C": 2, "G": 0}

def astar(s, t, h):
    f = [(h[s], 0, s, [s])]
    best = {s: 0}
    done = []
    while f:
        f.sort()
        _, cost, n, p = f.pop(0)
        if cost != best[n]:
            continue
        done.append(n)
        if n == t:
            return cost, p, done
        for x, d in g[n]:
            nc = cost + d
            if nc < best.get(x, 999):
                best[x] = nc
                f.append((nc + h[x], nc, x, p + [x]))

h2 = dict(h)
h2["C"] = 10

print("A*:", astar("S", "G", h))
print("UCS:", astar("S", "G", {k: 0 for k in h}))
print("Overestimate:", astar("S", "G", h2))
