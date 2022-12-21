class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {
            ')':'(',
            '}':'{',
            ']':'[',
        }
        
        for char in s:
            print(char)
            if char not in mapping:
                stack.append(char)
                # print(stack)
            elif not stack or mapping[char] != stack.pop():
                return False

        return len(stack) == 0