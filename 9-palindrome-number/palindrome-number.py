class Solution(object):
    def isPalindrome(self, number):
        number = int(number)
        if number < 0:
            return False
        elif number == 0:
            return True
        number_list = []
        while number > 0:
            rem = number%10
            number_list.insert(0,rem)
            number = int(number/10)
        if len(number_list) == 1:
            return True
        else:
            start = 0
            end =  len(number_list)-1
            while start <= int(len(number_list)/2):
                if number_list[start] != number_list[end]:
                    return False
                else:
                    start += 1
                    end += -1
            return True
            