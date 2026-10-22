class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        l=0
        score = 0
        total = 0
        for r in range(k):
            total+=calories[r]
        if total > upper:
            score += 1
        elif total < lower:
            score -= 1
        for r in range(k, len(calories)):
            total += calories[r]
            total -= calories[l]
            l += 1
            if total > upper:
                score += 1
            elif total < lower:
                score -= 1
        
        return score