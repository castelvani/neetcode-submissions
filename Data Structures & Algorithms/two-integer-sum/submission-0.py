class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}

        for i, val in enumerate(nums):
            map[val] = i

        for i, val in enumerate(map):
            if target - val in map and i != map[target - val]:
                return [i, map[target - val]]