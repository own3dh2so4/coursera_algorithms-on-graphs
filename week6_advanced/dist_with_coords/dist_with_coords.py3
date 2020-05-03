#!/usr/bin/python3

import sys
import queue
import math

class AStar:
    def __init__(self, n, adj, cost, x, y):
        # See the explanations of these fields in the starter for friend_suggestion        
        self.n = n;
        self.adj = adj
        self.cost = cost
        self.inf = n*10**6
        self.d = [self.inf]*n
        self.visited = [False]*n
        self.workset = []
        # Coordinates of the nodes
        self.x = x
        self.y = y

    # See the explanation of this method in the starter for friend_suggestion
    def clear(self):
        for v in self.workset:
            self.d[v] = self.inf
            self.visited[v] = False;
        del self.workset[0:len(self.workset)]

    # See the explanation of this method in the starter for friend_suggestion
    def visit(self, q, v, dist, measure):
        #print("Analizo {} con dist {} actual {}".format(v, dist, self.d[v]))
        if self.d[v] > dist:
            self.d[v] = dist
            #print("Meto {} con prioridad {} distancia {}".format(v, dist + measure, dist))
            q.put((dist + measure, v))
            self.workset.append(v)

    # Returns the distance from s to t in the graph
    def query(self, s, t):
        self.clear()
        q = queue.PriorityQueue()
        # Implement the rest of the algorithm yourself
        self.visit(q,s,0,0)
        self.visited[s] = True
        self.workset.append(s)
        while not q.empty():
            priority, u = q.get()
            #print("Saco {} con prioridad {}".format(u, priority))
            if u == t:
                return self.d[u]
            for i in range(len(self.adj[u])):
                v = adj[u][i]
                self.visit(q, v, self.d[u] + self.cost[u][i], prio(self.x[u], self.y[u], self.x[v], self.y[v]))
            self.visited[u] = True
        return -1

def prio(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def readl():
    return map(int, sys.stdin.readline().split())

if __name__ == '__main__':
    n,m = readl()
    x = [0 for _ in range(n)]
    y = [0 for _ in range(n)]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for i in range(n):
        a, b = readl()
        x[i] = a
        y[i] = b
    for e in range(m):
        u,v,c = readl()
        adj[u-1].append(v-1)
        cost[u-1].append(c)
    t, = readl()
    astar = AStar(n, adj, cost, x, y)
    for i in range(t):
        s, t = readl()
        print(astar.query(s-1, t-1))
