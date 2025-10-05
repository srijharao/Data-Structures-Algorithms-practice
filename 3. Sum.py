class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #time: O(n^2)
        #space: O(m+n) other than o/p

        nums.sort()
        resSet = set()
        
        for i in range(len(nums)):
            j = i + 1
            k = len(nums)-1
            while(j < k):
                if (nums[i] + nums[j] + nums[k] == 0):
                    resSet.add((nums[i], nums[j], nums[k])) #space seen: O(m)
                    j += 1
                elif (nums[i] + nums[j] + nums[k] > 0):
                    k -= 1
                else:
                    j += 1

        return [list(i) for i in resSet] #space: o(n) converting to list

    #remove duplicates, use list
    #time: O(n^2) ; Space: O(1) other than o/p
    def threeSum(self, nums: List[int]) -> List[List[int]]:
            result = []
            nums.sort()
    
            for i in range(len(nums)):
                j = i+1
                k = len(nums)-1
                if i >0 and nums[i] == nums[i-1]:
                    continue
                while j < k:
                    total = nums[i] + nums[j] + nums[k]
                    if total == 0:
                        result.append([nums[i],nums[j],nums[k]])
                        j += 1
                        k -= 1
                        while j<k and nums[j] == nums[j-1]:
                            j += 1
                        while j<k and nums[k] == nums[k+1]:
                            k -= 1
                        
                    elif total < 0:
                        j += 1
                    else:
                        k -= 1
            
            return result
        
