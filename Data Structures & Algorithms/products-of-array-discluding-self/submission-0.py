class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        def multiply(lst):
            res = 1

            for i in lst:
                res *= i

            return res
                
        output = [0] * len(nums)
        for j in range(len(nums)):
            output[j] = multiply(nums[:j]) * multiply(nums[j+1:])
        
        return output