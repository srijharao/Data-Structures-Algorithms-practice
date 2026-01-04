class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:

        for c1, c2 in zip(self.generate(word1), self.generate(word2)):
            if c1 != c2:
                return False
        return True
      #O(min(m,n)) for zip iteration

    def generate(self, wordlist): #O(m+n) 2 strings
        for word in wordlist:
            for c in word:
                yield c
        yield None
        
