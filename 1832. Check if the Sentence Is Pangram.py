class Solution:
    def checkIfPangram(self, sentence: str) -> bool:

        if len(sentence) < 26:
            return False
            
        seen = set()
        
        for c in sentence:
            if c.isalpha():
                seen.add(c)

        return len(seen) == 26
      #time: O(n) space: O(1) #26 char
        
