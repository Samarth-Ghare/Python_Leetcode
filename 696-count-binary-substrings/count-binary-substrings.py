import numpy as np
class Solution(object):
    def countBinarySubstrings(self, s):
        a = np.frombuffer(s.encode(), dtype=np.uint8)
        changes = np.where(np.diff(a) != 0)[0] + 1
        groups = np.diff(np.concatenate(([0], changes, [len(a)])))
        return int(np.sum(np.minimum(groups[:-1], groups[1:])))