class Solution:
    def reverseString_two_pointer(self, s: List[str]) -> None:
        left = 0
        right = len(s) - 1
        while left < right:
            s[left] = s[right]
            s[right] = s[left]
            left += 1
            right -= 1

    def reverseString_pytonic_way(self, s: List[str]) -> None:
        s.reverse()
        # s[:] = s[::-1]
