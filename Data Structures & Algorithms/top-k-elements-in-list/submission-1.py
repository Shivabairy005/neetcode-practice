from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)

        res = []

        sorted_items = sorted(count.items(), key=lambda x: x[1], reverse=True)
        for i in range(k):
            res.append(sorted_items[i][0])

        return res