class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        check_duplicate_set = set()

        for index , value in enumerate(nums):

            if value in check_duplicate_set:
                return True
            check_duplicate_set.add(value)
        
        return False