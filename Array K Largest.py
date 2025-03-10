from collections import Counter as ct

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count=ct(nums)
        return [x[0] for x in count.most_common(k)]
