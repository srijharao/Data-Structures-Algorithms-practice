class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #Keys are hashed(immutable) and values are mutable
        #sorted gives a list output - not hashable as it can be appended to
        #tuple 'q''e''t'
        mp = defaultdict(list)
        for word in strs:
            mp[tuple(sorted(word))].append(word)
        return list(mp.values())
