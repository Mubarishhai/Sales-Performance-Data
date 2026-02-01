class Solution:
    def minimumCost(self, nums):
        # First element always contributes to cost
        first = nums[0]

        # Get the two smallest elements from the rest
        rest = sorted(nums[1:])

        return first + rest[0] + rest[1]
