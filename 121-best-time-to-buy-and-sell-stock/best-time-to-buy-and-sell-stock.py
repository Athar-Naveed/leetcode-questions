class Solution(object):
    def maxProfit(self, array):
        if len(array) == 1:
            return 0
        else:
            profit_keeper = []
            maxi,mini = 0,0
            for i in range(len(array)-1):
                if array[i+1] > array[mini]:
                    maxi = i+1
                elif array[i+1] < array[maxi]:
                    mini = i+1
                if mini < maxi:
                    profit_keeper.append(array[maxi]-array[mini])
            if profit_keeper:
                return max(profit_keeper)
            else:
                return 0
        