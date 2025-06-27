class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:

        i , j = 0,0
        abbr_length , word_length = len(abbr), len(word)

        while i < abbr_length and j < word_length:
            if abbr[i].isdigit():
                if abbr[i] == '0':
                    return False
                nums = 0
                while i < abbr_length and abbr[i].isdigit():
                    nums = nums * 10 + int(abbr[i])
                    i += 1
                j += nums
            else:
                if abbr[i] != word[j]:
                    return False
                i += 1
                j += 1
                
        return i == abbr_length and j == word_length
        
