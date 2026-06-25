class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        nums.sort()
        val = nums[0]
        current_count = 1
        max_count = 1
        
        for i in range(1, len(nums)):
            if nums[i] == val:
                continue
            elif nums[i] == val + 1:
                current_count += 1
                val += 1
            else:
                max_count = max(max_count, current_count)
                current_count = 1
                val = nums[i]
                
        return max(max_count, current_count)