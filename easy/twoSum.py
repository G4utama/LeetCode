class Solution:
    def twoSum(self, nums, target):
        l = len(nums)
        for i in range(l-1):
            for j in range(i+1,l):
                if (i != j) and (nums[i] + nums[j] == target):
                    return [i,j]
        return []