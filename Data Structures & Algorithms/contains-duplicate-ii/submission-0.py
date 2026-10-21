class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        numset = set()
        l = 0
        
        for r in range(len(nums)):
            if r-l > k:
                numset.remove(nums[l])
                l+=1
            if nums[r] in numset:
                return True
            numset.add(nums[r])
        return False
            
        