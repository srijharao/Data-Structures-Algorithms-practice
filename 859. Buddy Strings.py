class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        swap = []

        if len(s) != len(goal):
            return False

        #when strings are equal replacement is possible if there are duplicates aa aba
        if s == goal: 
            return True if len(s) - len(set(goal)) >= 1 else False

        #calculate how many differences, invalid if more than 2
        for i in range(len(goal)):
            if(s[i] != goal[i]):
                swap.append(i)
        if(len(swap) != 2):
            return False
        else:
            if(goal[swap[1]] == s[swap[0]] and goal[swap[0]] == s[swap[1]]):
                return True
        return False
