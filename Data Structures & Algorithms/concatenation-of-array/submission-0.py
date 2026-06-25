class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:

        #length of the nums array 
        n = len(nums) 
        #init ans array with 2 * n size 
        ans = [0] * 2 * n # [0 , 0 , 0 , 0 , 0 , 0 , 0] a[0]
        """

        []
        a.append(10) [10]  a[0 + 4]
        """

        #Output: [1,4,1,2,1,4,1,2]

        for i in range(n):
            ans[i] = nums[i]
            ans[i + n] = nums[i]
        
        return ans

    


        
        
        