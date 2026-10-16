class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = defaultdict(int)
        ans=[]
        for num in nums:
            counter[num]+=1
        
        res = [[] for _ in range(len(nums)+1)]

        for num,cnt in counter.items():
            res[cnt].append(num)
        

        for i in range(len(res)-1,0,-1):
            for num in res[i]:
                ans.append(num)
                if k==len(ans):
                    return ans