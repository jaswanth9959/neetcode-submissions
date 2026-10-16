class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # num_set = set(nums)
        # return not len(num_set) == len(nums)

        nums.sort()
        for i in range(1,len(nums)):
            if nums[i-1] == nums[i]:
                return True
        return False
        