class Solution:
    def minTimeMaxPower(self, n: int, edges: List[List[int]], power: int, cost: List[int], source: int, target: int) -> List[int]:
        adj = [[] for _ in range(n)]
        for u, v, t in edges:
            adj[u].append((v,t))
        max_p = [-1] *n
        pq = [(0, -power, source)]
        while pq:
            t, neg_p, u = heapq.heappop(pq)
            p = -neg_p
            if u == target:
                return [t, p]
            if p <=max_p[u]:
                continue
            max_p[u] = p
            if p >= cost[u]:
                next_p = p-cost[u]
                for v, weight in adj[u]:
                    if next_p > max_p[v]:
                        heapq.heappush(pq, (t+weight, -next_p, v))
        return [-1, -1]