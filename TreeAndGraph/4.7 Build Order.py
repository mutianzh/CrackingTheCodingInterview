"""
4.7 Build Order: You are given a list of projects and a list of dependencies (which is a list of pairs of
projects, where the second project is dependent on the first project). All of a project's dependencies
must be built before the project is. Find a build order that will allow the projects to be built. If there
is no valid build order, return an error.
EXAMPLE
Input:
projects: a, b, c, d, e, f
dependencies: (a, d), (f, b), (b, d), (f, a), (d, c)
Output: f, e, a, b, d, c
"""
import collections

graph = {}
graph['a'] = ['e']
graph['b'] = ['a', 'e']
graph['c'] = ['a']
graph['d'] = ['g']
graph['e'] = []
graph['f'] = ['a', 'b', 'c']
graph['g'] = []

# Non recursive method
def find_order_non_recur(graph):
    num_dep = collections.defaultdict(int)
    for key in graph.keys():
        for child in graph[key]:
            num_dep[child] += 1

    order = []
    for key in graph.keys():
        if num_dep[key] == 0:
            order.append(key)

    to_be_processed = 0
    while len(order) < len(graph.keys()):
        if to_be_processed + 1 > len(order):
            return False
        # remove myself from dependencies
        for child in graph[order[to_be_processed]]:
            num_dep[child] -= 1

        # check if there is new zero dependent project can be added
        for child in graph[order[to_be_processed]]:
            if num_dep[child] == 0:
                order.append(child)
        to_be_processed += 1

    return order
print(find_order_non_recur(graph))


# Recursive method
def find_order_dfs(graph):
    def dfs(node, stack):
        if status[node] == 'pending':
            return False

        if status[node] == 'blank':
            status[node] = 'pending'
            for child in graph[node]:
                if not dfs(child, stack):
                    return False

            status[node] = 'completed'
            stack.append(node)
        return True

    status = {}
    stack = []
    for key in graph.keys():
        status[key] = 'blank'

    for key in graph.keys():
        if not dfs(key, stack):
            return False
    return stack[::-1]

print(find_order_dfs(graph))









