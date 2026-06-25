class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        #insert all the elements in the nums in. set

        numSet = set(nums)

        return True if len(numSet) != len(nums) else False