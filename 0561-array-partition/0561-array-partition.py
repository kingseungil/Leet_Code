class Solution:
    # 오름차순
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        sum = 0
        pair = []

        for n in nums:
            # 앞에서부터 오름차순으로 페어를 만들어서 합 계산
            pair.append(n)
            if len(pair) == 2:
                sum += min(pair)
                pair = []

        return sum

    # 짝수 번째 값만 계산(페어에 대해 min()값을 구하지 않아도 됨)
    def arrayPairSum2(self, nums: List[int]):
        sum = 0
        nums.sort()

        for i, n in enumerate(nums):
            # 짝수 번 째 값의 합 계산
            if i % 2 == 0:
                sum += n

        return sum

    # Pythonic Way -> slicing 활용
    def arrayPairSum3(self, nums: List[int]):
        return sum(sorted(nums)[::2])
