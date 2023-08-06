def dfs_recursive(graph, node, visited):
    if node not in visited:
        visited.add(node)
        print("Visiting node:", node)
        for neighbor in graph[node]:
            dfs_recursive(graph, neighbor, visited)

# Example usage:
graph = {
    1: [2, 3],
    2: [1, 4, 5],
    3: [1],
    4: [2],
    5: [2]
}

visited_nodes = set()
dfs_recursive(graph, 1, visited_nodes)
