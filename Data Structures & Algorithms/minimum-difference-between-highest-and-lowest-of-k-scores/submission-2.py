class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        l=0
        r=k-1
        res = float("inf")
        
        
        while r < len(nums):
            diff = nums[r] - nums[l]
            res = min(diff , res)

            l+=1
            r+=1
        return res

        