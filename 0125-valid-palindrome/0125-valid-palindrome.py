class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs = []
        for char in s:
            if char.isalnum():  # isalnum() : 영문자, 숫자 여부를 판별하는 함수
                strs.append(char.lower())

        # 펠른드롬 여부 판별
        while len(strs) > 1:
            if strs.pop(0) != strs.pop():  # pop(0) : 맨 앞의 값을 가져옴, pop() : 맨 뒤의 값을 가져옴
                return False

        return True
