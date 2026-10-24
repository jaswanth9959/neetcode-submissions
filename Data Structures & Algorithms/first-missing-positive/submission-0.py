class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        if nums[0] > 1:
            return 1
        else:
            i = 1
            numset = set(nums)
            while True:
                if i not in numset:
                    return i
                i+=1