import numpy as np
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        d = {}
        for n in nums:
            d[n] = d.get(n, 0) + 1
        # sort the numbers by count, highest first, and keep the first k
        return sorted(d, key=d.get, reverse=True)[:k]
        
        