#Uses python3

import sys

sys.setrecursionlimit(200000)

def reverse_graph(adj):
    reverse_adj = [[] for _ in range(len(adj))]
    for i in range(len(adj)):
        for j in adj[i]:
            reverse_adj[j].append(i)
    return reverse_adj   


def explore(adj, x, visited, removed=[], post_order=None):
    visited.append(x)
    for v in adj[x]:
        invalid_vertex = visited + removed
        if v not in invalid_vertex:
            explore(adj, v, visited, removed=removed, post_order=post_order)
    if post_order is not None:
        post_order.append(x)


def dfs(adj):
    visited = []
    post_order = []
    for v in range(len(adj)):
        if v not in visited:
            explore(adj, v, visited, post_order=post_order)
    return post_order
        

def number_of_strongly_connected_components(adj):
    reverse_adj = reverse_graph(adj)
    post_order = dfs(reverse_adj)
    visited_total = []
    all_visited = []
    for v in reversed(post_order):
        if v not in all_visited:
            visited = []
            explore(adj, v, visited, removed=all_visited)
            visited_total.append(visited)
            all_visited.extend(visited)
    return len(visited_total)

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(number_of_strongly_connected_components(adj))
