import collections
import re
from typing import Deque


class Solution:
    # 1. list 활용
    def isPalindrome_list(self, s: str) -> bool:
        strs = []
        for char in s:
            if char.isalnum():  # isalnum() : 영문자, 숫자 여부를 판별하는 함수
                strs.append(char.lower())  # lower() : 소문자로 바꿔주는 함수

        # 펠른드롬 여부 판별
        while len(strs) > 1:
            if strs.pop(0) != strs.pop():  # pop(0) : 맨 앞의 값을 가져옴, pop() : 맨 뒤의 값을 가져옴
                                           # O(N) + O(1)
                return False

        return True

    # 2.deque 활용
    def isPalindrome_deque(self, s: str) -> bool:

        # 자료형 데크로 선언
        # strs: collections.deque = collections.deque()
        strs = Deque()

        for char in s:
            if char.isalnum():
                strs.append(char.lower())

        while len(strs) > 1:
            if strs.popleft() != strs.pop():  # O(1) + O(1)
                return False

        return True

    # 3.slicing 활용
    def isPalindrome_slicing(self, s: str) -> bool:
        s = s.lower()
        # 정규식으로 불필요한 문자 필터링
        s = re.sub('[^a-z0-9]', '', s)

        return s == s[::-1]  # 슬라이싱
