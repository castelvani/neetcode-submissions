class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        validate = {}
        for i, val in enumerate(nums):
            validate[val] = i

        return len(validate) != len(nums)

