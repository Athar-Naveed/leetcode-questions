class Solution(object):
    def productExceptSelf(self, array):
        product = 1
        keeper = []
        zero_checker = []
        for i in range(len(array)):
            if array[i] == 0:
                zero_checker.append(i)
                continue
            elif len(zero_checker) >= 2:
                break
            else:
                product*= array[i]
        for i in range(len(array)):
            if len(zero_checker) >= 2:
                keeper.append(0)
            elif len(zero_checker) == 1:
                if i != zero_checker[0]:
                    keeper.append(0)
                else:
                    keeper.append(product)
            else:
                keeper.append(int(product/array[i]))
        return keeper
        