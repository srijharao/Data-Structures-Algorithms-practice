class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        mp = defaultdict(int)
        for i in arr:
            mp[i] = mp[i] + 1
        
        unique = list(mp.values())

        return len(unique) == len(set(unique))
        
