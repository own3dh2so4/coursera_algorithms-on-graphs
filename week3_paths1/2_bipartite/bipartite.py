#Uses python3

import sys
import queue


def bipartite(adj):
    bipartite = [ None for _ in range(len(adj)) ]
    q = queue.Queue()
    for i in range(len(adj)):
        if bipartite[i] is None:
            bipartite[i] = True
            q.put(i)
            while not q.empty():
                x = q.get()
                value = bipartite[x]
                for v in adj[x]:
                    if bipartite[v] is None:
                        q.put(v)
                        bipartite[v] = not value
                    elif bipartite[v] == value:
                        return 0    
    return 1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(bipartite(adj))
