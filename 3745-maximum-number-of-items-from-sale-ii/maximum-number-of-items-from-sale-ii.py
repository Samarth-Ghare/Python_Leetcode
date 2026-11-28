class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        factors, prices = zip(*items)
        have = [0] * (len(items)+1)
        for fact in factors:
            have[fact] += 1
        deals = cache(lambda fact:sum(have[fact::fact])-1)

        cheapest = min(prices) 
        heap = [(price, fact) for fact, price in items if price < 2 * cheapest]
        heapify(heap)
        copies = 0
        while heap and heap[0][0] <= budget:
            price, fact = heappop(heap)
            pairs = min(deals(fact), budget // price)
            copies += 2*pairs
            budget -= pairs * price
        return copies + budget // cheapest