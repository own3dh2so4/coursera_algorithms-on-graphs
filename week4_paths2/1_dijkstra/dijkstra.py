#Uses python3

import sys
import queue


def distance(adj, cost, s, t):
    distances = [ -1 for _ in range(len(adj))]
    prev = [ -1 for _ in range(len(adj))]
    distances[s] = 0
    q = queue.PriorityQueue()
    q.put((0, s))
    while not q.empty():
        value, x = q.get()
        if distances[x] == -1 or distances[x] >= value:
            i = 0
            for v in adj[x]:
                if distances[v] == -1 or distances[v] > distances[x] + cost[x][i]:
                    distances[v] = distances[x] + cost[x][i]
                    prev[v] = x                    
                    q.put((distances[v], v))
                i += 1
    return distances[t]


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
    s, t = data[0] - 1, data[1] - 1
    print(distance(adj, cost, s, t))
