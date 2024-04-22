class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:

        tree = defaultdict(list)
        l = len(parents)
        for i in range(l):
            tree[parents[i]].append(i)

        freqDict = defaultdict(int)
        def calCost(root):
            n = len(tree[root])
            p,s = 1,0
            if n==0:
                p = l - 1
                freqDict[p] += 1
            elif n == 1:
                r1 = calCost(tree[root][0])
                s = r1
                p = r1 *  max(1,l-1-s)
                freqDict[p] += 1
            else:
                r1 = calCost(tree[root][0])
                r2 = calCost(tree[root][1])
                s = r1 + r2
                p = r1 * r2 * max(1,l-1-s)
                freqDict[p] += 1

            return 1 + s
        calCost(0)
        # print (tree)
        return freqDict[max(freqDict.keys())]
        
