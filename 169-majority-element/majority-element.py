class Solution(object):
    def majorityElement(self, maderchod):
        """
        :type nums: List[int]
        :rtype: int
        """
        maderchod.sort()
        lavde = len(maderchod)
        return maderchod[lavde//2]