class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = {0:1}

        res = 0
        s = 0
        for num in nums:
            s += num
            diff = s - k
            if diff in prefix_sum:
                res+=prefix_sum[diff]
            prefix_sum[s] = 1 + prefix_sum.get(s,0)
        return res
        