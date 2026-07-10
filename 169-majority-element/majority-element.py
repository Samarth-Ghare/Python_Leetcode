class Solution(object):
    def majorityElement(self, maderchod):
        """
        :type nums: List[int]
        :rtype: int
        """
        d=defaultdict(int)
        for i in maderchod:
            d[i]+=1
        return max(d,key=lambda x:d[x])