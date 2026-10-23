class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)
        res = r

        def canShip(cap):
            cnt, curCap = 1, cap
            for w in weights:
                if curCap - w < 0:
                    cnt+=1
                    curCap = cap
                curCap -= w
            return cnt <= days


        while l <= r:
            capacity = (l+r)//2
            if canShip(capacity):
                res = min(res , capacity)
                r = capacity -1
            else:
                l = capacity +1
        return res
            

