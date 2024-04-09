class Solution(object):
    def containsDuplicate(self, nums):
        sorted_array = sorted(nums)
        i = 0
        while i < len(sorted_array)-1:
            j = i+1
            if sorted_array[j] == sorted_array[i]:
                return True
            i+=1
        return False
        