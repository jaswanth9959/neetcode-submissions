class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        l=0
        cnt = 0
        min_cnt = float("inf")
        for r in range(k):
            if blocks[r] == "W":
                cnt+=1
        r = k

        if k == len(blocks):
            return cnt
        while r < len(blocks):
            if blocks[r] == "W":
                cnt+=1
            if blocks[l] == "W":
                cnt-=1
            l+=1
            r+=1
            min_cnt = min(min_cnt, cnt)
        return min_cnt


        