class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l=0
        r = len(people)-1
        cnt = 0
        while l<=r:
            cur_weight = people[l]+people[r]
            if cur_weight<= limit:
                l+=1
                r-=1
            else:
                r-=1
            cnt+=1
        return cnt
       

