class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l = max(nums)
        r = sum(nums)
        res = r

        def canSplit(largest):
            cnt = 1
            cur_sum = 0
            for n in nums:
                cur_sum+=n
                if cur_sum > largest:
                    cnt+=1
                    cur_sum = n
                    
            return cnt <= k

        while l <= r:
            mid = l + (r-l)//2
            if canSplit(mid):
                res = mid
                r = mid-1

            else:
                l= mid+1
        return res

        