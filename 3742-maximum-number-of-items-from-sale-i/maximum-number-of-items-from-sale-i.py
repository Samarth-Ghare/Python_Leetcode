class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        factors, prices = zip(*items)
        have = [0] * (max(factors)+1)
        for fact in factors:
            have[fact] += 1
        gains = {fact: sum(have[fact::fact]) for fact in set(factors)}

        cheapest = min(prices)
        best = [money // cheapest for money in range(budget+1)]
        for fact, price in items:
            if(gain := gains[fact]) > price //cheapest:
                for money in range(budget, price - 1, -1):
                    best[money] = max(best[money], best[money - price] + gain)
        return best[budget]