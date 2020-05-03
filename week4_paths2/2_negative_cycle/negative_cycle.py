#Uses python3

import sys


def relax(dist, u, v, cost, prev):
    if dist[v] is None or dist[v] > dist[u] + cost:
        dist[v] = dist[u] + cost
        prev[v] = u
        return True
    return False

def negative_cycle(adj, cost):
    visited = [ False for _ in range(len(adj))]
    for k in range(len(adj)):
        if not visited[k]:
            distances = [ None for _ in range(len(adj))]
            prev = [ -1 for _ in range(len(adj))]
            distances[k] = 0
            visited[k] = True
            changes = True
            i = 0
            max_i = len(adj)
            while i < max_i and changes:
                changes = False
                for u in range(len(adj)):
                    if distances[u] is not None:
                        j = 0
                        for v in adj[u]:
                            visited[v] = True
                            changes = relax(distances, u, v, cost[u][j], prev)
                            j += 1
                i += 1
            if changes:
                return 1
    return 0


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    print(negative_cycle(adj, cost))
