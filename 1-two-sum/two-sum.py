class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        keeper = {}
        for i in range(len(nums)):
            keeper.update({nums[i]:i})
        for i in range(len(nums)):
            sub = target-(nums[i])
            if sub in keeper and keeper[sub] != i:
                return [i,keeper[sub]]
        return []
        