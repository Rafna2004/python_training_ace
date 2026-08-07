"""
LeetCode 547: Number of Provinces

Problem Description:
There are n cities. Some of them are connected, while some are not.
If city a is connected directly with city b, and city b is connected directly with city c,
then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and
the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.
"""

from typing import List
from collections import deque


class Solution:
    def findCircleNumDFS(self, isConnected: List[List[int]]) -> int:
        """
        Approach 1: Depth First Search (DFS)
        Time Complexity: O(n^2)
        Space Complexity: O(n) for visited array and recursion stack
        """
        n = len(isConnected)
        visited = [False] * n
        provinces = 0

        def dfs(city: int):
            for neighbor in range(n):
                if isConnected[city][neighbor] == 1 and not visited[neighbor]:
                    visited[neighbor] = True
                    dfs(neighbor)

        for i in range(n):
            if not visited[i]:
                visited[i] = True
                provinces += 1
                dfs(i)

        return provinces

    def findCircleNumBFS(self, isConnected: List[List[int]]) -> int:
        """
        Approach 2: Breadth First Search (BFS)
        Time Complexity: O(n^2)
        Space Complexity: O(n) for visited array and queue
        """
        n = len(isConnected)
        visited = [False] * n
        provinces = 0

        for i in range(n):
            if not visited[i]:
                provinces += 1
                visited[i] = True
                queue = deque([i])
                
                while queue:
                    curr = queue.popleft()
                    for neighbor in range(n):
                        if isConnected[curr][neighbor] == 1 and not visited[neighbor]:
                            visited[neighbor] = True
                            queue.append(neighbor)

        return provinces

    def findCircleNumUnionFind(self, isConnected: List[List[int]]) -> int:
        """
        Approach 3: Union-Find (Disjoint Set Union - DSU)
        Time Complexity: O(n^2 * alpha(n))
        Space Complexity: O(n) for parent array
        """
        n = len(isConnected)
        parent = list(range(n))
        provinces = n

        def find(i: int) -> int:
            if parent[i] != i:
                parent[i] = find(parent[i])  # Path compression
            return parent[i]

        def union(i: int, j: int) -> bool:
            nonlocal provinces
            root_i = find(i)
            root_j = find(j)
            if root_i != root_j:
                parent[root_i] = root_j
                provinces -= 1
                return True
            return False

        for i in range(n):
            for j in range(i + 1, n):
                if isConnected[i][j] == 1:
                    union(i, j)

        return provinces


# Test cases for verification
if __name__ == "__main__":
    sol = Solution()

    # Test Case 1
    isConnected1 = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
    expected1 = 2
    res_dfs1 = sol.findCircleNumDFS(isConnected1)
    res_bfs1 = sol.findCircleNumBFS(isConnected1)
    res_dsu1 = sol.findCircleNumUnionFind(isConnected1)
    print(f"Test 1 - DFS: {res_dfs1}, BFS: {res_bfs1}, DSU: {res_dsu1} (Expected: {expected1})")
    assert res_dfs1 == expected1 and res_bfs1 == expected1 and res_dsu1 == expected1

    # Test Case 2
    isConnected2 = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    expected2 = 3
    res_dfs2 = sol.findCircleNumDFS(isConnected2)
    res_bfs2 = sol.findCircleNumBFS(isConnected2)
    res_dsu2 = sol.findCircleNumUnionFind(isConnected2)
    print(f"Test 2 - DFS: {res_dfs2}, BFS: {res_bfs2}, DSU: {res_dsu2} (Expected: {expected2})")
    assert res_dfs2 == expected2 and res_bfs2 == expected2 and res_dsu2 == expected2

    print("All test cases passed successfully!")
