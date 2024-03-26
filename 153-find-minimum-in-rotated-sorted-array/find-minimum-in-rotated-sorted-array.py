class Solution(object):
    def findMin(self, nums):
        if len(nums) == 1:
            return int(nums[0])
        elif len(nums) == 2:
            if nums[0] > nums[1]:
                return int(nums[1])
            else:
                return int(nums[0])
        else:
            
            mid = int(len(nums)/2)
            arr1 = nums[:mid]
            arr2 = nums[mid:]
            mini1 = min(arr1)
            mini2 = min(arr2)
            if mini1 > mini2:
                return int(mini2)
            else:
                return int(mini1)
            