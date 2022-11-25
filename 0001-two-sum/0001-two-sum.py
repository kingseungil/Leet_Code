class Solution:
    # Brute-Force
    def two_sum_brute_force(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

    # in을 이용한 탐색
    def two_sum_in(self, nums: List[int], target: int):
        for i, n in enumerate(nums):
            complement = target - n

            if complement in nums[i+1]:
                return [nums.index(n), nums[i+1].index(complement)+(i+1)]

    # 첫 번째 수를 뺀 결과 키 조회
    def two_sum(self, nums: List[int], target: int):
        nums_map = {}
        # 키와 값을 바꿔서 딕셔너리로 저장
        for i, num in enumerate(nums):
            nums_map[num] = i

        # 타겟에서 첫 번째 수를 뺀 결과를 키로 조회
        for i, num in enumerate(nums):
            if (target - num in nums_map) and (i != nums_map[target-num]):
                return [i, nums_map[target-num]]
