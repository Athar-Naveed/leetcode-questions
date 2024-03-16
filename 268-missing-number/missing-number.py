class Solution(object):
    def missingNumber(self, number):
        if len(number) == 1:
            if number[0] == 1:
                return 0
            else:
                return 1
        else:
            sorted_array = sorted(number)
            for i in range(len(sorted_array)):
                if i != sorted_array[i]:
                    return i
                elif i == len(sorted_array)-1:
                    return i+1
            