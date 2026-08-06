from typing import Dict, List
from collections import deque

def bfs_traversal(graph: Dict[int, List[int]], start_node: int) -> List[int]:
    visited_order = []
    seen = {start_node}
    queue = deque([start_node])  
    
    while queue:
        node = queue.popleft()   
        visited_order.append(node)
        for neighbor in graph[node]:
            if neighbor not in seen:
                seen.add(neighbor)
                queue.append(neighbor)
    return visited_order
print("---Breadth First Search (BFS) Results---")
