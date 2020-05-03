#Uses python3

import sys


def explore(adj, x, used, order):
    used.append(x)
    for v in adj[x]:
        if v not in used:
            explore(adj, v, used, order)
    order.insert(0, x)

def dfs(adj, used, order):
    for v in range(len(adj)):
        if v not in used:
            explore(adj, v, used, order)


def toposort(adj):
    used = []
    order = []
    dfs(adj, used, order)
    return order

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    order = toposort(adj)
    for x in order:
        print(x + 1, end=' ')

