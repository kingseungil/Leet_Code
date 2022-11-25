class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)
        
        prefix = 1
        #왼쪽 곱셈
        for i in range(0,len(nums)):
            output[i] = prefix
            prefix *= nums[i]
            
        postfix = 1
        # 왼쪽 곱셈 결과에 오른쪽 값을 차례대로 곱셈
        for i in range(len(nums)-1,-1,-1):
            output[i] *= postfix
            postfix *= nums[i]
        
        return output