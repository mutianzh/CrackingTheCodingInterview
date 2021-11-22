"""
4.1 Route Between Nodes: Given a directed graph, design an algorithm to find out whether there is a
route between two nodes.
"""
import collections

def find_route_bfs(G, node_1, node_2):
    visited = {}
    queue = G[node_1]
    while queue:
        n = queue.pop(0)
        if n not in visited:
            if n == node_2:
                return True
            visited[n] = True
            queue += G[n]

    return False



G1 = collections.defaultdict(list)
G1[0] = [1,5]
G1[1] = [4,2]
G1[2] = [3]
G1[3] = [0,1]
G1[4] = [3]
G1[5] = [4]

G2 = collections.defaultdict(list)
G2[0] = [1,4,5]
G2[1] = [3,4]
G2[2] = [1]
G2[3] = [2,4]

print(find_route_bfs(G1, 1, 5))
print(find_route_bfs(G2, 0, 3))







