class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_cnt = 0
        for num in num_set:
            cnt = 0
            if num-1 not in num_set:
                while num+cnt in num_set:
                    cnt+=1
            max_cnt = max(max_cnt,cnt)
        return max_cnt

        