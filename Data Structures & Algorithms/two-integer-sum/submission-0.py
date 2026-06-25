class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        missingElement = dict()

        for index , value in enumerate(nums):

            required = target - value

            if required in missingElement:
                return [missingElement[required] , index]

            missingElement[value] = index

        return None 