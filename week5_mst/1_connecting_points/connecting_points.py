#Uses python3
import sys
import math

def distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 -y2) ** 2)

def minimum_distance(x, y):
    size = len(x)
    result = 0.
    edges = []
    for i in range(size):
        for j in range(i + 1, size):
            edges.append((i,j, distance(x[i], y[i], x[j], y[j])))
    edges.sort(key=lambda x: x[2])
    nodes = [set([i]) for i in range(size)]
    for e in edges:
        if e[0] not in nodes[e[1]] and e[1] not in nodes[e[0]]:
            nodes[e[0]] = nodes[e[1]].union(nodes[e[0]])
            for i in nodes[e[1]]:
                nodes[i] = nodes[e[0]]
            result += e[2]
    return result


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))
