class Solution:
    def singleNumber(self,array):
        s_array = sorted(array)
        i = 0
        while i < len(s_array):
            if i == len(s_array)-1:
                return s_array[i]
            elif s_array[i] != s_array[i+1]:
                return s_array[i] 
            else:
                i += 2

array = [4,2,2,1,4]
s = Solution().singleNumber(array)
# print(s.f_array(array))