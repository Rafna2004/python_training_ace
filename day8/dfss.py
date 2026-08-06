from typing import Dict, List

def dfs_iterative(graph: Dict[int, List[int]], start_node: int) -> List[int]:
    visited_order = []
    seen = {start_node}
    stack = [start_node]
    
    while stack:
        node = stack.pop()
        visited_order.append(node)
        for neighbor in graph[node]:
            if neighbor not in seen:
                seen.add(neighbor)
                stack.append(neighbor)
    return visited_order

print("---Depth First Search (DFS) Results---")
