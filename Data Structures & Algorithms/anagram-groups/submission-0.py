class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res = defaultdict(list)
        for s in strs:
            char_arr = [0] * 26
            for ch in s:
                char_arr[ord(ch) - ord("a")]+=1
            res[tuple(char_arr)].append(s)
        
        return list(res.values())


        